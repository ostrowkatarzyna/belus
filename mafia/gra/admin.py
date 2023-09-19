from django.contrib import admin
from .models import Gra, Rola, Gracz, Ruch, Runda
# Register your models here.
admin.site.register(Gra)
admin.site.register(Rola)
admin.site.register(Gracz)
admin.site.register(Ruch)
admin.site.register(Runda)