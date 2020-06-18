from tkinter import *



root = Tk() # tk- базовый класс
root.title("Ня, Кавай") # Название окна
root.geometry('512x512+0+0')
root.resizable(True,True)
root.config(background='yellow')

canv = Canvas (root, width=340, height=370, bg = 'lightblue')
canv.pack()

# Border of oval

x = 10
while x<330:
    canv.create_oval (x, 10, x+20, 30,fill='black')
    x=x+30


y = 10
while y<360:
    canv.create_oval (10, y, 30, y+20,fill='black')
    y=y+30

x = 10
while x<330:
    canv.create_oval (x, 340, x+20, 360,fill='black')
    x=x+30

y = 10
while y<360:
    canv.create_oval (310, y, 330, y+20,fill='black')
    y=y+30


canv.create_oval([90, 100], [230,240],fill='#777777') # Head

canv.create_polygon([105,140],[100,70],[150,110],fill='#777777', outline='black', width=2) # Left uho
canv.create_polygon([115,130],[105,80],[137,113],fill='#000')
canv.create_line(105,140,150,110, fill='#777777', width=2)

canv.create_polygon([215,140],[220,70],[170,110],fill='#777777', outline='black', width=2) # Right uho
canv.create_polygon([205,130],[215,80],[180,113],fill='#000')
canv.create_line(215,140,170,110, fill='#777777', width=2)

canv.create_arc([120,140],[150,170],fill='#FFF',extent=180) # Left eye
canv.create_arc([125,145],[145,165],fill='#00F',extent=180)
canv.create_arc([130,150],[140,160],fill='#000',extent=180)

canv.create_arc([170,140],[200,170],fill='#FFF',extent=180) # Right eye
canv.create_arc([175,145],[195,165],fill='#00F',extent=180)
canv.create_arc([180,150],[190,160],fill='#000',extent=180)

canv.create_polygon([150,170],[170,170],[160,180],fill='#000') # Nos triangle

#canv.create_arc([135,185],[160,215],fill='#F11',extent=180, start=180) # Das alter_maul 

canv.create_arc([130,165],[160,195], outline='#F11',extent=180, start=180, style= ARC, width=2) # Das maul
canv.create_arc([190,165],[160,195], outline='#F11',extent=180, start=180, style= ARC, width=2)
#canv.create_arc([150,208],[170,188],fill='#F11',extent=180, start=180) # Language

canv.create_line (120,170,60,145, fill='#000', width=1) #Left usi
canv.create_line (118,180,40,175, fill='#000', width=1)
canv.create_line (125,190,75,205, fill='#000', width=1)

canv.create_line (200,170,260,145, fill='#000', width=1) #Right usi
canv.create_line (198,180,280,175, fill='#000', width=1)
canv.create_line (200,190,245,205, fill='#000', width=1)

canv.create_oval ([130,80],[190,102],fill='#000') # Cilinder
canv.create_polygon([140,90],[130,50],[190,50],[180,90],fill='#000')
canv.create_oval ([130,40],[190,60],fill='#444')

canv.create_line (150,101,150,125, fill='#000', width=2) # Lob line
canv.create_line (160,100,160,130, fill='#000', width=2)
canv.create_line (170,101,170,123, fill='#000', width=2)

canv.create_polygon([150,215],[170,215],[160,225],fill='#000') # tie (if not language)
canv.create_polygon([160,225],[148,255],[160,270],[172,255],fill='#000')

# Надпись : Почему? Во славу Коти, конечно же
canv.create_text(165,300, text='Why? \n For the glory of Catan, of course', font='Times_new_Roman 13', anchor='c', justify= CENTER)

myMenu=Menu(root)
root.config(menu=myMenu)
myMenu.add_command(label='Закрыть',command=root.destroy)

root.mainloop()
