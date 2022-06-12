use semi2_practica1;

-- INSERTS INTO ARTIST_DIMENSION TABLE
insert into artist_dimension(artist_name)
select distinct artist from temporal
order by artist;

SELECT 
    *
FROM
    artist_dimension;

-- INSERTS INTO SONG_DIMENSION TABLE
insert into song_dimension(song_name, duration_ms, explicit, song_year, popularity, genre)
select t_aux.song, t_aux.duration_ms, t_aux.explicit, t_aux.song_year, t_aux.popularity, t_aux.genre
from
(
select distinct artist, upper(song) as song, cast(avg(duration_ms) as signed) as duration_ms, explicit, song_year, cast(avg(popularity) as signed) as popularity, genre from temporal
group by artist, song
order by song
) as t_aux;

SELECT 
    *
FROM
    song_dimension;

-- INSERTS INTO MUSIC_FACT TABLE
insert into music_fact(id_artist, id_song, reproduccion, danceability, energy, music_key, loudness,
music_mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo)
select artD.id_artist, songD.id_song, auxiliar.reproduccion, auxiliar.danceability, auxiliar.energy, auxiliar.music_key, auxiliar.loudness,
auxiliar.music_mode, auxiliar.speechiness, auxiliar.acousticness, auxiliar.instrumentalness, auxiliar.liveness, auxiliar.valence, auxiliar.tempo
from
(
select artist, upper(song) as song, count(song) as reproduccion,danceability, energy, music_key, loudness, music_mode, speechiness,
acousticness, instrumentalness, liveness, valence, tempo, song_year, genre
from temporal
group by artist, song
) as auxiliar
inner join artist_dimension as artD
on artD.artist_name = auxiliar.artist
inner join song_dimension as songD
on songD.song_name = auxiliar.song and songD.song_year = auxiliar.song_year and songD.genre = auxiliar.genre;

SELECT 
    *
FROM
    music_fact;
