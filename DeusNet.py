from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

class Goods(): # Можно было бы построить работу на классах, но я посчитал лучше использовать базы данных
    pass
class Buyers():
    pass

def talisman(): # А кто не любит котиков?
    import webbrowser
    webbrowser.open("music.mp3")
    import Talisman
    
def pressF(): # Просиба кликнуть на DeusNet
    if language: messagebox.showinfo('Клик', 'Нажмите на DeusNet!')
    else: messagebox.showinfo('Click', 'Click on DeusNet!')


def com (): # Действие кнопок в top (на уровне с DeusNet и "Вход")
    global language
    if language: messagebox.showinfo('Жаль', 'Для сравнения ничего нет')
    else: messagebox.showinfo('Sorry', 'There is nothing for comparison')
    
def fav ():
    global language
    if language: messagebox.showinfo('Sorry', 'Ничего нет в вашем списке желаний')
    else: messagebox.showinfo('Sorry', ' Nothing is on your wish list')
    
def shop (): #
    global language
    if language: messagebox.showinfo('Жаль', 'Эх, корзина пуста\n Вы уже приласкали котика?')
    else: messagebox.showinfo('Sorry', ' Eh, the basket is empty\n Have you petted the cat yet?')

def Choice():# Дейтвие кнопки "Вход"
    window_2.destroy()
    import Start

def rusEng(): # Смена языка
    global language
    Button_left_place_1.config (text = "Computers and\naccessories")
    Button_left_place_2.config (text = "Accessories")
    Button_left_place_3.config (text = "Internet and\nperipherals")
    Button_left_place_4.config (text = "Office\nequipment")
    Button_left_place_5.config (text = "Services")
    Button_left_place_6.config (text = "Markdown")
    Button_left_place_7.config (text = "Question-answer")

    plase_gray_price_1.config (text = "Top product\nof the week")
    plase_gray_price_2.config (text = "Popular promotions")
    plase_gray_price_3.config (text = "Promotions for members\nclub bonus")
    plase_gray_price_4.config (text = "News")
    plase_gray_price_5.config (text = "Novelty")
    plase_gray_price_6.config (text = "Novelty\nthe news")
    plase_gray_price_7.config (text = "News about\nnew product")

    
    poisk.delete(0, END)
    poisk.insert(0,'Search by store')
    Compare.config (text = 'Compare')
    favorites.config (text = 'favorites')
    shopping_cart.config (text = 'Basket')
    entry.config (text = 'entry')
    
    shops.config (text = 'shops')
    Buyers.config (text = 'Buyers')
    Partners.config (text = 'Partners')
    Bonus_club.config (text = 'Bonus_club')
    Number.config (text = '+7-812-322-20-12 (6 - 18)')
    language = False
    

def engRus():#
    global language
    Button_left_place_1.config (text = "Компьютеры и\nкомплектующие")
    Button_left_place_2.config (text = "Акссесуары")
    Button_left_place_3.config (text = "Интернет и\nперефирия")
    Button_left_place_4.config (text = "Офисная\nтехника")
    Button_left_place_5.config (text = "Услуги")
    Button_left_place_6.config (text = "Уценка")
    Button_left_place_7.config (text = "Вопрос- ответ")

    plase_gray_price_1.config (text = "Топ товар\nнедели")
    plase_gray_price_2.config (text = "Популярные акции")
    plase_gray_price_3.config (text = "Акции для участников\nбонус клуба")
    plase_gray_price_4.config (text = "Новость")
    plase_gray_price_5.config (text = "Новинка")
    plase_gray_price_6.config (text = "Новинка\nновости")
    plase_gray_price_7.config (text = "Новость о\nновинке")

    poisk.delete(0, END)
    poisk.insert(0,'Поиск по магазину')
    Compare.config (text = 'Сравнить')
    favorites.config (text = 'Избранное')
    shopping_cart.config (text = 'Корзина')
    entry.config (text = 'Вход')

    shops.config (text = 'Магазины')
    Buyers.config (text = 'Покупателям')
    Partners.config (text = 'Партнёрам')
    Bonus_club.config (text = 'Бонус клуб')
    Number.config (text = '+7-812-322-20-12 (с 6 до 18)')
    language = True
    


window_2 = Tk()
window_2.title('DeusNet')
window_2.geometry('820x425')
window_2.option_add('*Font', ("Arial", 10))# установка шрифта
window_2.config(background='white')
window_2.resizable(False,False) # Запрет масштабирования

# Цветные поля :-)
place_top_top=Label(text='', bg='#00b7ff'); place_top_top.place(x=0,y=0,relwidth=1.0,height=28)
place_top = Label(text='', bg='#0075d5'); place_top.place(x=0,y=28,relwidth=1.0,height=55)
place_left = Label(text='', bg='#d9ffe8'); place_left.place(x=10,y=100,width=114,height=310)

