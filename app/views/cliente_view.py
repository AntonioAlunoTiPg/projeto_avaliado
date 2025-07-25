import tkinter as tk
from app.controllers.cliente_controller import ClienteController

def abrir_interface():
    def adicionar():
        nome = entry_nome.get()
        email = entry_email.get()
        ClienteController.adicionar_cliente(nome, email)
        listar()

    def listar():
        lista.delete(0, tk.END)
        for c in ClienteController.listar_clientes():
            lista.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]}")

    janela = tk.Tk()
    janela.title("Controle de Clientes")

    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Email").pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Button(janela, text="Adicionar Cliente", command=adicionar).pack()

    lista = tk.Listbox(janela, width=50)
    lista.pack()

    listar()
    janela.mainloop()
