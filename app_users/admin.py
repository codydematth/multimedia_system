from django.contrib import admin
from app_users.models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)

admin.site.site_title = "Fountain International School"
admin.site.site_header = "Fountain International School Administration"
admin.site.site_url = "Fountain International School"
admin.site.index_title = "Fountain International School"
