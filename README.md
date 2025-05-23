# Projeto Django Simples

Este é um projeto básico em Django com um ambiente virtual Python (`venv`), estrutura padrão com diretório `project/` para configurações do Django e um app nomeado `aplicativo_django`.

## ✅ Requisitos

- Python 3.8 ou superior
- pip
- virtualenv (opcional, mas recomendado)

## 📁 Estrutura do Projeto

```
projeto_django/
├── venv/              # Ambiente virtual
├── manage.py
├── projeto_django/           # Configurações principais do Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── aplicativo_django/               # Aplicativo Django
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── tests.py
```
---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/meu_projeto.git
cd meu_projeto
```

### 2. Crie e ative o ambiente virtual

#### Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install django
```

Se tiver um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
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

Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠️ Comandos úteis do Django

| Ação | Comando |
|------|---------|
| Criar novo app | `python manage.py startapp nome_do_app` |
| Criar migrações | `python manage.py makemigrations` |
| Aplicar migrações | `python manage.py migrate` |
| Criar superusuário | `python manage.py createsuperuser` |
| Executar testes | `python manage.py test` |
| Acessar o shell | `python manage.py shell` |

---

## 🔐 Segurança

- **Nunca suba arquivos sensíveis como `.env` ou `db.sqlite3` em repositórios públicos.**
- Use variáveis de ambiente ou bibliotecas como `python-decouple` para proteger suas configurações.
