from django.contrib import admin

# Register your models here.
from .models import Users,Artists,Albums,Songs,Playlists,Playlist_songs

admin.site.register(Users)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Songs)
admin.site.register(Playlists)
admin.site.register(Playlist_songs)

