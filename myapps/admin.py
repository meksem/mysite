from django.contrib import admin
from .models import Devis,DevisDemande
admin.site.site_header = 'My GOTICDZ'
admin.site.register(Devis)
admin.site.register(DevisDemande)

