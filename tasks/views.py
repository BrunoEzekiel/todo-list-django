from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm, TaskFilterForm, CustomUserCreationForm

# Create your views here.

@login_required
def task_list(request):
    """
    View para listar todas as tarefas do usuário com filtros
    """
    tasks = Task.objects.filter(user=request.user)
    filter_form = TaskFilterForm(request.GET)
    
    # Aplicar filtros
    if filter_form.is_valid():
        status = filter_form.cleaned_data.get('status')
        priority = filter_form.cleaned_data.get('priority')
        search = filter_form.cleaned_data.get('search')
        
        if status == 'pending':
            tasks = tasks.filter(completed=False)
        elif status == 'completed':
            tasks = tasks.filter(completed=True)
        
        if priority:
            tasks = tasks.filter(priority=priority)
        
        if search:
            tasks = tasks.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search)
            )
    
    # Paginação
    paginator = Paginator(tasks, 10)  # 10 tarefas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estatísticas
    total_tasks = Task.objects.filter(user=request.user).count()
    completed_tasks = Task.objects.filter(user=request.user, completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    context = {
        'page_obj': page_obj,
        'filter_form': filter_form,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }
    
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
    """
    View para criar uma nova tarefa
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Nova Tarefa'
    })

@login_required
def task_edit(request, pk):
    """
    View para editar uma tarefa existente
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Editar Tarefa',
        'task': task
    })

@login_required
def task_delete(request, pk):
    """
    View para excluir uma tarefa
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle_complete(request, pk):
    """
    View AJAX para marcar/desmarcar tarefa como concluída
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'completed': task.completed,
            'message': 'Tarefa concluída!' if task.completed else 'Tarefa marcada como pendente!'
        })
    
    messages.success(request, 
        'Tarefa concluída!' if task.completed else 'Tarefa marcada como pendente!'
    )
    return redirect('task_list')

def register(request):
    """
    View para registro de novos usuários
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    """
    View da página inicial
    """
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request, 'tasks/home.html')
