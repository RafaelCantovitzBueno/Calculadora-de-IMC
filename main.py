import customtkinter as ctk

# Light
cores_light = {
'cor0': "#2C3E50", 
'cor1': "#ECF0F1",  
'cor2': "#3498DB", 
'cor3': "#E5E8E8", 
'cor4': "#16A085", 
'cor5': "#95A5A6"
}

# Dark
cores_dark = {
    'cor0' : "#fff",
    'cor1' : "#fff",
    'cor2': "#3498DB",
    'cor3' : "#fff",
    'cor4' : "#FFFF00",
    'cor5' : "#fff"
}

tema = 'light'
cores = cores_light

ctk.set_appearance_mode(tema)
app = ctk.CTk()
app.title("Calculadora de IMC")
app.geometry("440x540")
app.configure(bg=cores['cor3'])

# Função para trocar o Tema
def trocar_modo():
    global tema, cores
    if tema == 'light':
        ctk.set_appearance_mode('dark')
        tema = 'dark'
        temab.configure(text='Dark')
        cores = cores_dark
        atualizar_cores()
    else:
        ctk.set_appearance_mode('light')
        tema = 'light'
        temab.configure(text='Light')
        cores = cores_light
        atualizar_cores()
        

# Configurações do Tema
def atualizar_cores():
    app.configure(text_color=cores['cor3'])
    tema_app.configure(text_color=cores['cor0'])
    temab.configure(fg_color=cores['cor2'])
    nome_app.configure(text_color=cores['cor4'])
    lpeso.configure(text_color=cores['cor0'])
    laltura.configure(text_color=cores['cor0'])
    lresultado.configure(text_color=cores['cor0'])
    lresultado_texto.configure(text_color=cores['cor0'])
    bcalcular.configure(fg_color=cores['cor2'])

# Função para calcular o IMC
def calcular():
    peso = float(epeso.get())
    altura = float(ealtura.get()) ** 2
    resultado = peso/altura

    if resultado < 18.6:
        lresultado_texto.configure(text='Seu IMC é abaixo do peso')
    elif resultado >= 18.6 and resultado < 24.9:
        lresultado_texto.configure(text='Seu IMC é normal')
    elif resultado >= 25 and resultado < 29.9:
        lresultado_texto.configure(text='Seu IMC é sobrepeso')
    else:
        lresultado_texto.configure(text='Seu IMC é obesidade')

    # Resetar os inputs do usuario
    epeso.delete(0, 'end')
    ealtura.delete(0, 'end')

    # Configurações de Aparencia
    lresultado.configure(font=('Arial', 30, 'bold'))
    lresultado_texto.configure(font=('Arial', 16))

    lresultado.configure(text="{:.{}f}".format(resultado, 2))

# Dividindo a janela
janela_tema = ctk.CTkFrame(app, width=400, height=30, corner_radius=15)
janela_tema.grid(row=0, column=0, sticky='nsew', padx=20, pady=5)

janela_superior = ctk.CTkFrame(app, width=400, height=90, corner_radius=15)
janela_superior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

janela_inferior = ctk.CTkFrame(app, width=400, height=380, corner_radius=15)
janela_inferior.grid(row=2, column=0, sticky='nsew', padx=20, pady=20)

# Janela Tema
tema_app = ctk.CTkLabel(janela_tema, text='Tema', text_color=cores['cor0'], font=('Arial', 15, 'bold'))
tema_app.grid(row=0, column=0, sticky='nsew', padx=15, pady=15)
janela_tema.columnconfigure(0, weight=0) # Label fixo

temab = ctk.CTkButton(janela_tema, text='Light', width=180, height=50, font=('Arial', 16, 'bold'), fg_color=cores['cor2'], hover_color="#2980B9", corner_radius=12, command=trocar_modo)
temab.grid(row=0, column=1, sticky='e', padx=15, pady=5)
janela_tema.columnconfigure(1, weight=1) # Botão expandindo

# Janela Superior
nome_app = ctk.CTkLabel(janela_superior, text='Calculadora de IMC', text_color=cores['cor4'], anchor='center', font=('Arial', 30, 'bold'))
nome_app.place(x=0, y=25, relwidth=1)

# Janela Inferior
lpeso = ctk.CTkLabel(janela_inferior, text='Digite seu peso (kg)', text_color=cores['cor0'], font=('Arial', 14))
lpeso.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

epeso = ctk.CTkEntry(janela_inferior, width=180, font=('Arial', 16), justify='center', corner_radius=12)
epeso.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)


laltura = ctk.CTkLabel(janela_inferior, text='Digite sua altura (m)', text_color=cores['cor0'], font=('Arial', 14))
laltura.grid(row=2, column=0, sticky='nw', padx=15, pady=15)

ealtura = ctk.CTkEntry(janela_inferior, width=180, font=('Arial', 16), justify='center', corner_radius=12)
ealtura.grid(row=2, column=1, sticky='nsew', padx=15, pady=15)

lresultado = ctk.CTkLabel(janela_inferior, text='', width=5, height=1, text_color=cores['cor0'], anchor='center', corner_radius=12)
lresultado.grid(row=3, column=0, columnspan=2, padx=15, pady=2)


lresultado_texto = ctk.CTkLabel(janela_inferior, text='', text_color=cores['cor0'], anchor='center')
lresultado_texto.grid(row=4, column=0, columnspan=2, padx=15, pady=2)

# Botão
bcalcular = ctk.CTkButton(janela_inferior, text='Calcular', width=180, height=50, font=('Arial', 16, 'bold'), fg_color=cores['cor2'], hover_color="#2980B9", corner_radius=12, command=calcular)
bcalcular.grid(row=5, column=0, columnspan=2, padx=15, pady=25)

# Iniciar a aplicação
app.mainloop()