from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Task
    """
    list_display = ['title', 'user', 'priority', 'completed', 'created_at', 'due_date']
    list_filter = ['completed', 'priority', 'created_at', 'user']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['completed', 'priority']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'user')
        }),
        ('Status e Prioridade', {
            'fields': ('completed', 'priority', 'due_date')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        """
        Otimiza as consultas incluindo o relacionamento com User
        """
        return super().get_queryset(request).select_related('user')
    
    def save_model(self, request, obj, form, change):
        """
        Automaticamente define o usuário se não estiver definido
        """
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
