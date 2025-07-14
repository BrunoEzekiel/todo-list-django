# 🌟 To-Do List Django

![Django](https://img.shields.io/badge/Django-5.1.5-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)

Um sistema completo de gerenciamento de tarefas desenvolvido com Django, apresentando uma interface moderna com tema verde neon e funcionalidades avançadas de CRUD, autenticação e filtros.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Capturas de Tela](#capturas-de-tela)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autor](#autor)

## 🎯 Sobre o Projeto

Este projeto é um sistema de gerenciamento de tarefas (To-Do List) desenvolvido com Django que oferece uma experiência completa de organização pessoal. Com um design moderno em tema escuro e verde neon, o sistema permite aos usuários criar, gerenciar e acompanhar suas tarefas de forma eficiente.

### ✨ Destaques

- 🎨 **Interface Moderna**: Design responsivo com tema verde neon
- 🔐 **Sistema de Autenticação**: Registro e login seguros
- 📊 **Dashboard Analítico**: Estatísticas em tempo real
- 🔍 **Busca Avançada**: Filtros por status, prioridade e texto
- 📱 **Responsivo**: Funciona perfeitamente em dispositivos móveis
- ⚡ **Performance**: Otimizado com paginação e queries eficientes

## 🚀 Funcionalidades

### ✅ Gestão de Tarefas
- **Criar** tarefas com título, descrição, prioridade e data de vencimento
- **Listar** tarefas com layout em cards responsivo
- **Editar** tarefas existentes com formulários intuitivos
- **Excluir** tarefas com confirmação de segurança
- **Marcar** como concluída/pendente com um clique (AJAX)
- **Prioridades**: Alta (vermelha), Média (amarela), Baixa (verde)
- **Status**: Pendente, Concluída, Atrasada (com indicadores visuais)

### 👤 Sistema de Usuários
- **Registro** de novos usuários com validação
- **Login/Logout** com redirecionamento inteligente
- **Isolamento** de dados por usuário
- **Perfil** personalizado no navbar

### 🔍 Filtros e Busca
- **Filtro por Status**: Todas, Pendentes, Concluídas
- **Filtro por Prioridade**: Todas, Alta, Média, Baixa
- **Busca Textual**: Pesquisa no título e descrição
- **Combinação**: Múltiplos filtros simultâneos
- **URL Persistente**: Filtros mantidos na navegação

### 📊 Dashboard e Analytics
- **Contadores**: Total, Pendentes, Concluídas
- **Cards Estatísticos**: Visuais coloridos por categoria
- **Indicadores**: Tarefas atrasadas destacadas
- **Progresso Visual**: Acompanhamento do desempenho

### 🎨 Interface e UX
- **Tema Escuro**: Fundo preto com acentos verde neon
- **Efeitos Visuais**: Animações de hover e brilho neon
- **Responsividade**: Bootstrap 5 com layout adaptativo
- **Ícones**: Font Awesome para elementos visuais
- **Feedback**: Mensagens de sucesso/erro em tempo real

## 🛠️ Tecnologias

### Backend
- **Django 5.1.5** - Framework web Python
- **Python 3.8+** - Linguagem de programação
- **SQLite** - Banco de dados (desenvolvimento)

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização com variáveis CSS
- **JavaScript** - Interações e AJAX
- **Bootstrap 5.1.3** - Framework CSS responsivo
- **Font Awesome 6.0** - Biblioteca de ícones
- **jQuery 3.6** - Manipulação DOM e AJAX

### Ferramentas
- **Git** - Controle de versão
- **pip** - Gerenciador de pacotes Python
- **Virtualenv** - Ambiente virtual Python

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone git@github.com:BrunoEzekiel/todo-list-django.git
cd todo-list-django
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

6. **Inicie o servidor**
```bash
python manage.py runserver
```

7. **Acesse a aplicação**
- Interface principal: http://127.0.0.1:8000/
- Admin Django: http://127.0.0.1:8000/admin/

## 📖 Como Usar

### Primeiro Acesso
1. Acesse http://127.0.0.1:8000/
2. Clique em "Registrar" para criar uma conta
3. Faça login com suas credenciais
4. Comece a criar suas tarefas!

### Gerenciando Tarefas

#### Criar Nova Tarefa
1. Clique em "Nova Tarefa" no navbar ou botão principal
2. Preencha os campos:
   - **Título**: Nome da tarefa (obrigatório)
   - **Descrição**: Detalhes da tarefa (opcional)
   - **Prioridade**: Baixa, Média ou Alta
   - **Data de Vencimento**: Data e hora limite (opcional)
3. Clique em "Salvar Tarefa"

#### Visualizar e Filtrar
- **Dashboard**: Veja estatísticas na página principal
- **Filtros**: Use os seletores para filtrar por status/prioridade
- **Busca**: Digite termos na caixa de pesquisa
- **Paginação**: Navegue pelas páginas se houver muitas tarefas

#### Ações nas Tarefas
- **✅ Concluir**: Clique no botão verde para marcar como concluída
- **✏️ Editar**: Clique no botão azul para editar
- **🗑️ Excluir**: Clique no botão vermelho para excluir
- **↩️ Reverter**: Desfaça a conclusão clicando no botão laranja

## 📁 Estrutura do Projeto

```
todo-list-django/
│
├── 📄 manage.py                    # Script principal do Django
├── 📄 requirements.txt             # Dependências do projeto
├── 📄 README.md                   # Documentação
├── 📄 .gitignore                  # Arquivos ignorados pelo Git
│
├── 📁 todo_project/               # Configurações do projeto
│   ├── 📄 __init__.py
│   ├── 📄 settings.py             # Configurações Django
│   ├── 📄 urls.py                 # URLs principais
│   └── 📄 wsgi.py                 # Configuração WSGI
│
└── 📁 tasks/                      # Aplicação principal
    ├── 📄 __init__.py
    ├── 📄 admin.py                # Configuração do admin
    ├── 📄 apps.py                 # Configuração da app
    ├── 📄 models.py               # Modelos de dados
    ├── 📄 views.py                # Lógica das views
    ├── 📄 forms.py                # Formulários
    ├── 📄 urls.py                 # URLs da aplicação
    ├── 📄 tests.py                # Testes unitários
    │
    ├── 📁 migrations/             # Migrações do banco
    │   └── 📄 0001_initial.py
    │
    ├── 📁 templates/              # Templates HTML
    │   ├── 📁 tasks/
    │   │   ├── 📄 base.html       # Template base
    │   │   ├── 📄 home.html       # Página inicial
    │   │   ├── 📄 task_list.html  # Lista de tarefas
    │   │   ├── 📄 task_form.html  # Formulário de tarefa
    │   │   └── 📄 task_confirm_delete.html
    │   └── 📁 registration/
    │       ├── 📄 login.html      # Página de login
    │       └── 📄 register.html   # Página de registro
    │
    └── 📁 static/                 # Arquivos estáticos
        └── 📁 tasks/
            └── 📄 style.css       # CSS customizado
```

## 🎨 Capturas de Tela

### 🏠 Página Inicial
- Design moderno com tema verde neon
- Apresentação das funcionalidades
- Botões de call-to-action

### 📋 Lista de Tarefas
- Cards responsivos com informações completas
- Filtros e busca no topo
- Estatísticas em tempo real
- Ações rápidas para cada tarefa

### ✏️ Formulários
- Interface limpa e intuitiva
- Validação em tempo real
- Campos organizados logicamente

### 👤 Autenticação
- Páginas de login e registro
- Design consistente com o tema
- Validação de dados

## 🔧 Configurações Avançadas

### Personalizações CSS
O projeto utiliza variáveis CSS para fácil customização:

```css
:root {
    --green-neon: #00ff41;
    --green-light: #39ff6b;
    --green-dark: #00cc33;
    --black-bg: #0a0a0a;
    --black-card: #1a1a1a;
}
```

### Configurações Django
- **Localização**: Português do Brasil (pt-br)
- **Timezone**: America/Sao_Paulo
- **Debug**: True (desenvolvimento)
- **Database**: SQLite (pode ser alterado para PostgreSQL/MySQL)

## 🧪 Testes

Para executar os testes:

```bash
python manage.py test
```

## 📈 Melhorias Futuras

### Planejadas
- [ ] **API REST** com Django REST Framework
- [ ] **Notificações** por email para tarefas vencidas
- [ ] **Categorias/Tags** para organização
- [ ] **Compartilhamento** de tarefas entre usuários
- [ ] **Anexos** em tarefas
- [ ] **Tema claro/escuro** alternável

### Ideias
- [ ] **Dashboard avançado** com gráficos
- [ ] **Exportação** de dados (PDF, Excel)
- [ ] **App mobile** com React Native
- [ ] **Integração** com calendários
- [ ] **Colaboração** em tempo real

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### Diretrizes de Contribuição
- Siga as convenções de código Python (PEP 8)
- Escreva testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use commits descritivos e organizados

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades  
- Enviar pull requests
- Melhorar a documentação

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 👨‍💻 Autor

**Bruno Ezekiel**
- GitHub: [@BrunoEzekiel](https://github.com/BrunoEzekiel)
- LinkedIn: [Bruno Ezekiel](https://linkedin.com/in/bruno-ezekiel)

---

<div align="center">

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Feito com ❤️ e muito ☕ por Bruno Ezekiel**

</div>
