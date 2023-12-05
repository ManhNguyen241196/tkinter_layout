from tkinter import *



# định nghĩa chương trình chính
root = Tk()
# myLabel2 = Label(root, anchor=E,  bg='blue',text="hi great")

i=1

def callback():
    global i
    i=i+1
    myLabel2 = Label(root, anchor=E,  bg='blue',text="hi great")
    myLabel2.grid(row=i,column=0)
    print(0)
    myButton.flash()  # nhap nhay nut giua trang thai active và non-active
    # myButton.config(state=DISABLED,padx=10,pady=10) 
    
myButton = Button(root, text="click me",
                  activebackground='#78d6ff',
                  activeforeground='#ff0000',
                  command=callback)
myButton.grid(row=0,column=0)

#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()