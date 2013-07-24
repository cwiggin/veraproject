from django.contrib import admin
from .models import Shows

class ShowsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Shows, ShowsAdmin)




