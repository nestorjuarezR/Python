from tkinter import *
from tkinter import messagebox

# ----- Variable global -----

i = 0

# ----- Funciones -----

def info():
    messagebox.showinfo('Información', 'Creado por:\nNéstor Juárez')

def salir():
    x = messagebox.askyesno('Salir', '¿Desea realmente salilr?')
    if x == True:
        root.destroy()

def click(valor):
    global i
    entrada.insert(i, valor)
    i += 1

def borrar():
    entrada.delete(0, END)
    i = 0

def borrar_num():
    display_state = entrada.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        borrar()
        entrada.insert(0,display_new_state)
    else:
        borrar()

def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    i = 0

# ----- Raiz -----

root = Tk()
root.title('Calculadora')
root.config(bg='#3E3939', width=300,height=300, cursor='hand1')
root.option_add('*Dialog.msg.font', 'Helvetica 10')
root.resizable(0,0)

# ----- Barra Menu -----

barraMenu = Menu(root)
root.config(menu=barraMenu)

opcionesMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Opciones', font=('Helvetica 10'), menu=opcionesMenu)
opcionesMenu.add_command(label='Acerca de', command=info, font=('Helvetica 9'))
opcionesMenu.add_command(label='Salir', command=salir, font=('Helvetica 9'))

# ----- Entrada -----

entrada = Entry(root,bg='#8EBE78',font=('Helvetica 20'))
entrada.grid(row=0, column=0, columnspan=4,
            padx=5, pady=5)

# ----- Botones -----

boton1 = Button(root, text='1', width=5, height=2, bd=0, command= lambda: click(1))
boton2 = Button(root, text='2', width=5, height=2, bd=0, command= lambda: click(2))
boton3 = Button(root, text='3', width=5, height=2, bd=0, command= lambda: click(3))
boton4 = Button(root, text='4', width=5, height=2, bd=0, command= lambda: click(4))
boton5 = Button(root, text='5', width=5, height=2, bd=0, command= lambda: click(5))
boton6 = Button(root, text='6', width=5, height=2, bd=0, command= lambda: click(6))
boton7 = Button(root, text='7', width=5, height=2, bd=0, command= lambda: click(7))
boton8 = Button(root, text='8', width=5, height=2, bd=0, command= lambda: click(8))
boton9 = Button(root, text='9', width=5, height=2, bd=0, command= lambda: click(9))
boton0 = Button(root, text='0', width=5, height=2, bd=0, command= lambda: click(0))

boton_borrar_todo = Button(root, text='DEL', width=5, height=2, bg='#6D7872', fg='white', bd=0, command= lambda: borrar())
boton_borrar_numero =  Button(root, text='↞', width=5, height=2, bg='#6D7872', fg='white', bd=0, command= lambda: borrar_num())
boton_parentesis1 = Button(root, text='(', width=5, height=2, bg='#6D7872', fg='white',bd=0, command= lambda: click('('))
boton_parentesis2 = Button(root, text=')', width=5, height=2, bg='#6D7872', fg='white', bd=0, command= lambda: click(')'))
boton_punto = Button(root, text='.', width=5, height=2, bg='#6D7872', bd=0, fg='white', command= lambda: click('.'))

boton_div = Button(root, text='/', width=5, height=2, bg='#6D7872', bd=0, fg='white', command= lambda: click('/'))
boton_multi = Button(root, text='x', width=5, height=2, bg='#6D7872', bd=0, fg='white', command= lambda: click('*'))
boton_sum = Button(root, text='+', width=5, height=2, bg='#6D7872', bd=0, fg='white', command= lambda: click('+'))
boton_rest = Button(root, text='-', width=5, height=2, bg='#6D7872', bd=0, fg='white', command= lambda: click('-'))
boton_igual = Button(root, text='=', width=5, height=2, bg='#E18B29', bd=0, fg='white', command= lambda: operaciones())

# ----- Estructura de botones -----

boton_borrar_todo.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=2)
boton8.grid(row=2, column=1, padx=5, pady=2)
boton9.grid(row=2, column=2, padx=5, pady=2)
boton_multi.grid(row=2, column=3, padx=5, pady=2)

boton4.grid(row=3, column=0,padx=5, pady=2)
boton5.grid(row=3, column=1,padx=5, pady=2)
boton6.grid(row=3, column=2,padx=5, pady=2)
boton_sum.grid(row=3, column=3,padx=5, pady=2)

boton1.grid(row=4, column=0,padx=5, pady=2)
boton2.grid(row=4, column=1,padx=5, pady=2)
boton3.grid(row=4, column=2,padx=5, pady=2)
boton_rest.grid(row=4, column=3,padx=5, pady=2)

boton0.grid(row=5, column=0, padx=5, pady=2)
boton_borrar_numero.grid(row=5, column=1, padx=5, pady=2)
boton_punto.grid(row=5, column=2, padx=5, pady=2)
boton_igual.grid(row=5, column=3, padx=5, pady=2)

root.mainloop()