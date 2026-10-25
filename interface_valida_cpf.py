import tkinter as tk
from valida_cpf import validar_cpf

#cores
COR_FUNDO = "#1e1e1e"        # Cinza
COR_TEXTO = "#ffffff"        # Branco
COR_BOTAO = "#2a2a2a"        # Cinza claro
COR_AZUL = "#3b82f6"         # Azul moderno
COR_AZUL_HOVER = "#2563eb"   # Azul escuro
COR_VERMELHO = "#ef4444"     # Vermelho 
COR_VERDE = "#10b981"        # Verde

#config janela
janela = tk.Tk()
janela.title("Validar CPF")
janela.geometry("350x400")
janela.config(bg=COR_FUNDO)

#texto Digite
titulo1 = tk.Label(janela, text="DIGITE O CPF", bg=COR_FUNDO, fg=COR_TEXTO)
titulo1.place(relx=0.5, rely=0.3, anchor="center")

#entrada cpf
cpf_entrada = tk.Entry(janela,
bg=COR_BOTAO, 
fg=COR_TEXTO,
relief="flat",
bd=0)

cpf_entrada.place(relx=0.5, rely=0.35, anchor="center")

#Função para formatar o entry
def formatar_cpf(event):
    texto = cpf_entrada.get()
    apenas_nums = "".join([c for c in texto if c.isdigit()])[:11]
    
    novo_texto = ""
    for i, c in enumerate(apenas_nums):
        if i == 3 or i == 6:
            novo_texto += "."
        elif i == 9:
            novo_texto += "-"
        novo_texto += c
    #atualiza o campo
    if novo_texto != texto:
        cpf_entrada.delete(0, tk.END)
        cpf_entrada.insert(0, novo_texto)

# Vincula o evento
cpf_entrada.bind("<KeyRelease>", formatar_cpf)

#texto resposta
texto_resposta = tk.Label(janela, 
text="",
 bg=COR_FUNDO)
 
texto_resposta.place(relx=0.5, rely=0.5, anchor= "center")
        
#resposta botao
def resposta_botao():
    cpf_resposta = cpf_entrada.get()
    valida, mensagem = validar_cpf(cpf_resposta)
    if valida:
       texto_resposta.config(text=mensagem, fg=COR_VERDE)
    else:
       texto_resposta.config(text=mensagem, fg=COR_VERMELHO) 
       
#botao que valida
botao_ver = tk.Button(
janela, text="ACESSAR", 
bg=COR_AZUL, 
fg=COR_TEXTO, 
relief="flat",
cursor="hand2",
command=resposta_botao)

botao_ver.place(relx=0.5, rely=0.42, anchor="center")

janela.mainloop()