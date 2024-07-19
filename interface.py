
from tkinter import *
from tkinter import ttk

def destroy():
    root.destroy()
    
def execSystem():
    from Assets.transferApp import exec
    return exec(),destroy()

root = Tk()
root.title("Archive Transfer")

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calcular as coordenadas para centralizar a janela
x = (largura_tela // 2) - (400 // 2)
y = (altura_tela // 2) - (100 // 2)

# Definir a posição da janela
root.geometry(f'{400}x{100}+{x}+{y}')

frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="Deseja iniciar a transferencia de arquivos ?").grid(column=0,row=0)
ttk.Button(frm, text="Sim", command=execSystem).grid(column=0, row=1)
ttk.Button(frm, text="Não", command=root.destroy).grid(column=1, row=1)
root.mainloop()
