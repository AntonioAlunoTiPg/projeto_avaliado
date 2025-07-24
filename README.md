📦 README.md completo markdown
Copiar
Editar
# 🛍️ Sistema de Controle de Loja (Store Management System)

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Relational%20DB-yellow?logo=mysql)
![License](https://img.shields.io/badge/license-Free-lightgrey)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-informational)

---

## 📌 Sobre o Projeto

Este é um sistema desktop de controle de loja, com **cadastro de produtos, clientes e vendas**, desenvolvido em **Python** com interface gráfica **Tkinter**, banco de dados **MySQL** e arquitetura **MVC**.

> ✅ Ideal para estudos, pequenos comércios ou ponto de partida para sistemas maiores.

---

## 📁 Estrutura do Projeto

```bash
loja_sistema/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── views/
│   ├── database/
│   └── main.py
├── docs/
│   ├── requisitos.txt
│   ├── algoritmo.txt
│   ├── modelo_banco.png
│   └── DER/
├── .env
├── .gitignore
└── README.md
✅ Funcionalidades
🛒 Cadastro e listagem de Produtos

👤 Cadastro e listagem de Clientes

🧾 Registro de Vendas

🧠 Arquitetura MVC

🐬 Banco de dados MySQL

🖼️ Interface gráfica com Tkinter

🔐 Proteção de credenciais via .env

🧱 Código modular e organizado

💾 Banco de Dados
Banco de dados: loja_db

Tabelas: produtos, clientes, vendas

Modelo ER: docs/DER/modelo_banco.png

💡 Gere o diagrama automaticamente com:

bash
Copiar
Editar
python docs/DER/der_generator.py
⚙️ Instalação
✅ Requisitos
Python 3.10+

MySQL Server

Bibliotecas Python:

bash
Copiar
Editar
pip install -r requirements.txt
🔐 Configurar .env
Crie o arquivo .env com as credenciais do MySQL:

ini
Copiar
Editar
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=senha_do_seu_mysql
DB_NAME=loja_db
⚠️ O .env está no .gitignore e não deve ser versionado.

🚀 Como executar
bash
Copiar
Editar
# Clone o repositório
git clone https://github.com/seuusuario/loja_sistema.git
cd loja_sistema

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
python app/main.py
🖼️ Interface
Tela de Produtos

Tela de Clientes

Tela de Vendas

Menu inicial para navegação

📌 Observações
Venda simples: 1 produto por venda

Preparado para futura expansão: múltiplos itens, login, relatórios, etc

Recomendado usar ambiente virtual (venv)

👨‍💻 Author
Desolvolvido por - [Antonio] — 2025