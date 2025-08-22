from django.db import models

# Create your models here.
class Characters(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name
    
class diagram(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    luke=models.FloatField()
    jamie=models.FloatField()
    manon=models.FloatField()
    kimberly=models.FloatField()
    marisa=models.FloatField()
    lily=models.FloatField()
    jp=models.FloatField()
    juri=models.FloatField()
    deejay=models.FloatField()
    cammy=models.FloatField()
    ryu=models.FloatField()
    ehonda=models.FloatField()
    blanka=models.FloatField()
    guile=models.FloatField()
    ken=models.FloatField()
    chunli=models.FloatField()
    zangief=models.FloatField()
    dhalsim=models.FloatField()
    rashid=models.FloatField()
    aki=models.FloatField()
    ed=models.FloatField()
    akuma=models.FloatField()
    mbison=models.FloatField()
    terry=models.FloatField()
    mai=models.FloatField()
    elena=models.FloatField()
    
    def __str__(self):
        return self.name