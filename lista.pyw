import tkinter as tk
from tkinter import messagebox, ttk
import json

class Produto:
    def __init__(self, nome, quantidade, preco, setor):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.setor = setor

    def __str__(self):
        return f"{self.nome} - Q: {self.quantidade} - R$ {self.preco:.2f} - {self.setor}"

class ListaDeComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        
        self.produtos = []

        # Configuração da tabela
        self.tree = ttk.Treeview(root, columns=("Nome", "Quantidade", "Preço", "Setor"), show='headings')
        self.tree.heading("Nome", text="Produto", command=lambda: self.ordenar_coluna("Nome"))
        self.tree.heading("Quantidade", text="Quantidade", command=lambda: self.ordenar_coluna("Quantidade"))
        self.tree.heading("Preço", text="Preço", command=lambda: self.ordenar_coluna("Preço"))
        self.tree.heading("Setor", text="Setor", command=lambda: self.ordenar_coluna("Setor"))
        
        # Centralizando as informações
        for col in ("Nome", "Quantidade", "Preço", "Setor"):
            self.tree.column(col, anchor='center')
        
        self.tree.pack(padx=10, pady=10)

        # Configurar largura das colunas
        self.tree.column("Nome", width=150)
        self.tree.column("Quantidade", width=100)
        self.tree.column("Preço", width=100)
        self.tree.column("Setor", width=100)

        # Configurações da interface
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label_nome = tk.Label(self.frame, text="Produto:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        self.label_quantidade = tk.Label(self.frame, text="Quantidade:")
        self.label_quantidade.grid(row=1, column=0)
        self.entry_quantidade = tk.Entry(self.frame)
        self.entry_quantidade.grid(row=1, column=1)

        self.label_preco = tk.Label(self.frame, text="Preço:")
        self.label_preco.grid(row=2, column=0)
        self.entry_preco = tk.Entry(self.frame)
        self.entry_preco.grid(row=2, column=1)

        self.label_setor = tk.Label(self.frame, text="Setor:")
        self.label_setor.grid(row=3, column=0)
        self.entry_setor = tk.Entry(self.frame)
        self.entry_setor.grid(row=3, column=1)

        # Configurando os botões lado a lado
        self.btn_frame = tk.Frame(self.frame)
        self.btn_frame.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_adicionar = tk.Button(self.btn_frame, text="Adicionar Produto", command=self.adicionar_produto)
        self.btn_adicionar.grid(row=0, column=0, padx=5)

        self.btn_remover = tk.Button(self.btn_frame, text="Remover Produto", command=self.remover_produto)
        self.btn_remover.grid(row=0, column=1, padx=5)

        self.btn_total = tk.Button(self.btn_frame, text="Calcular Total", command=self.calcular_total)
        self.btn_total.grid(row=0, column=2, padx=5)

        self.btn_salvar = tk.Button(self.btn_frame, text="Salvar Lista", command=self.salvar_lista)
        self.btn_salvar.grid(row=0, column=3, padx=5)

        self.btn_carregar = tk.Button(self.btn_frame, text="Carregar Lista", command=self.carregar_lista)
        self.btn_carregar.grid(row=0, column=4, padx=5)

        # Rodapé
        self.rodape = tk.Label(root, text="Criado por Kleber Klaar", fg="gray")
        self.rodape.pack(side=tk.BOTTOM, pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        preco = self.entry_preco.get()
        setor = self.entry_setor.get()
        
        if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit() and setor:
            produto = Produto(nome, int(quantidade), float(preco), setor)
            self.produtos.append(produto)
            self.atualizar_tabela()
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

    def atualizar_tabela(self):
        # Limpar a tabela antes de atualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        for produto in self.produtos:
            self.tree.insert("", tk.END, values=(produto.nome, produto.quantidade, f"R$ {produto.preco:.2f}", produto.setor))

    def remover_produto(self):
        selecionado = self.tree.selection()
        if selecionado:
            for item in selecionado:
                self.tree.delete(item)
                index = self.tree.index(item)
                del self.produtos[index]
            self.atualizar_tabela()
        else:
            messagebox.showwarning("Atenção", "Selecione um produto para remover.")

    def calcular_total(self):
        total = sum(p.quantidade * p.preco for p in self.produtos)
        messagebox.showinfo("Total", f"Total da compra: R$ {total:.2f}")

    def salvar_lista(self):
        with open("lista_de_compras.json", "w") as file:
            json.dump([vars(p) for p in self.produtos], file)
        messagebox.showinfo("Sucesso", "Lista salva com sucesso!")

    def carregar_lista(self):
        try:
            with open("lista_de_compras.json", "r") as file:
                produtos = json.load(file)
                self.produtos = [Produto(**p) for p in produtos]
                self.atualizar_tabela()
            messagebox.showinfo("Sucesso", "Lista carregada com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")

    def ordenar_coluna(self, coluna):
        # Função para ordenar a tabela
        self.produtos.sort(key=lambda p: getattr(p, coluna.lower()), reverse=False)
        self.atualizar_tabela()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_setor.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeComprasApp(root)
    root.mainloop()
