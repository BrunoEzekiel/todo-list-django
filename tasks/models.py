from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    """
    Modelo para representar uma tarefa no sistema To-Do List
    """
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descrição")
    completed = models.BooleanField(default=False, verbose_name="Concluída")
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='media',
        verbose_name="Prioridade"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Criada em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizada em")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de vencimento")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Usuário"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        """Verifica se a tarefa está atrasada"""
        if self.due_date and not self.completed:
            return timezone.now() > self.due_date
        return False
