from django.contrib import admin
from.models import student,address,Skills,candidate,parent,child1,child2
# Register your models here.
admin.site.register([student,address])
admin.site.register([Skills,candidate])
admin.site.register([child1,child2])