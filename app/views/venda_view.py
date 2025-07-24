import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from app.controllers.venda_controller import VendaController
from app.controllers.cliente_controller import ClienteController
from app.controllers.produto_controller import ProdutoController

def abrir_interface():
    def adicionar():
        try:
            cliente_idx = combo_cliente.current()
            produto_idx = combo_produto.current()
            quantidade = int(entry_quantidade.get())

            if cliente_idx == -1 or produto_idx == -1:
                messagebox.showerror("Erro", "Selecione cliente e produto")
                return

            cliente_id = clientes[cliente_idx][0]
            produto_id = produtos[produto_idx][0]
            preco_unit = produtos[produto_idx][2]
            valor_total = preco_unit * quantidade
            data_venda = date.today().isoformat()

            VendaController.adicionar_venda(cliente_id, produto_id, quantidade, data_venda, valor_total)
            listar()
            messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida")

    def listar():
        lista.delete(*lista.get_children())
        vendas = VendaController.listar_vendas()
        for v in vendas:
            lista.insert("", "end", values=v)

        # Atualiza combos
        global clientes, produtos
        clientes = ClienteController.listar_clientes()
        produtos = ProdutoController.listar_produtos()

        combo_cliente['values'] = [c[1] for c in clientes]
        combo_produto['values'] = [p[1] for p in produtos]

    janela = tk.Tk()
    janela.title("Controle de Vendas")

    tk.Label(janela, text="Cliente").grid(row=0, column=0)
    combo_cliente = ttk.Combobox(janela, state="readonly")
    combo_cliente.grid(row=0, column=1)

    tk.Label(janela, text="Produto").grid(row=1, column=0)
    combo_produto = ttk.Combobox(janela, state="readonly")
    combo_produto.grid(row=1, column=1)

    tk.Label(janela, text="Quantidade").grid(row=2, column=0)
    entry_quantidade = tk.Entry(janela)
    entry_quantidade.grid(row=2, column=1)

    tk.Button(janela, text="Registrar Venda", command=adicionar).grid(row=3, column=0, columnspan=2)

    cols = ("ID", "Cliente", "Produto", "Quantidade", "Data", "Valor Total")
    lista = ttk.Treeview(janela, columns=cols, show="headings")
    for col in cols:
        lista.heading(col, text=col)
    lista.grid(row=4, column=0, columnspan=2)

    listar()
    janela.mainloop()
