from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'created_by', 'created_at', 'updated_at')
    search_fields = ('client_name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'get_users', 'created_at']  
    filter_horizontal = ['users']  
    
    def get_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Users'  

admin.site.register(Project, ProjectAdmin)
