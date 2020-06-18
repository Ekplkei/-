from tkinter import *

def entry(): # Переходы к основным окнам
    window_3.destroy()
    import Entry
    
def registration():
    window_3.destroy()
    import Registration
def guest():#
    window_3.destroy()
    import DeusNet
def rusEng():# Смена языка
    window_3.title('Start')
    entry.config(text='Entry')
    registration.config(text='Registartion')
    guest.config(text='Log in as a guest')
    Label.config(text='Welcome!\nChoose a way to log in to the site')
def engRus():#
    window_3.title('Начало')
    entry.config(text='Вход')
    registration.config(text='Регистрация')
    guest.config(text='Войти как гость')
    Label.config(text='Добро пожаловать!\nВыберете способ входа на сайт')
    


window_3=Tk()
window_3.title('Начало')
window_3.geometry('300x300')
window_3.option_add('*Font', ("Arial", 12))# установка шрифта
window_3.config(background='#9efff4')
window_3.resizable(False,False) # Запрет масштабирования

entry = Button (text='Вход',command = entry ); entry.place(x=150,y=130,width=130,heigh=35)
registration = Button (text='Регистрация',command = registration ); registration.place(x=20,y=130,width=130,heigh=35)
guest = Button (text='Войти как гость',command = guest ); guest.place(x=50,y=166,width=200,heigh=35)
Label=Label(text= "Добро пожаловать!\nВыберете способ входа на сайт",bg='#9efff4',font=('Arial',13)); Label.place(relx=0.07, y=45)

myMenu = Menu(window_3)
window_3.config(menu = myMenu)
myMenu.add_command(label = 'Закрыть', command = window_3.destroy)
myMenu.add_command(label = 'English', command = rusEng)
myMenu.add_command(label = 'Русский', command = engRus)

window_3.mainloop()
