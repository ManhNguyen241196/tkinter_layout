# from tkinter import *
# from tkinter import messagebox


# # định nghĩa chương trình chính
# root = Tk()
# root.title("Window With a Title Bar")
# root.geometry("400x300")


# myListCheckBox = []

# My_frame = LabelFrame(root, text="This frame for checkbox", padx=5,pady=5)
# cb1 = IntVar()
# cb2= IntVar()
# cb3 = IntVar()

# def isChecked():
    
#     if (cb1.get() == 1) :
#         if(not ("cb1" in myListCheckBox) ):
#             myListCheckBox.append("cb1")
#         pass
#     if (cb2.get() == 1) :
#         if(not "cb2" in myListCheckBox ):
#             myListCheckBox.append("cb2")
#         pass
#     if (cb3.get() == 1) :
#         if(not "cb3" in myListCheckBox ):
#             myListCheckBox.append("cb3")
#         pass
    
#     if (cb1.get() == 0):
#         if("cb1" in myListCheckBox ):
#             myListCheckBox.remove("cb1")
#         pass
#     if (cb2.get() == 0):
#         if("cb2" in myListCheckBox ):
#             myListCheckBox.remove("cb2")
#         pass
#     if (cb3.get() == 0):
#         if("cb3" in myListCheckBox ):
#             myListCheckBox.remove("cb3")
#         pass

#     print(myListCheckBox)

# mycb1 = Checkbutton(My_frame, text="option 1", variable=cb1, onvalue=1, offvalue=0, command=isChecked)
# mycb2 =Checkbutton(My_frame, text="option 2", variable=cb2, onvalue=1, offvalue=0, command=isChecked)
# mycb3 =Checkbutton(My_frame, text="option 3", variable=cb3, onvalue=1, offvalue=0, command=isChecked)


# mycb1.pack()
# mycb2.pack()
# mycb3.pack()
# btn = Button(My_frame, text='Sleeping!', state=DISABLED, padx=20, pady=5)
# btn.pack()

# My_frame.pack()


# #vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
# root.mainloop()

from tkinter import *


def isChecked():
    myListCheckBox = [cb.get() for cb in checkboxes]
    if(1 in myListCheckBox):
        btn.config(state=NORMAL)
    print(myListCheckBox)

root = Tk()
root.title("Window With a Title Bar")
root.geometry("400x300")

My_frame = LabelFrame(root, text="This frame for checkbox", padx=5,pady=5)
checkboxes = []

for i in range(3):
    cb = IntVar()
    checkboxes.append(cb)
    Checkbutton(My_frame, text=f"option {i+1}", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()

btn = Button(My_frame, text='Sleeping!', state=DISABLED, padx=20, pady=5)
btn.pack()
My_frame.pack()

root.mainloop()
