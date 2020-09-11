from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page,name="login_page"),
    path('admin_page',views.admin_page,name="admin_page"),
    path('add_song',views.add_song,name="add_song"),
    path('add_artist',views.add_artist,name="add_artist"),
    path('add_album',views.add_album,name="add_album"),
    path('display_table',views.display_table,name="display_table"),    
    path('user_page',views.user_page,name="user_page"),
    path('add_song_to_playlist',views.add_song_to_playlist, name="add_song_to_playlist"),
    path('create_playlist',views.create_playlist,name="create_playlist"),
    path('show_playlist',views.show_playlist,name="show_playlist"),
    
]