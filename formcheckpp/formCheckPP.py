from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter as tk

#sample function
def run_with_method_1():
    print("form da chọn la: 1" )
def run_with_method_2():
    print("form da chọn la: 2" )

def func0():
    print("Chaỵ func check  giá trị của # trong các silde")
def func1():
    print("Check tên trong slide menu")




# định nghĩa chương trình chính
root = Tk()
root.title("Window With a Title Bar")
root.geometry("700x400")
# root.resizable(False,False)


def load_checkboxes(checkboxes):
    for index, ele in enumerate(checkboxes):
        if ele == 1:
            if index == 0:
                func0()
            elif index == 1:
                func1()
            
#Button run function
def printMessage():
    sel()
    load_checkboxes(listCheckBoxRender)
    messagebox.showinfo(title="show mess", message=var.get())
 
#define element
frame_form = LabelFrame(root, text="Chọn form powerpoint để check", padx=5,pady=5, font=('Arial', 10, 'bold'))
frame_method = LabelFrame(root, text="Chọn hạng mục check", padx=5,pady=5, font=('Arial', 10, 'bold'))
frame_image = LabelFrame(root, text="Preview form pp", padx=5,pady=5, font=('Arial', 10, 'bold'))                  
label = Label(frame_form)  # vi du de check selection form


#---------------------creat lable empty
def creat_space_grid_y(grid_y, num_space):
    label_space = Label(root, text=f'{" "*num_space}')
    label_space.grid(row=4,column=grid_y)
    
def creat_space_grid_x(grid_x):
    label_space = Label(root, text=" ")
    label_space.grid(row=grid_x,column=1)
#----------------------------------


#--------------------selection form
var = IntVar()
var.set(1) 
def sel():
    if(var.get() == 1):
        run_with_method_1()     
    if(var.get() == 2):
        run_with_method_2()


#show photo preview
label_image = Label(frame_image)
def image( link_img):
    python_image = PhotoImage(file=link_img)
    original_image = python_image.subsample(3,3)
    label_image.config(image=original_image)
    label_image.image = original_image
    label_image.pack(fill=BOTH, expand=1)
image('C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy.png') #xuat hien ban dau mac dinh la 1
def showImg():
    Link = ''
    if(var.get() == 1):  
        Link = 'C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy.png'
        image ( Link)
    if(var.get() == 2):   
        Link = 'C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy_table.png'
        image ( Link)
    print(Link)

R1 = Radiobutton(frame_form, text="Form battery chứa dạng #x:xxx[MPa]", variable=var, value=1, command= showImg)
R1.pack( anchor = W )
R2 = Radiobutton(frame_form, text="Form chứa bảng", variable=var, value=2, command= showImg)
R2.pack( anchor = W )
# label.pack()
#----------------------------------





#------------------- checkbox form
listCheckBoxRender = []
def isChecked():
    myListCheckBox = [cb.get() for cb in checkboxes]
    if(1 in myListCheckBox):
        myBtn.config(state=NORMAL)
    print(myListCheckBox)
    global listCheckBoxRender
    listCheckBoxRender=myListCheckBox

checkboxes = []
for i in range(2):
    cb = IntVar()
    checkboxes.append(cb)
    if(i ==0):       
        Checkbutton(frame_method, text=f"Check giá trị #", variable=cb, onvalue=1, offvalue=0,command=isChecked).pack( anchor = W)
    if(i ==1):       
        Checkbutton(frame_method, text=f"Check chỉ vị trí chi tiết", variable=cb, onvalue=1, offvalue=0,command=isChecked).pack( anchor = W)
#----------------------------------

#------------------- Button Run form
myBtn = Button(root, text="RUN",state=DISABLED, activebackground='green',padx=8,pady=8, command=printMessage)
myBtn.flash()

#----------------------------------
#layout Element
creat_space_grid_y(2, 20)
creat_space_grid_y(0, 5)
creat_space_grid_x(0)
creat_space_grid_x(4)

frame_method.grid(row=1,column=1)
frame_form.grid(row=1,column=3)
frame_image.grid(row=5,column=3)
myBtn.grid(row=5,column=1)
 
#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()
