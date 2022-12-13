<p align="center">
  <img src="https://res.cloudinary.com/dnqiosdb6/image/upload/v1670929871/cover/flask-mongodb_kmrq6f.png" />
  <br/>
</p>

<p align="center" style="margin: 0.618rem 0 0.618rem 0">
Um simples setup de API RESTful com Flask e MongoDB.
</p>

<p align="center">
<img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
</p>

### Motivação

A ideia desse projeto é criar uma simples setup de API RESTful com Flask e MongoDB, para que possa ser utilizado como base para outros projetos.

### Funcionalidades

- Adicionar
- Listar
- Atualizar
- Deletar

### Instalação e execução

```bash
# Clone o repositório
$ git clone

# Entre na pasta
$ cd flask-mongodb

# Crie um ambiente virtual
$ python -m venv env

# Ative o ambiente virtual
$ source . env/bin/activate

# Instale as dependências
$ pip install -r requirements.txt

# Configure o arquivo .env
$ cp .env.example .env

# Configure o arquivo .env com as suas variáveis de ambiente
$ nano .env

# Rode o projeto
$ flask run ou python run.py
```

### Rotas da API

<table>
   <thead>
      <tr>
         <th>Endpoint</th>
         <th>Methods</th>
         <th>Rule</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>api_todos.todo</td>
         <td>DELETE, GET, PUT</td>
         <td>/todo/</td>
      </tr>
      <tr>
         <td>api_todos.todos</td>
         <td>GET, POST</td>
         <td>/</td>
      </tr>
      <tr>
         <td>static</td>
         <td>GET</td>
         <td>/static/</td>
      </tr>
   </tbody>
</table>
