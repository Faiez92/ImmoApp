from rest_framework import routers

from ImmoApp.viewsets import AppartementViewset

router = routers.DefaultRouter()
router.register('Appartements', AppartementViewset)
router.register('Apparts', AppartementViewset)