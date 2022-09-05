from tkinter import *
import render

class App:
    def __init__(self, master):
        self.Help = Label(master,text="Введите название картинки с расширением:")
        self.FileName = Entry(master)
        self.FieldXHelp = Label(master,text="Масштаб по X (float):")
        self.XScale = Entry(master)
        self.FieldYHelp = Label(master,text="Масштаб по Y (float):")
        self.YScale = Entry(master)
        self.ScaleHelp = Label(master,text="Масштаб шрифта (int):")
        self.Scale = Entry(master)
        self.Start = Button(master,text="Преобразовать")
        self.text = Text()
        self.HowToUseHelp = Label(master,text="Помощь:\nпереместите в папку со скриптом картинку\nкажите ее имя с расширением в поле также выберете масштабы по осям\nнажмите преобразовать\nскопируйте результат из текстового поля")
        self.Help.pack()
        self.FileName.pack()
        self.FieldXHelp.pack()
        self.XScale.pack()
        self.FieldYHelp.pack()
        self.YScale.pack()
        self.ScaleHelp.pack()
        self.Scale.pack()
        self.Start.pack()
        self.text.pack()
        self.HowToUseHelp.pack()
        self.Start.bind('<Button-1>',self.Render)
    def Render(self,e):
        #try:
            self.text.delete(1.0, END)
            text = ""
            img = render.render(self.FileName.get(),float(self.XScale.get()),float(self.YScale.get()))
            for x in range(0,len(img[0])):
                for y in range(0,len(img)):
                    text += img[y][x]
                text += '\n'
            self.text.font=('Times New Roman',int(self.Scale.get()))
            self.text.insert(1.0,text)
        #except Exception:
            #print('Это что ещё такое?')

root = Tk()
root.title("PicToText")
root.geometry("1000x1000")
app = App(root)
root.mainloop()
