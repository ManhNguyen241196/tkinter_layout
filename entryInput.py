from tkinter import *

# định nghĩa chương trình chính
root = Tk()

inputText = Entry(root,  bd=3)
inputText.grid(row=0,column=0)
inputText.insert(0,"checked")


def printText():
    myLabel = Label(root, text = inputText.get())
    myLabel.grid(row=2,column=0)

submitBtn = Button(root, text="Submit",
                  activebackground='#78d6ff',
                  activeforeground='#ff0000',
                  command=printText)
submitBtn.grid(row=1,column=0)
#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()