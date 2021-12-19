#jokenpo
from random import *
from tkinter import *
#FC'S
def fc_pedra():
    jogadas = ['pedra', 'papel', 'tesoura']
    computer = choice(jogadas)
    jogador = 'pedra'
    print(jogador)
    print(computer)
    lb_extra = Label(root, text='', bg='red')
    if computer == 'papel':
        lb_extra.grid_forget()
        lb_extra = Label(root, text = 'Você perdeu!!',bg='red',fg='white')
        lb_extra.grid(row = 2, column = 1)
    elif computer == 'tesoura':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='Você venceu!!',bg='green',fg='white')
        lb_extra.grid(row=2, column=1)
    elif computer == 'pedra':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='EMPATE!!',bg='yellow',fg='blue')
        lb_extra.grid(row=2, column=1)

def fc_papel():
    jogadas = ['pedra', 'papel', 'tesoura']
    computer = choice(jogadas)
    jogador = 'papel'
    print(jogador)
    print(computer)
    lb_extra = Label(root, text='', bg='red')
    if computer == 'tesoura':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='Você perdeu!!', bg='red', fg='white')
        lb_extra.grid(row=2, column=1)
    elif computer == 'pedra':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='Você venceu!!', bg='green', fg='white')
        lb_extra.grid(row=2, column=1)
    elif computer == 'papel':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='EMPATE!!', bg='yellow', fg='blue')
        lb_extra.grid(row=2, column=1)

def fc_tesoura():
    jogadas = ['pedra', 'papel', 'tesoura']
    computer = choice(jogadas)
    jogador = 'tesoura'
    print(jogador)
    print(computer)
    lb_extra = Label(root, text='', bg='red')
    if computer == 'pedra':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='Você perdeu!!', bg='red', fg='white')
        lb_extra.grid(row=2, column=1)
    elif computer == 'papel':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='Você venceu!!', bg='green', fg='white')
        lb_extra.grid(row=2, column=1)
    elif computer == 'tesoura':
        lb_extra.grid_forget()
        lb_extra = Label(root, text='EMPATE!!', bg='yellow', fg='blue')
        lb_extra.grid(row=2, column=1)

#early window
root = Tk()
root.title('Jokenpo')
root['bg'] = 'black'
root.iconbitmap('game.ico')

#Button Widgets
lb_text = Label(root, text = '-=-=-=-=-!JOKENPO!-=-=-=--=-',bg='black',fg='red')
lb_text2 = Label(root, text = '!!!Faça sua escolha!!!',bg='black',fg='blue')
lb_space = Label(root, text='',bg='black')


bt_pedra = Button(root, text='Pedra',bg = 'black',padx=10,pady=10,fg='white',command = fc_pedra)
bt_papel = Button(root, text='Papel',padx=10,pady=10,bg = 'black',fg='white',command = fc_papel)
bt_tesoura = Button(root, text='Tesoura',padx=10,pady=10,bg = 'black',fg='white',command = fc_tesoura)

#posição
lb_text.grid(row = 0, column = 0,columnspan=3)
lb_text2.grid(row = 1, column = 0,columnspan=3)
lb_space.grid(row = 2, column = 0)

bt_pedra.grid(row = 3, column = 0,padx=10,pady=10)
bt_papel.grid(row = 3, column = 1,padx=10,pady=10)
bt_tesoura.grid(row = 3, column = 2,padx=10,pady=10)
#Over window
root.mainloop()


