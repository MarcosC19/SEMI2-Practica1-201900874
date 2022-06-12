-- CONSULTA 1

SELECT artist_name, sum(reproduccion) as reproducciones
from music_fact msF
inner join artist_dimension artD
on msF.id_artist = artD.id_artist
group by artist_name
order by reproducciones desc
limit 10;

-- CONSULTA 2

SELECT artist_name, song_name, sum(reproduccion) as reproducciones
from music_fact msF
inner join artist_dimension artD
on msF.id_artist = artD.id_artist
inner join song_dimension songD
on msF.id_song = songD.id_song
group by artist_name, song_name
order by reproducciones desc
limit 10;

-- CONSULTA 3

SELECT genre, sum(reproduccion) as reproducciones
from music_fact msF
inner join song_dimension songD
on msF.id_song = songD.id_song
group by genre
order by reproducciones desc
limit 5;

-- CONSULTA 4

select aux.artist_name artist_name, aux.genre genre, max(aux.reproducciones) as reproducciones
from
(
SELECT artist_name, genre, sum(reproduccion) as reproducciones
from music_fact msF
inner join artist_dimension artD
on msF.id_artist = artD.id_artist
inner join song_dimension songD
on msF.id_song = songD.id_song
group by artist_name, genre
order by reproducciones desc
) aux
group by genre
order by genre;

-- CONSULTA 5

select aux.artist_name, aux.song_name song_name, aux.genre genre, max(aux.reproducciones) as reproducciones
from
(
SELECT artist_name, song_name, genre, sum(reproduccion) as reproducciones
from music_fact msF
inner join artist_dimension artD
on msF.id_artist = artD.id_artist
inner join song_dimension songD
on msF.id_song = songD.id_song
group by artist_name,song_name, genre
order by reproducciones desc
) aux
group by genre
order by genre;

-- CONSULTA 6

select aux.artist_name, aux.song_name, aux.song_year, max(aux.reproducciones) reproducciones
from
(
SELECT artist_name, song_name, song_year, sum(reproduccion) as reproducciones
from music_fact msF
inner join artist_dimension artD
on msF.id_artist = artD.id_artist
inner join song_dimension songD
on msF.id_song = songD.id_song
group by artist_name, song_name
order by reproducciones desc
) aux
group by aux.song_year
order by aux.song_year;

-- CONSULTA 7

select artist_name, sum(popularity) popularity
from music_fact msf
inner join artist_dimension artd
on artd.id_artist = msf.id_artist
inner join song_dimension songd
on songd.id_song = msf.id_song
group by artist_name
order by popularity desc
limit 10;

-- CONSULTA 8

select song_name, popularity
from music_fact msf
inner join song_dimension songd
on songd.id_song = msf.id_song
order by popularity desc
limit 10;

-- CONSULTA 9

select genre, sum(popularity) popularity
from music_fact msf
inner join song_dimension songd
on songd.id_song = msf.id_song
group by genre
order by popularity desc
limit 5;


-- CONSULTA 10

select b.song_name, b.genre, reproducciones
from
(
select genre, max(reproduccion) reproducciones
from music_fact msf
inner join song_dimension songd
on songd.id_song = msf.id_song
where explicit = 1
group by genre
order by genre
) a
inner join song_dimension b
inner join music_fact c
where c.id_song = b.id_song and b.genre = a.genre and c.reproduccion = a.reproducciones
group by genre
order by genre;
