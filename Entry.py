from tkinter import *
from tkinter import messagebox
def entry_mall(): # Вход на "сайт"
    global happy, m, stroka

    if data.get() == 0: # Проверка на робота
        if language: messagebox.showinfo('Робот?', 'Подтвердите, что вы не робот!')
        else: messagebox.showinfo('Robot?', 'Confirm that you are not a robot!')
    else: 
        
        Check() # проверка на совпадение логина(телефона) и пароля
        if happy: # Совпадение
            happy = False  # Флажок в исходное положение
            with open('User.txt','w') as g: # Запись мыла в User
                if count:
                    g.write(emailPhone.get())
                else:
                    with open('DataBase.txt') as f:
                        strochka = stroka[m].split('\t')
                        g.write(strochka[1])
                        f.close()
                g.close()
            window_0.destroy()
            import DeusNet
        else: # Не совпадение
            if language: messagebox.showinfo('Неправильность', 'Неправильно ведены данные \n проверьте правильность своих данных')
            else: messagebox.showinfo('Incorrect', 'data entered Incorrectly \n check that your data is correct')
        

def Check(): 
    global happy, m, stroka

    with open('DataBase.txt') as f:
        datar = f.read() # Файл
        stroka= datar.split('\n') # Строка в файле
        
        k=datar.count('\n')
        for i in range (1,k+1):
            strochka = stroka[i].split('\t') # слово в строке
            if count: # Флаг поднят, значит сравнение по мылу
                if emailPhone.get() == strochka[1] and password_entry.get()==strochka[3]:
                    happy = True # совпадение найдено
                    break
            else: # Флаг опущен, значит сравнение по телефону
                if emailPhone.get() == strochka[2] and password_entry.get()==strochka[3]:
                    happy = True
                    m=i
                    break
        

    
    
    
def registration_mall():# переход к окну регистрации
    window_0.destroy()
    import Registration
    
def click_email(): # Выбор захода по мылу
    global count
    if count:
        pass
    else:
        count = True
        email.config (bg= '#9efff4', fg='#ffa200')
        phone.config (bg= '#9efff4', fg='#0055ff')
        
def click_phone (): # Выбор захода по телефону
    global count
    if count:
        count = False
        email.config (bg= '#9efff4', fg='#0055ff')
        phone.config (bg= '#9efff4', fg='#ffa200')
def eye (): # видимость не видимость пароля
    global Check_eye
    if Check_eye:
        password_entry.config (show='')
        if language: password_eye.config (text='Виден')
        else: password_eye.config (text='visiable')
        Check_eye = False
    else:
        password_entry.config (show='*')
        if language: password_eye.config (text='Не виден')
        else: password_eye.config (text='invisiable')
        Check_eye = True

def bad_brain (): # стандартное "вы забыли пароль"
    global count
    if language:
        if count: messagebox.showinfo('Помощь в восcтановлении пароля', 'Пароль выслан вам на ваш Email')
        else: messagebox.showinfo('Помощь в восcтановлении пароля', 'Пароль выслан вам на ваш телефон')
    else:
        if count: messagebox.showinfo('Help in password recovery', 'Password sent to your Email')
        else: messagebox.showinfo('Help with password recovery', 'Password sent to your phone')
    
def rusEng(): # переход с русского на английский
    global language
    window_0.title('Entry')
    entry_in_mall.config (text="Enter the store")
    phone.config (text='phone')
    e_or_p.config (text='or')
    password_lbl.config (text='Password')
    chbData.config (text="I'm not a robot")
    registration.config (text='registration')
    entry.config (text='entry')
    bad_brain.config (text="Don't remember your password?")
    if Check_eye:
        password_eye.config (text='invisiable')
    else: password_eye.config (text='visiable')
    language = False
    
def engRus(): # переход с английского на русский
    global language
    window_0.title('Вход')
    entry_in_mall.config (text="Войти в магазин")
    phone.config (text='Телефон')
    e_or_p.config (text='или')
    password_lbl.config (text='Пароль')
    chbData.config (text="Я не робот")
    registration.config (text='Регистрация')
    entry.config (text='Вход')
    bad_brain.config (text="Не помните пароль?")
    if Check_eye:
        password_eye.config (text='Не виден')
    else: password_eye.config (text='виден')
    language = True
    pass

window_0=Tk()
window_0.title('Вход')
window_0.geometry('300x300')
window_0.option_add('*Font', ("Arial", 12))# установка шрифта
window_0.config(background='#9efff4')
window_0.resizable(False,False) # Запрет масштабирования

entry_in_mall = Label(fg='#0040ff', bg='#9efff4', font='Arial 14', text="Войти в магазин"); entry_in_mall.place(x=32, y=3)
## выбор через что вход (мыло или телефон)
email = Button(window_0, bg= '#9efff4', fg='#ffa200', font='Arial 10',borderwidth=0, padx=0,pady=0, text="Email",command=click_email);email.place(x= 32 ,y=30)
e_or_p = Label (fg='#000', bg='#9efff4', font='Arial 8', text="Или"); e_or_p.place(x=88, y=32)
phone = Button(window_0, bg= '#9efff4', fg='#0055ff', font=('Arial', 10, 'normal'), borderwidth=0, padx=0,pady=0, text="Телефон",command=click_phone);phone.place(x= 125 ,y=30)
emailPhone = Entry(window_0, width =27 , bg='white'); emailPhone.place(x= 32 ,y=52)
# пароль
password_lbl = Label (fg='#0055ff', bg='#9efff4', font='Arial 10', text="Пароль"); password_lbl.place(x=30, y=80)
password_entry = Entry(window_0, show='*', font='Timesnewroman', width =27 , bg='white'); password_entry.place(x= 32 ,y=102)
password_eye = Button(window_0, bg= 'White', fg='#3098ff', font=('Arial', 8, 'normal'), borderwidth=0, padx=0,pady=0, text="Не виден",command=eye);password_eye.place(x= 220 ,y=104)
# забыли пароль
bad_brain = Button(window_0, bg= '#9efff4', fg='#ff0000', font='Arial 11',borderwidth=0, padx=0,pady=0, text="Не помните пароль?",command=bad_brain);bad_brain.place(x= 30 ,y=130)
# Мб костыль, но он лёгок в применении и не занимает много времени
place= Label(text=2*(50*" "+'\n'));place.place(x=34, y=160) # Это не костыль (разве что чуть-чуть)
# Капча от роботов
data = IntVar()# переменная для хранения значения chbData
chbData = Checkbutton(text="Я не робот", variable = data, font='Arial 11'); chbData.place(x=34, y=175)
captcha = Label(text=':-) \n myCAPTCHA',font=('Arial', 8, 'italic'));captcha.place(x=166, y=175)
# Кнопки регистрации и входа
registration = Button(window_0, bg= '#b8ff7d', fg='#0040ff', text="Регистрация",command=registration_mall);registration.place(x= 32 ,y=230, heigh=35, width= 115)
entry = Button(window_0, bg= '#b8ff7d', fg='#0040ff', text="Вход", command=entry_mall); entry.place(x= 152 ,y=230, heigh=35, width= 115)
# Переменные
count = True # отвечает за способ входа (мыло и телефон)
Check_eye = True # отвечает за видимость/ не видимость пароля
language = True # отвечает за язык
happy = False # переменная- разрешение на вход

# Верхняя менюшка
myMenu = Menu(window_0)
window_0.config(menu = myMenu)
myMenu.add_command(label = 'Закрыть', command = window_0.destroy)
myMenu.add_command(label = 'English', command = rusEng)
myMenu.add_command(label = 'Русский', command = engRus)

window_0.mainloop()

