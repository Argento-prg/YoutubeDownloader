import tkinter as tk
import getVideo

class GraphicForm:
    #дефолтный статус
    status = 0
    #конструктор
    def __init__(self):
        self.myWindow = tk.Tk()
        self.myWindow.title('YoutubeDownloader')
        self.myWindow.geometry('200x200')
        self.createForm()
    #заполнение элементами окна программыф
    def createForm(self):
        #окно ввода
        self.linkInputField = tk.Entry(self.myWindow)
        self.linkInputField.grid(column=0, row=0)
        #статус выполнения
        self.statusLabel = tk.Label(self.myWindow, text='Ожидание ввода')
        self.statusLabel.grid(column=0, row=1)
        #кнопка для начала выполнения
        self.startButton = tk.Button(
            self.myWindow, 
            text='Загрузить', 
            command=self.startProcess
        )
        self.startButton.grid(column=0, row=2)
    
    def startProcess(self):
        self.statusLabel.config(text='Загрузка')
        linkVideo = str(self.linkInputField.get())
        (status, errVideo) = getVideo.getVideo(linkVideo)
        if status == -1:
            self.statusLabel.config(text=errVideo)
        else:
            self.statusLabel.config(text='Успешно')


    #функция старта
    def start(self):
        self.myWindow.mainloop()
