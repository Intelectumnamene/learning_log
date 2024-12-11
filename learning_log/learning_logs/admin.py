from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')  # Exibe esses campos na lista de tópicos
    search_fields = ['text']  # Adiciona barra de pesquisa para campo "text"

class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added')
    search_fields = ['text', 'topic__text']
    
admin.site.register(Topic)
admin.site.register(Entry)
