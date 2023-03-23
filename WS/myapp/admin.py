from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Workers)
admin.site.register(Order)
admin.site.register(WorkerJobTitle)
admin.site.register(Change)


#пароль = Петя: petya321
#пароль = Антон: anton123
#пароль = Иван: ivan1234