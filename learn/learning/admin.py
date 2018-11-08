from django.contrib import admin

from learning.models import Topic
from learning.models import Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
