from django.contrib import admin
from music.models import music

class music_admin(admin.ModelAdmin):
    list_display=['id','song_name','artist','duration','image','Audio_file','Audio_link']
admin.site.register(music,music_admin)
 