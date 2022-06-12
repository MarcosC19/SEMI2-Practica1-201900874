CREATE DATABASE semi2_practica1;

use semi2_practica1;

-- MODEL CREATION
CREATE TABLE artist_dimension (
    id_artist INTEGER AUTO_INCREMENT,
    artist_name VARCHAR(250) NOT NULL,
    CONSTRAINT pk_artist_dimension PRIMARY KEY (id_artist)
);

CREATE TABLE song_dimension (
    id_song INTEGER AUTO_INCREMENT,
    song_name VARCHAR(250) NOT NULL,
    duration_ms INTEGER,
    explicit BOOLEAN,
    song_year INTEGER,
    popularity INTEGER,
    genre VARCHAR(250),
    CONSTRAINT pk_song_dimension PRIMARY KEY (id_song)
);

CREATE TABLE music_fact (
    id_artist INTEGER NOT NULL,
    id_song INTEGER NOT NULL,
    danceability FLOAT,
    energy FLOAT,
    music_key INTEGER,
    loudness INTEGER,
    music_mode INTEGER,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    CONSTRAINT fk_id_artist FOREIGN KEY (id_artist)
        REFERENCES artist_dimension (id_artist),
    CONSTRAINT fk_id_song FOREIGN KEY (id_song)
        REFERENCES song_dimension (id_song)
);

CREATE TABLE temporal (
    artist VARCHAR(250),
    song VARCHAR(250),
    duration_ms INTEGER,
    explicit BOOLEAN,
    song_year INTEGER,
    popularity INTEGER,
    danceability FLOAT,
    energy FLOAT,
    music_key INTEGER,
    loudness INTEGER,
    music_mode INTEGER,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    genre VARCHAR(250)
);

-- MODEL ELIMINATION
DROP table if exists temporal;
drop table music_fact;
drop table artist_dimension;
drop table song_dimension;
