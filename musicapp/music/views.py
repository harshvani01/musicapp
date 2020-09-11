from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponse
from .models import Users,Artists,Albums,Songs,Playlists,Playlist_songs

# Create your views here.
def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		p = Users.objects.filter(username=username , password = password)

		if p:
			if(username == "admin"):
				return redirect('admin_page')
			else:
				request.session['username']=username
				return redirect('user_page')
		else:
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def admin_page(request):
	return render(request,'admin_page.html')

def add_song(request):
	artist_data = Artists.objects.all()
	album_data = Albums.objects.all()
	context = {"artist_data":artist_data,
		"album_data":album_data
		}


	if request.method == "POST":
		song_name = request.POST.get('song_name')
		filename = request.POST.get('filename')
		artist_id = request.POST.get('artist_id')
		album_id = request.POST.get('album_id')
		artist = Artists.objects.get(id = artist_id)
		album = Albums.objects.get(id = album_id)
		song = Songs(song_name=song_name,filename=filename,artist_id=artist,album_id=album)
		song.save()

		return render(request,'add_song.html',context)
	else:
		
		return render(request,'add_song.html',context)


def add_artist(request):
	if request.method == "POST":
		artist_name = request.POST.get('artist_name')
		artist = Artists(artist_name = artist_name)
		artist.save()
	else:
		return render(request,'add_artist.html')

def add_album(request):
	artist_data = Artists.objects.all()
	context = {"artist_data":artist_data}

	if request.method == "POST":
		album_name = request.POST.get('album_name')
		artist_id = request.POST.get('artist_id')
		artist = Artists.objects.get(id = artist_id)
		album = Albums(album_name=album_name,artist_id = artist)
		album.save()

		return render(request,'add_album.html',context)
	else:
		
		return render(request,'add_album.html',context)

def display_table(request):
	if request.method == "POST":
		table_name = request.POST.get('table_name')
		if(table_name == "Artists"):
			context = {"query_result":Artists.objects.all()}
			

		elif(table_name == "Albums"):
			context = {"query_result":Albums.objects.all()}

		elif(table_name == "Songs"):
			context = {"query_result":Songs.objects.all()}

		return render(request,'display_table.html',context)

	else:
		return render(request,'display_table.html')

def user_page(request):
	context = {"username":request.session['username']}
	return render(request,'user_page.html',context)
 
def add_song_to_playlist(request):
	user_id = Users.objects.get(username=request.session['username'])
	playlist_data = Playlists.objects.filter(user_id=user_id)
	song_data = Songs.objects.all()
	context = {"playlist_data":playlist_data,
	"song_data":song_data,
	"username":request.session['username']}
	if request.method == "POST":
		playlist_id = request.POST.get('playlist_id')
		song_id = request.POST.get('song_id')
		playlist = Playlists.objects.get(id = playlist_id)
		song = Songs.objects.get(id = song_id)
		o = Playlist_songs(playlist_id = playlist,song_id = song)
		o.save()
		return render(request,'add_song_to_playlist.html',context)
	else:
		return render(request,'add_song_to_playlist.html',context)

def create_playlist(request):
	user_id = Users.objects.get(username=request.session['username'])
	context = {"username":request.session['username']}
	if request.method == "POST":
		playlist_name = request.POST.get('playlist_name')
		playlist = Playlists(playlist_name=playlist_name,user_id=user_id)
		playlist.save()
		return render(request,'create_playlist.html',context)
	else:
		return render(request,'create_playlist.html',context)

def show_playlist(request):
	user_id = Users.objects.get(username=request.session['username'])
	user_playlist_data = Playlists.objects.filter(user_id=user_id)
	context = {"user_playlist_data":user_playlist_data,
	"username":request.session['username']}

	if request.method == "POST":
		playlist_id = request.POST.get('playlist_id')
		song_ids = Playlist_songs.objects.filter(playlist_id=playlist_id)
		context["songs"]=song_ids
		# song_names = []
		# for song in song_ids:
		# 	song_names +=  song.song_id
		# context["songs"]=song_names
		return render(request,'show_playlist.html',context)
	else:
		return render(request,'show_playlist.html',context)
