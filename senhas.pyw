import tkinter as tk
import random
import string
from tkinter import messagebox

# Função para gerar senha
def gerar_senha():
    comprimento = int(entry_comprimento.get())  # Obtém o comprimento da senha
    caracteres = ""
    
    # Adiciona caracteres conforme a seleção do usuário
    if var_maiusculas.get():
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation
    
    # Gera a senha
    if caracteres:
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        entry_senha.config(state='normal')  # Ativa a entrada para exibir a senha
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
        entry_senha.config(state='readonly')  # Desativa novamente após inserir a senha
    else:
        messagebox.showwarning("Seleção inválida", "Selecione pelo menos uma opção de caractere!")

# Configurações da interface
root = tk.Tk()
root.title("Gerador de Senhas - Kleber Klaar")

# Título do programa
label_titulo = tk.Label(root, text="Gerador de Senhas", font=("Helvetica", 16))
label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Labels e entradas
label_comprimento = tk.Label(root, text="Comprimento da senha:")
label_comprimento.grid(row=1, column=0, padx=5, pady=5)

entry_comprimento = tk.Entry(root)
entry_comprimento.grid(row=1, column=1, padx=5, pady=5)
entry_comprimento.insert(0, "8")  # Valor padrão

# Opções de caracteres
var_maiusculas = tk.BooleanVar()
check_maiusculas = tk.Checkbutton(root, text="Incluir Maiúsculas", variable=var_maiusculas)
check_maiusculas.grid(row=2, column=0, padx=5, pady=5)

var_minusculas = tk.BooleanVar()
check_minusculas = tk.Checkbutton(root, text="Incluir Minúsculas", variable=var_minusculas)
check_minusculas.grid(row=2, column=1, padx=5, pady=5)

var_numeros = tk.BooleanVar()
check_numeros = tk.Checkbutton(root, text="Incluir Números", variable=var_numeros)
check_numeros.grid(row=3, column=0, padx=5, pady=5)

var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(root, text="Incluir Símbolos", variable=var_simbolos)
check_simbolos.grid(row=3, column=1, padx=5, pady=5)

# Botão para gerar senha
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
btn_gerar.grid(row=4, column=0, columnspan=2, pady=10)

# Exibir senha gerada
entry_senha = tk.Entry(root, state='readonly', width=30)
entry_senha.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Rodapé com crédito
rodape = tk.Label(root, text="Criado por Kleber Klaar", anchor='center')
rodape.grid(row=6, column=0, columnspan=2, pady=10)

# Executa a interface
root.mainloop()
