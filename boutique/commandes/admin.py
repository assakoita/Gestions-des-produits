from django.contrib import admin
from .models import Commande

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_commande', 'termine')
    list_filter = ('termine', 'date_commande')
    filter_horizontal = ('produits',)

admin.site.register(Commande, CommandeAdmin)
