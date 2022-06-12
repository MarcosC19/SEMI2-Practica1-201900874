from .loggerConfig import logger
from .database import executeQuery
import pandas as pd

dist_artist_table = 'INSERT INTO artist_dimension(artist_name)\
                     SELECT DISTINCT artist FROM temporal\
                     ORDER BY artist;'

dist_song_table = 'insert into song_dimension(song_name, duration_ms, explicit, song_year, popularity, genre)\
                   select t_aux.song, t_aux.duration_ms, t_aux.explicit, t_aux.song_year, t_aux.popularity, t_aux.genre\
                   from\
                   (\
                   select distinct artist, upper(song) as song, cast(avg(duration_ms) as signed) as duration_ms, explicit,\
                   song_year, cast(avg(popularity) as signed) as popularity, genre from temporal\
                   group by artist, song\
                   order by song\
                   ) as t_aux;'

dist_music_table = 'insert into music_fact(id_artist, id_song, reproduccion, danceability, energy, music_key, loudness,\
                    music_mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo)\
                    select artD.id_artist, songD.id_song, auxiliar.reproduccion, auxiliar.danceability, auxiliar.energy, auxiliar.music_key, auxiliar.loudness,\
                    auxiliar.music_mode, auxiliar.speechiness, auxiliar.acousticness, auxiliar.instrumentalness, auxiliar.liveness, auxiliar.valence, auxiliar.tempo\
                    from\
                    (\
                    select artist, upper(song) as song, count(song) as reproduccion,danceability, energy, music_key, loudness, music_mode, speechiness,\
                    acousticness, instrumentalness, liveness, valence, tempo, song_year, genre\
                    from temporal\
                    group by artist, song\
                    ) as auxiliar\
                    inner join artist_dimension as artD\
                    on artD.artist_name = auxiliar.artist\
                    inner join song_dimension as songD\
                    on songD.song_name = auxiliar.song and songD.song_year = auxiliar.song_year and songD.genre = auxiliar.genre;'

def dataLoad():
    try:
        # READING DATASET INFORMATION
        logger.info("Comenzando lectura del dataset...")
        logger.info("Solicitando la ruta del archivo")
        pathData = input("Ingrese la ruta donde se encuentra los datos a utilizar: ")
        logger.info("Leyendo el archivo...")
        dataSet = pd.read_csv(pathData)
        dataFrame = pd.DataFrame(dataSet)
        logger.info("Archivo leido con exito")
        # LOADING INFORMATION TO MODEL
        logger.info("Comenzando carga del dataset...")
        loadTemporal(dataFrame)
        # DATA DISTRIBUTION
        logger.info("Comenzando distribucion de informacion...")
        loadTables()
    except Exception as e:
        logger.error(e)
        print("Ocurrio un error")

def loadTemporal(dataFrame):
    i = 0
    for row in dataFrame.itertuples():
        i+= 1
        # cleaning data artist, replacing " to '
        artist = str(row[1]).replace("\"", "'")
        # cleaning data song, replacing " to '
        song = str(row[2]).replace("\"", "'")
        # cleaning data genre, replcaing "set()" to "otros"
        genre = str(row[18])
        if genre == 'set()':
            genre = 'otros'
        executeQuery(f'INSERT INTO temporal VALUES("{artist}", "{song}", {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, "{genre}")', 'insert')
        logger.info(f'Fila {i} insertada con exito')
    logger.info("Carga del dataset finalizado")
    logger.info(f'Se cargaron correctamente {i} filas')

def loadTables():
    logger.info("Cargando informacion de los artistas...")
    executeQuery(dist_artist_table, 'insert')
    logger.info("Cargando informacion de las canciones...")
    executeQuery(dist_song_table, 'insert')
    logger.info("Cargando informacion de la musica...")
    executeQuery(dist_music_table, 'insert')
    logger.info("Distribucion de informacion finalizada")