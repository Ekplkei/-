from tkinter import *
from tkinter import messagebox
DataBase = 'DataBase.txt'

def entry_mall(): # открывает окно на вход
    window_1.destroy()
    import Entry

def happy(): # изменяет значение happy, чтобы была возможность зарегистрироваться со 2+ попытки
    global happy
    happy= True
    registration_mall()

def registration_mall(): # Процесс регистрации
    global happy
    if data.get() == 0: #Робот?
        if language: messagebox.showinfo('Робот?', 'Подтвердите, что вы не робот!')
        else: messagebox.showinfo('Robot?', 'Confirm that you are not a robot!')
    elif len(email_entry.get())<4:
        if language: messagebox.showinfo('Ошибка', 'Not enough characters!\nNeed at least 4')
        else: messagebox.showinfo('Error', 'Confirm that you are not a robot!')
        
    else:
        # определение id новой записи. Почему бы и нет?
        with open(DataBase) as f:
            last_entry = f.readlines()[-1] # считываем последнюю строку из файла базы данных
            next_id = int(last_entry.split()[0]) + 1 # определение id новой записи
            f.close()
            
        with open('DataBase.txt') as f: # Конечно не классы, но мне кажется
            # через БД удобнее
            datar = f.read() # Считывание всей бд
            stroka= datar.split('\n') # Конкретная строка
        
            k=datar.count('\n') # Количество активных строк в бд (без лейбла)
            for i in range (1,k+1):
                strochka = stroka[i].split('\t') # Захват определённого слова
                if email_entry.get() == strochka[1] or phone_entry.get()==strochka[2]:
                    # Если совпало, то процесс регистрации прерывается, новая строка в бд не появляется
                    happy = False
                    break
# Для чего это нужно? Для того, чтобы в бд не было повторений по телефону или мылу
        
        if happy: # Если повторений нет, то идёт запись новой строки
            with open(DataBase, 'a') as f:
                f.write('\n' + str(next_id) + '\t'+ email_entry.get() + '\t'+phone_entry.get() + '\t'+password_entry.get())
                f.close()
            with open('User.txt','w') as g:
                g.write(email_entry.get())
                
                g.close
            if language: messagebox.showinfo('Подтверждение', 'Вам на почту и телефон отправлено сообщение с подтверждением почты и телефонного номера')
            # Из разряда, не зачем, но очень хочется
            else: messagebox.showinfo('Confirmation', 'A message was sent to Your email and phone number confirming your email and phone number')
            window_1.destroy()
            import DeusNet
            
        else: # Если повторения есть
            if language: messagebox.showinfo('Неправильность', 'Аккаунт с данными данными уже существует')
            else: messagebox.showinfo('Incorrect', 'an Account with this data already exists')    

def eye (): # Всё так же видимость\невидимость пароля
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

def Privacy_policy_link (): # Открытие политики приватности
    import webbrowser
    if language:
        webbrowser.open("Политика конфединциальности.txt")
    else: webbrowser.open("Privacy policy.txt")
    
def rusEng(): # Перевод рус- анг
    global language
    window_1.title('Registration')
    registration_in_mall.config (text="Registration")
    phone.config (text='phone')
    password_lbl.config (text='Password')
    chbData.config (text="I'm not a robot")
    registration.config (text='registration')
    entry.config (text='entry')
    Privacy_policy.config (text='I have read and agree to the')
    Privacy_policy_link.config (text='privacy policy')
    if Check_eye:
        password_eye.config (text='invisiable')
    else: password_eye.config (text='visiable')
    language = False
    
def engRus():# Перевод анг- рус
    global language
    window_1.title('Регистрация')
    registration_in_mall.config (text="Регистрация")
    phone.config (text='Телефон')

    password_lbl.config (text='Пароль')
    chbData.config (text="Я не робот")
    registration.config (text='Регистрация')
    entry.config (text='Вход')

    if Check_eye:
        password_eye.config (text='Не виден')
    else: password_eye.config (text='виден')
    language = True

# Самообновление базы данных
with open('DataBase.txt') as f: 
    datar = f.read() # Считывание всей бд
    stroka= datar.split('\n') # Конкретная строка
    f.close()
