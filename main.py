import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from views.produto_view import abrir_interface as abrir_produto
from views.cliente_view import abrir_interface as abrir_cliente
from views.venda_view import abrir_interface as abrir_venda

def main():
    janela = tk.Tk()
    janela.title("Sistema de Controle de Loja")

    tk.Button(janela, text="Produtos", width=20, command=lambda: [janela.destroy(), abrir_produto()]).pack(pady=5)
    tk.Button(janela, text="Clientes", width=20, command=lambda: [janela.destroy(), abrir_cliente()]).pack(pady=5)
    tk.Button(janela, text="Vendas", width=20, command=lambda: [janela.destroy(), abrir_venda()]).pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    main()
