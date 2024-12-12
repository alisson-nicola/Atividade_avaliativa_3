# Atividade Avaliativa 3

Este repositório contém o código-fonte da aplicação desenvolvida para a "Atividade Avaliativa 3". A aplicação foi criada como parte de um projeto acadêmico e tem como objetivo atender aos requisitos especificados na atividade proposta.

## Funcionalidades

- Cadastro de funcionários
- Gerenciamento de informações dinâmicas
- Integração com templates responsivos em Bootstrap 5

## Estrutura do Projeto

O projeto segue a estrutura padrão de aplicações Django:

```
Atividade_avaliativa_3/
├── manage.py
├── app/              # App principal da aplicação
│   ├── migrations/   # Arquivos de migração
│   ├── templates/    # Templates HTML
│   ├── models.py     # Definição dos modelos de dados
│   ├── views.py      # Lógica de negócio
│   ├── urls.py       # Definição das rotas do app
│   └── forms.py      # Definição de formulários
└── funcionario/      # Sistema principal da aplicação
    ├── settings.py   # Configurações do sistema
    └── urls.py       # Definição das rotas do sistema
```

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação principal
- **Django 4.2**: Framework web para o backend
- **Bootstrap 5**: Framework CSS para estilização e responsividade
- **MySQL**: Sistema de gerenciamento de banco de dados

## Como Executar o Projeto

### Passos para executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/alisson-nicola/Atividade_avaliativa_3.git
   cd Atividade_avaliativa_3
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
    pip install -r requirements.txt
   ```

4. Crie o banco MySQL e conecte no sistema pelo arquivo Settings.py:

   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        'NAME': '',
    }
   }
   ```

5. Aplique as migrações ao banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor local:

   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação em seu navegador:

   ```
   http://127.0.0.1:8000/
   ```

## Autores

[Alisson Nicola](https://github.com/alisson-nicola) | [João Eduardo Panissa](https://github.com/) | [Vinícius Zorzi Martins da Silva](https://github.com/)