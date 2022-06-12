from .loggerConfig import logger
from .database import getQuerySelect
from tabulate import tabulate

query1 = '\
    SELECT artist_name, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join artist_dimension artD\
    on msF.id_artist = artD.id_artist\
    group by artist_name\
    order by reproducciones desc\
    limit 10;\
'

query2 = '\
    SELECT artist_name, song_name, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join artist_dimension artD\
    on msF.id_artist = artD.id_artist\
    inner join song_dimension songD\
    on msF.id_song = songD.id_song\
    group by artist_name, song_name\
    order by reproducciones desc\
    limit 10;\
'

query3 = '\
    SELECT genre, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join song_dimension songD\
    on msF.id_song = songD.id_song\
    group by genre\
    order by reproducciones desc\
    limit 5;\
'

query4 = '\
    select aux.artist_name artist_name, aux.genre genre, max(aux.reproducciones) as reproducciones\
    from\
    (\
    SELECT artist_name, genre, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join artist_dimension artD\
    on msF.id_artist = artD.id_artist\
    inner join song_dimension songD\
    on msF.id_song = songD.id_song\
    group by artist_name, genre\
    order by reproducciones desc\
    ) aux\
    group by genre\
    order by genre;\
'

query5 = '\
    select aux.artist_name, aux.song_name song_name, aux.genre genre, max(aux.reproducciones) as reproducciones\
    from\
    (\
    SELECT artist_name, song_name, genre, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join artist_dimension artD\
    on msF.id_artist = artD.id_artist\
    inner join song_dimension songD\
    on msF.id_song = songD.id_song\
    group by artist_name,song_name, genre\
    order by reproducciones desc\
    ) aux\
    group by genre\
    order by genre;\
'

query6 = '\
    select aux.artist_name, aux.song_name, aux.song_year, max(aux.reproducciones) reproducciones\
    from\
    (\
    SELECT artist_name, song_name, song_year, sum(reproduccion) as reproducciones\
    from music_fact msF\
    inner join artist_dimension artD\
    on msF.id_artist = artD.id_artist\
    inner join song_dimension songD\
    on msF.id_song = songD.id_song\
    group by artist_name, song_name\
    order by reproducciones desc\
    ) aux\
    group by aux.song_year\
    order by aux.song_year;\
'

query7 = '\
    select artist_name, sum(popularity) popularity\
    from music_fact msf\
    inner join artist_dimension artd\
    on artd.id_artist = msf.id_artist\
    inner join song_dimension songd\
    on songd.id_song = msf.id_song\
    group by artist_name\
    order by popularity desc\
    limit 10;\
'

query8 = '\
    select song_name, popularity\
    from music_fact msf\
    inner join song_dimension songd\
    on songd.id_song = msf.id_song\
    order by popularity desc\
    limit 10;\
'

query9 = '\
    select genre, sum(popularity) popularity\
    from music_fact msf\
    inner join song_dimension songd\
    on songd.id_song = msf.id_song\
    group by genre\
    order by popularity desc\
    limit 5;\
'

query10 = '\
    select b.song_name, b.genre, reproducciones\
    from\
    (\
    select genre, max(reproduccion) reproducciones\
    from music_fact msf\
    inner join song_dimension songd\
    on songd.id_song = msf.id_song\
    where explicit = 1\
    group by genre\
    order by genre\
    ) a\
    inner join song_dimension b\
    inner join music_fact c\
    where c.id_song = b.id_song and b.genre = a.genre and c.reproduccion = a.reproducciones\
    group by genre\
    order by genre;\
'

def executeQuerys():
    try:
        logger.info("Abriendo el archivo para almacenar resultados...")
        fileResults = open('querys.txt', 'w+', encoding='utf-8')
        logger.info("Comenzando las consultas...")
        logger.info("Ejecutando consulta 1...")
        fileResults.write('################################################### CONSULTA 1 ###################################################\n')
        fileResults.write('Artista         Reproducciones\n')
        dataQuery = getQuerySelect(query1)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 1 almacenada con exito")
        logger.info("Ejecutando consulta 2...")
        fileResults.write('################################################### CONSULTA 2 ###################################################\n')
        fileResults.write('Artista                   Cancion                  Reproducciones\n')
        dataQuery = getQuerySelect(query2)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 2 almacenada con exito")
        logger.info("Ejecutando consulta 3...")
        fileResults.write('################################################### CONSULTA 3 ###################################################\n')
        fileResults.write('Genero                 Reproducciones\n')
        dataQuery = getQuerySelect(query3)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 3 almacenada con exito")
        logger.info("Ejecutando consulta 4...")
        fileResults.write('################################################### CONSULTA 4 ###################################################\n')
        fileResults.write('Artista                Genero                                  Reproducciones\n')
        dataQuery = getQuerySelect(query4)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 4 almacenada con exito")
        logger.info("Ejecutando consulta 5...")
        fileResults.write('################################################### CONSULTA 5 ###################################################\n')
        fileResults.write('Artista                Cancion                                                Genero                               Reproducciones\n')
        dataQuery = getQuerySelect(query5)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 5 almacenada con exito")
        logger.info("Ejecutando consulta 6...")
        fileResults.write('################################################### CONSULTA 6 ###################################################\n')
        fileResults.write('Artista                   Cancion                               Año   Reproducciones\n')
        dataQuery = getQuerySelect(query6)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 6 almacenada con exito")
        logger.info("Ejecutando consulta 7...")
        fileResults.write('################################################### CONSULTA 7 ###################################################\n')
        fileResults.write('Artista         Popularidad\n')
        dataQuery = getQuerySelect(query7)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 7 almacenada con exito")
        logger.info("Ejecutando consulta 8...")
        fileResults.write('################################################### CONSULTA 8 ###################################################\n')
        fileResults.write('Cancion               Popularidad\n')
        dataQuery = getQuerySelect(query8)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 8 almacenada con exito")
        logger.info("Ejecutando consulta 9...")
        fileResults.write('################################################### CONSULTA 9 ###################################################\n')
        fileResults.write('Genero                 Popularidad\n')
        dataQuery = getQuerySelect(query9)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 9 almacenada con exito")
        logger.info("Ejecutando consulta 10...")
        fileResults.write('################################################### CONSULTA 10 ###################################################\n')
        fileResults.write('Cancion                                      Genero                           Popularidad\n')
        dataQuery = getQuerySelect(query10)
        fileResults.write(tabulate(dataQuery))
        fileResults.write('\n##################################################################################################################\n')
        logger.info("Consulta 10 almacenada con exito")
        logger.info("Cerrando el archivo de resultados...")
        fileResults.close()
    except Exception as e:
        logger.error(e)
        print("Ocurrio un error")