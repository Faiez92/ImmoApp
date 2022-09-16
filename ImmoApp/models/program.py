from django.db import models


class Program(models.Model):
    prog = (
        ('prog 001', 'prog 001'),
        ('prog 002', 'prog 002'),
        ('prog 003', 'prog 003'),
    )
    prog_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, choices=prog, default='green')
    dispo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
