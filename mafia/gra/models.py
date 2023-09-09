from django.db import models

class Gra(models.Model):
  status = models.BooleanField(default= True)

  def __str__(self):
    return f"Gra - {self.id}"
  
class Rola(models.Model):
  class Rodzaje(models.IntegerChoices):
      MIASTO = 1
      MAFIA = 2

  nazwa = models.CharField(max_length=20)
  rodzaj = models.IntegerField(choices = Rodzaje.choices)
  priorytet = models.IntegerField()

  def __str__(self):
    return f"{self.nazwa}"
  
class Gracz(models.Model):
  nazwa = models.CharField(max_length=50)
  numer = models.IntegerField()
  glosy = models.IntegerField()
  idRola = models.ForeignKey('Rola', on_delete=models.CASCADE)
  idGra = models.ForeignKey('Gra', on_delete=models.CASCADE)
  

  def __str__(self):
    return f"{self.nazwa} - {self.idRola}"