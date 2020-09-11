from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	def __str__(self):
		return self.username

class Artists(models.Model):
	artist_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.artist_name


class Albums(models.Model):
	album_name = models.CharField(max_length = 200)
	artist_id = models.ForeignKey(Artists, models.CASCADE)
	def __str__(self):
		return self.album_name

class Songs(models.Model):
	song_name = models.CharField(max_length = 200)
	filename = models.CharField(max_length = 200)
	artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
	album_id = models.ForeignKey(Albums, on_delete=models.CASCADE)
	def __str__(self):
		return self.song_name

class Playlists(models.Model):
	playlist_name = models.CharField(max_length = 200)
	user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
	def __str__(self):
		return self.playlist_name


class Playlist_songs(models.Model):
	playlist_id = models.ForeignKey(Playlists, on_delete = models.CASCADE)
	song_id = models.ForeignKey(Songs, on_delete = models.CASCADE)
	# def __str__(self):
	# 	return self.playlist_id





