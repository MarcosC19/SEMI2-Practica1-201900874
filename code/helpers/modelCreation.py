from .loggerConfig import logger
from .database import executeQuery
from mysql.connector import Error

drop_tables = 'DROP TABLE IF EXISTS temporal;\
                DROP TABLE IF EXISTS music_fact;\
                DROP TABLE IF EXISTS artist_dimension;\
                DROP TABLE IF EXISTS song_dimension;'

create_model_tables = 'CREATE TABLE artist_dimension (\
                    id_artist INTEGER AUTO_INCREMENT,\
                    artist_name VARCHAR(250) NOT NULL,\
                    CONSTRAINT pk_artist_dimension PRIMARY KEY (id_artist)\
                );\
                CREATE TABLE song_dimension (\
                    id_song INTEGER AUTO_INCREMENT,\
                    song_name VARCHAR(250) NOT NULL,\
                    duration_ms INTEGER,\
                    explicit BOOLEAN,\
                    song_year INTEGER,\
                    popularity INTEGER,\
                    genre VARCHAR(250),\
                    CONSTRAINT pk_song_dimension PRIMARY KEY (id_song)\
                );\
                CREATE TABLE music_fact (\
                    id_artist INTEGER NOT NULL,\
                    id_song INTEGER NOT NULL,\
                    reproduccion INTEGER,\
                    danceability FLOAT,\
                    energy FLOAT,\
                    music_key INTEGER,\
                    loudness INTEGER,\
                    music_mode INTEGER,\
                    speechiness FLOAT,\
                    acousticness FLOAT,\
                    instrumentalness FLOAT,\
                    liveness FLOAT,\
                    valence FLOAT,\
                    tempo FLOAT,\
                    CONSTRAINT fk_id_artist FOREIGN KEY (id_artist)\
                        REFERENCES artist_dimension (id_artist),\
                    CONSTRAINT fk_id_song FOREIGN KEY (id_song)\
                        REFERENCES song_dimension (id_song)\
                );'

create_temporal_table = 'CREATE TABLE temporal (\
                    artist VARCHAR(250),\
                    song VARCHAR(250),\
                    duration_ms INTEGER,\
                    explicit BOOLEAN,\
                    song_year INTEGER,\
                    popularity INTEGER,\
                    danceability FLOAT,\
                    energy FLOAT,\
                    music_key INTEGER,\
                    loudness INTEGER,\
                    music_mode INTEGER,\
                    speechiness FLOAT,\
                    acousticness FLOAT,\
                    instrumentalness FLOAT,\
                    liveness FLOAT,\
                    valence FLOAT,\
                    tempo FLOAT,\
                    genre VARCHAR(250)\
                );'

# METHOD MAIN TO CREATE MODEL TO DW
def createModel():
    try:
        # CREATION OF DATABASE MODEL
        logger.info("Comenzando la creacion del modelo...")
        logger.info("Eliminando tablas existentes del modelo...")
        executeQuery(drop_tables)
        logger.info("Tablas eliminadas con exito")
        logger.info("Creando tabla temporal para los datos...")
        executeQuery(create_temporal_table)
        logger.info("Tabla temporal creada con exito")
        logger.info("Creando las tablas del modelo...")
        executeQuery(create_model_tables)
        logger.info("Tablas del modelo creadas con exito")
    except Error as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)


