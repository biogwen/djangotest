from django.db import models
from django.conf import settings


class formulairetest(models.Model):
    champ_texte = models.CharField(max_length=400)
    champ_email = models.EmailField(max_length=40)
    champ_decimal = models.DecimalField(max_digits=4, decimal_places=3)
    champ_date = models.DateField()
    champ_heure = models.TimeField()


    def save(self):

        self.save()

    def __str__(self):
        return self.champ_texte