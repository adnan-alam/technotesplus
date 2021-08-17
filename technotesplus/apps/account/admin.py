from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


models_list = [User]


admin.site.register(*models_list)
