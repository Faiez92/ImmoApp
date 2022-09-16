from django.db import models
from multiselectfield import MultiSelectField

from ImmoApp.models.program import Program


class Appartement(models.Model):

    Liste_caracteristique = (
        ('piscine','piscine'),
        ('jardin', 'jardin'),
        ('cave', 'cave'),
        ('parking', 'jardin'),
        ('proche station ski', 'proche station ski'),

    )
    app_id = models.AutoField(primary_key=True)
    surface = models.FloatField()
    prix = models.FloatField()
    nbre_piece = models.IntegerField()
    caract = MultiSelectField(choices=Liste_caracteristique,
                                 max_length=20,
                                 default=None,
                                 null=True,
                                 blank=True
                                 )

    prog = models.ForeignKey(Program, on_delete=models.CASCADE, default= 1)

    def near_to(self):
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee','proche station ski' in self.caract)
        return 'proche station ski' in self.caract