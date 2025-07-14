# Sistema de Tarefas (To-Do List) - Django

Um sistema completo de gerenciamento de tarefas desenvolvido com Django, incluindo autenticação de usuários, CRUD completo e interface responsiva.

## 🚀 Funcionalidades

### ✅ Gestão de Tarefas
- **Criar tarefas** com título, descrição, prioridade e data de vencimento
- **Listar tarefas** com filtros por status e prioridade
- **Editar tarefas** existentes
- **Excluir tarefas** com confirmação
- **Marcar como concluída/pendente** com um clique
- **Buscar tarefas** por título ou descrição

### 👤 Sistema de Usuários
- **Registro** de novos usuários
- **Login/Logout** com autenticação segura
- **Tarefas individuais** por usuário
- **Perfil personalizado** para cada usuário

### 📊 Estatísticas e Filtros
- **Dashboard** com estatísticas das tarefas
- **Contadores** de tarefas totais, pendentes e concluídas
- **Filtros avançados** por status, prioridade e busca textual
- **Paginação** para grandes listas de tarefas

### 🎨 Interface
- **Design responsivo** com Bootstrap 5
- **Ícones** Font Awesome
- **Cores indicativas** para prioridades
- **Alertas visuais** para tarefas atrasadas
- **AJAX** para ações rápidas

## 🛠️ Tecnologias Utilizadas

- **Django 5.1.5** - Framework web
- **SQLite** - Banco de dados (padrão)
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Ícones
- **jQuery** - Interações JavaScript

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Configuração

### 1. Clone o repositório ou acesse a pasta do projeto

```bash
cd agenda-flask
```

### 2. Ative o ambiente virtual (se não estiver ativo)

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

### 7. Acesse o sistema

- **Aplicação principal**: http://127.0.0.1:8000/
- **Admin Django**: http://127.0.0.1:8000/admin/

## 📖 Como Usar

### Primeiro Acesso
1. Acesse http://127.0.0.1:8000/
2. Clique em "Registrar" para criar uma conta
3. Faça login com suas credenciais
4. Comece a criar suas tarefas!

### Criando Tarefas
1. Na página principal, clique em "Nova Tarefa"
2. Preencha os campos:
   - **Título**: Nome da tarefa (obrigatório)
   - **Descrição**: Detalhes da tarefa (opcional)
   - **Prioridade**: Baixa, Média ou Alta
   - **Data de Vencimento**: Data e hora limite (opcional)
3. Clique em "Salvar Tarefa"

### Gerenciando Tarefas
- **Marcar como concluída**: Clique no ícone ✓ verde
- **Editar**: Clique no ícone ✏️ azul
- **Excluir**: Clique no ícone 🗑️ vermelho
- **Filtrar**: Use os filtros na parte superior da lista
- **Buscar**: Digite termos na caixa de pesquisa

## 🗂️ Estrutura do Projeto

```
agenda-flask/
├── manage.py
├── requirements.txt
├── README.md
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        ├── tasks/
        │   ├── base.html
        │   ├── home.html
        │   ├── task_list.html
        │   ├── task_form.html
        │   └── task_confirm_delete.html
        └── registration/
            ├── login.html
            └── register.html
```

## 📱 Funcionalidades Detalhadas

### Models (Modelos)
- **Task**: Modelo principal com campos para título, descrição, prioridade, status, datas e usuário
- **User**: Modelo de usuário do Django (built-in)

### Views (Visualizações)
- **task_list**: Lista tarefas com filtros e paginação
- **task_create**: Cria nova tarefa
- **task_edit**: Edita tarefa existente
- **task_delete**: Exclui tarefa com confirmação
- **task_toggle_complete**: Marca/desmarca como concluída (AJAX)
- **register**: Registro de usuários
- **home**: Página inicial

### Forms (Formulários)
- **TaskForm**: Formulário para criar/editar tarefas
- **TaskFilterForm**: Formulário para filtros de busca
- **CustomUserCreationForm**: Formulário personalizado de registro

### Templates
- **base.html**: Template base com navegação e estilos
- **home.html**: Página inicial com informações
- **task_list.html**: Lista de tarefas com filtros
- **task_form.html**: Formulário de criação/edição
- **task_confirm_delete.html**: Confirmação de exclusão
- **login.html**: Página de login
- **register.html**: Página de registro

## 🎯 Conceitos Django Implementados

### ✅ Models
- Definição de modelos com relacionamentos
- Meta classes para ordenação e verbose names
- Properties e métodos customizados
- Relacionamento ForeignKey com User

### ✅ Views
- Function-based views
- Decoradores (@login_required)
- Tratamento de formulários (GET/POST)
- Filtros e busca com Q objects
- Paginação
- Mensagens de feedback
- Responses AJAX (JsonResponse)

### ✅ Templates
- Template inheritance (extends)
- Template tags e filtros
- Formulários com Bootstrap
- Conditional rendering
- Loops e iteração
- CSRF protection

### ✅ Forms
- ModelForm para CRUD
- Form simples para filtros
- Widgets customizados
- Validação de dados
- Form customizado herdando UserCreationForm

### ✅ URLs
- URL patterns
- URL namespacing
- Include de URLs de app
- Parâmetros em URLs (pk)

### ✅ Admin
- Registro de modelos
- Customização da interface admin
- List display e filtros
- Search fields
- Fieldsets organizados
- Campos readonly

### ✅ Autenticação
- Sistema de login/logout built-in
- Registro de usuários
- Proteção de views (@login_required)
- Redirecionamentos após login
- Usuários por sessão

## 🔒 Segurança

- **CSRF Protection**: Todos os formulários protegidos
- **Autenticação**: Acesso restrito às tarefas do usuário
- **Autorização**: Usuários só acessam suas próprias tarefas
- **Validação**: Validação server-side em todos os formulários

## 📈 Melhorias Futuras

- [ ] API REST com Django REST Framework
- [ ] Notificações por email para tarefas vencidas
- [ ] Categorias/Tags para tarefas
- [ ] Compartilhamento de tarefas entre usuários
- [ ] Dashboard com gráficos
- [ ] Exportação de tarefas (PDF, Excel)
- [ ] Tema escuro/claro
- [ ] PWA (Progressive Web App)

## 🐛 Resolução de Problemas

### Erro de Migração
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erro de Dependências
```bash
pip install -r requirements.txt
```

### Erro de Porta Ocupada
```bash
python manage.py runserver 8080
```

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades  
- Enviar pull requests
- Melhorar a documentação
