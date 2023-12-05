from tkinter import *
from tkinter import messagebox

# định nghĩa chương trình chính
root = Tk()
root.title("Window With a Title Bar")
root.geometry("400x300")


def printMessage():
    messagebox.showinfo(title="show mess", message=var.get())
 
#define element
My_frame = LabelFrame(root, text="This frame for choice method check ...", padx=5,pady=5)
var = IntVar()
var.set(1) 
label = Label(My_frame)
myBtn = Button(My_frame, text="mybtn", command=printMessage)

def sel():
    if(var.get() == 1):
        selection = "You selected the option co value 1"
    if(var.get() == 2):
        selection = "You selected the option co value 2"
    if(var.get() == 3):
        selection = "You selected the option co value 3"
    label.config(text = selection)
    label.pack()
    
    
R1 = Radiobutton(My_frame, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(My_frame, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(My_frame, text="Option 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)
# label.pack()

#layout Element
My_frame.grid(row=4,column=0)
myBtn.pack()



#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()