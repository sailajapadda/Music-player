from django.db import models


class music(models.Model):
    song_name=models.TextField()
    artist=models.TextField()
    duration=models.FloatField()
    image=models.ImageField(upload_to='staic/image')
    Audio_file=models.FileField(blank=True,null=True)
    Audio_link=models.FileField(max_length=200,blank=True)
    paginate_by=2
    def __str__(self):
        return self.song_name