from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=20)
    image = models.URLField()
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)


class Albom(models.Model):
    title = models.CharField(max_length=20)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.URLField()
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)





class Songs(models.Model):
    title = models.CharField(max_length=30)
    cover = models.URLField(null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    listened = models.PositiveBigIntegerField(default=0)
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]



class Country(models.Model):
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    albom = models.ForeignKey(Songs, on_delete=models.CASCADE, null=True)
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)