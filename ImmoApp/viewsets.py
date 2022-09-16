from django.template import loader
from rest_framework import viewsets
from . import serializers
from .models.models import Appartement
from .models.program import Program
from django.http import HttpResponse


class AppartementViewset(viewsets.ModelViewSet):
    queryset = Appartement.objects.all()
    serializer_class = serializers.AppartementSerializer

    def get_data(self):
        p = Program.objects.filter(dispo=True).values()
        id_list = []
        print('+++++++++++++++')
        print(p)
        for i in p:
            id_list.append(i['prog_id'])
        print('**********************')
        print(Appartement.objects.filter(prog__in=id_list).values())
        mydata = Appartement.objects.filter(prog__in=id_list).values()
        template = loader.get_template('template.html')
        context = {
            'mymembers': mydata,
        }
        return HttpResponse(template.render(context))