if stroka[0] == 'Id	Email	Phone	password' and stroka [1] == '1	EkplkeiDei@yandex.ru	89234234123	кароль':
    pass # Если строчек нет, то база обновляется
else:
    with open(DataBase, 'w') as f: # Обновление базы данных и запись первого пользователя (меня). Данные не настоящие
        f.write("Id" + '\t' +  "Email" + '\t' + 'Phone' + '\t' + 'password'+ '\n')
        f.write("1" + '\t' +  "EkplkeiDei@yandex.ru" + '\t' + '89234234123' + '\t' + 'кароль')

        f.close()

window_1=Tk()
window_1.title('Регистрация')
window_1.geometry('300x300')
window_1.option_add('*Font', ("Arial", 12))# установка шрифта
window_1.config(background='#9efff4')
window_1.resizable(False,False) # Запрет масштабирования


registration_in_mall = Label(fg='#0040ff', bg='#9efff4', font='Arial 14', text="Регистрация"); registration_in_mall.place(x=32, y=3)

# мыло
email = Label(window_1, bg= '#9efff4', fg='#0055ff', font='Arial 10',borderwidth=0, padx=0,pady=0, text="Email");email.place(x= 32 ,y=30)
email_entry = Entry(window_1, width =27 , bg='white'); email_entry.place(x= 32 ,y=52)
k=email_entry.get()

# телефон
phone = Label(window_1, bg= '#9efff4', fg='#0055ff', font=('Arial', 10, 'normal'), borderwidth=0, padx=0,pady=0, text="Телефон");phone.place(x= 32 ,y=80)
phone_entry = Entry(window_1, font='Timesnewroman', width =27 , bg='white'); phone_entry.place(x= 32 ,y=102)
n=phone_entry.get()

# пароль
password_lbl = Label (fg='#0055ff', bg='#9efff4', font='Arial 10', text="Пароль"); password_lbl.place(x=30, y=130)
password_entry = Entry(window_1, show='*', font='Timesnewroman', width =27 , bg='white'); password_entry.place(x= 32 ,y=158)
password_eye = Button(window_1, bg= 'White', fg='#3098ff', font=('Arial', 8, 'normal'), borderwidth=0, padx=0,pady=0, text="Не виден",command=eye);password_eye.place(x= 220 ,y=160)

# политка приватности
Privacy_policy = Label(window_1, bg= '#9efff4', fg='#3098ff', font='Arial 7',borderwidth=0, padx=0,pady=0, text="Ознакомлен и согласен с ");Privacy_policy.place(x= 30 ,y=247)
Privacy_policy_link = Button(window_1, bg= '#9efff4', fg='#ff0000', font=('Arial', 7,'underline'),borderwidth=0, padx=0,pady=0, text="политикой конфиденциальности",command=Privacy_policy_link);Privacy_policy_link.place(x= 132 ,y=245)

#Всё то же серое поле
place= Label(text=2*(50*" "+'\n'));place.place(x=34, y=185) # Это не костыль (разве что чуть-чуть)

#Проверка на робота
data = IntVar()# переменная для хранения значения chbData
chbData = Checkbutton(text="Я не робот", variable = data, font='Arial 11'); chbData.place(x=34, y=201)
captcha = Label(text=':-) \n myCAPTCHA',font=('Arial', 8, 'italic'));captcha.place(x=166, y=201)

registration = Button(window_1, bg= '#b8ff7d', fg='#0040ff', text="Регистрация",command=happy);registration.place(x= 32 ,y=260, heigh=35, width= 115)
entry = Button(window_1, bg= '#b8ff7d', fg='#0040ff', text="Вход", command=entry_mall); entry.place(x= 152 ,y=260, heigh=35, width= 115)
# Переменные
Check_eye = True # для смены режима видимости пароля
language = True # для смены языков
happy = True # для успешного входа

# Верхняя менюшка
myMenu = Menu(window_1)
window_1.config(menu = myMenu)
myMenu.add_command(label = 'Закрыть', command = window_1.destroy) 
myMenu.add_command(label = 'English', command = rusEng)
myMenu.add_command(label = 'Русский', command = engRus)

window_1.mainloop()

