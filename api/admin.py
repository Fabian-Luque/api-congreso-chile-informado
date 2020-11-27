from django.contrib import admin
from .models import Congressman, PoliticalParty, Commission
# Register your models here.

admin.site.register(Congressman)
admin.site.register(PoliticalParty)
admin.site.register(Commission)