# Аксессуарные кнопки
Button_left_place_1 = Button (text = "Компьютеры и\nкомплектующие",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_1.place (x = 11, y=105)
Button_left_place_2 = Button (text = "Акссесуары",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_2.place (x = 23, y=156)
Button_left_place_3 = Button (text = "Интернет и\nперефирия",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_3.place (x = 23, y=195 )
Button_left_place_4 = Button (text = "Офисная\nтехника",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_4.place (x = 24, y=255)
Button_left_place_5 = Button (text = "Услуги",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_5.place (x = 30, y=309)
Button_left_place_6 = Button (text = "Уценка",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_6.place (x = 30, y=345)
Button_left_place_7 = Button (text = "Вопрос- ответ",bg="#d9ffe8", bd=0, command=pressF );Button_left_place_7.place (x = 17, y=380)


# Нижний пак кнопок
place_biruze_pack_price = Label (text='', bg='#b8e5ff');place_biruze_pack_price.place(x=150,y=250,width=590,height=160)
News= Label (text='Новости и новинки', bg='#b8e5ff', font='Arial, 11'); News.place (x=155, y= 265)

plase_gray_price_1 = Button (text = "Топ товар\nнедели",bg="#ededed", bd=0, command=pressF );plase_gray_price_1.place (x = 150, y=100, width = 120, height = 110 )
plase_gray_price_2 = Button (text = "Популярные акции",bg="#ededed", bd=0, command=pressF);plase_gray_price_2.place (x = 300, y=100, width = 240, height = 110 )
plase_gray_price_3 = Button (text = "Акции для участников\nбонус клуба",bg="#ededed", bd=0, command=pressF);plase_gray_price_3.place (x = 560, y=100, width = 180, height = 110 )
plase_gray_price_4 = Button (text = "Новость",bg="#ededed", bd=0, command=pressF);plase_gray_price_4.place (x = 160, y=300, width = 125, height = 90 )
plase_gray_price_5 = Button (text = "Новинка",bg="#ededed", bd=0, command=pressF);plase_gray_price_5.place (x = 300, y=300, width = 125, height = 90 )
plase_gray_price_6 = Button (text = "Новинка\nновости",bg="#ededed", bd=0, command=pressF);plase_gray_price_6.place (x = 440, y=300, width = 125, height = 90 )
plase_gray_price_7 = Button (text = "Новость о\nновинке",bg="#ededed", bd=0, command=pressF);plase_gray_price_7.place (x = 580, y=300, width = 125, height = 90 )

# Кнопки top
Logo = Button(text = 'DeusNet', bg= '#0075d5',fg='#b8e5ff', bd='0', font=('Arial',12,'bold'),command=talisman) ; Logo.place(x=15,y=40)
poisk = Entry (bg='#b8e5ff',fg='#0075d5');poisk.place(x=110,y=35, height=40, width=230)
poisk.insert(0,'Поиск по магазину')
Compare = Button(text = 'Сравнить', bg= '#0075d5',fg='#252b59', bd='0', font=('Timesnewroman',12),command = com) ; Compare.place(x=400,y=40)
favorites = Button(text = 'Избранное', bg= '#0075d5',fg='#c90022', bd='0', font=('Timesnewroman',12),command = fav) ; favorites.place(x=500,y=40)
shopping_cart = Button(text = 'Корзина', bg= '#0075d5',fg='#65f208', bd='0', font=('Timesnewroman',12),command = shop) ; shopping_cart.place(x=625,y=40)


city = Combobox(window_2)   # Комбобокс
city['values'] = ("Санкт-Петербург", "Москва", "Лондон", "Париж", "Голуби", "Вверх", "Блики", "Крыш")  
city.current(0)  # вариант по умолчанию
city.place(x=10,y=2)

# Кнопки top_top
shops = Button(window_2,text = 'Магазины', bg= '#00b7ff',fg='black', bd='0', font=("Arial", 12), command=pressF) ; shops.place(x=200)
Buyers = Button(window_2,text = 'Покупателям', bg= '#00b7ff',fg='black', bd='0', font=("Arial", 12,'underline'), command=pressF) ; Buyers.place(x=290)
Partners = Button(window_2,text = 'Партнёрам', bg= '#00b7ff',fg='black', bd='0', font=("Arial", 12), command=pressF) ; Partners.place(x=400,)
Bonus_club = Button(window_2,text = 'Бонус клуб', bg= '#00b7ff',fg='black', bd='0', font=("Arial", 12), command=pressF) ; Bonus_club.place(x=500)
Number = Label(window_2,text = '+7-812-322-20-12 (с 6 до 18)', bg= '#00b7ff',fg='black', bd='0', font=("Arial", 12)) ; Number.place(x=600, y=5)

language = True #Язык :-)

myMenu = Menu(window_2)
window_2.config(menu = myMenu)
myMenu.add_command(label = 'Закрыть', command = window_2.destroy)
myMenu.add_command(label = 'English', command = rusEng)
myMenu.add_command(label = 'Русский', command = engRus)

with open('User.txt') as g: # Высвечивает первые 4 символа мыла
    datar=g.read()
    stroka= datar.split('\n')
    strochka = stroka[0].split('\t')
    g.close()
if len(strochka[0])<4:
    entry = Button (text = 'Вход', bg= '#0075d5',fg='white', bd='0', font=('Timesnewroman',12,'bold'), command=Choice); entry.place(x=750,y=40)
    if strochka[0]!='': # Сигнал, что кто-то залез в User и добавил строчку с 3- символами
        messagebox.showinfo('ОШИБКА!', 'Внесистемное внесение данных в User!')
    
else:
    s= strochka[0] # Замена "Вход" на 4 символа из логина
    entry = Button (text = s[0]+s[1]+s[2]+s[3], bg= '#0075d5',fg='white', bd='0', font=('Timesnewroman',12,'bold'), command=Choice); entry.place(x=750,y=40)
with open('User.txt','w') as g: # очистка User.txt
    g.close()
    
window_2.mainloop()
