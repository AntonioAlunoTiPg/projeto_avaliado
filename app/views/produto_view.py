import tkinter as tk
from tkinter import messagebox, simpledialog
from app.controllers.produto_controller import ProdutoController

def abrir_interface():
    controller = ProdutoController()

    def listar_produtos():
        lista.delete(0, tk.END)
        produtos = controller.listar_produtos()
        for p in produtos:
            lista.insert(tk.END, f"{p['id']} - {p['nome']} - R$ {p['preco']:.2f}")

    def adicionar_produto():
        nome = simpledialog.askstring("Nome do Produto", "Digite o nome do produto:")
        if not nome:
            messagebox.showwarning("Aviso", "Nome do produto é obrigatório.")
            return
        try:
            preco = float(simpledialog.askstring("Preço do Produto", "Digite o preço do produto:"))
        except (TypeError, ValueError):
            messagebox.showwarning("Aviso", "Preço inválido.")
            return

        controller.adicionar_produto(nome, preco)
        listar_produtos()

    def excluir_produto():
        selecionado = lista.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            return
        item = lista.get(selecionado)
        produto_id = int(item.split(" - ")[0])
        if messagebox.askyesno("Confirmação", f"Excluir produto ID {produto_id}?"):
            controller.excluir_produto(produto_id)
            listar_produtos()

    janela = tk.Tk()
    janela.title("Produtos")

    lista = tk.Listbox(janela, width=50)
    lista.pack(pady=10)

    btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
    btn_adicionar.pack(side=tk.LEFT, padx=10, pady=10)

    btn_excluir = tk.Button(janela, text="Excluir Produto", command=excluir_produto)
    btn_excluir.pack(side=tk.LEFT, padx=10, pady=10)

    listar_produtos()
    janela.mainloop()
