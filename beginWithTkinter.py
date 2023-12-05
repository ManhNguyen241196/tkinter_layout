from tkinter import *
from tkinter import font
# định nghĩa chương trình chính
root = Tk()
root.geometry("400x200")

#dinh nghĩa font chu
label_font = font.Font(size=9)
label_font2 = font.Font(size=18)


 #step1 : tao 1 element --------------------
myLabel = Label(root, anchor=E, font=label_font, bg='green',text="helloooooooooooo").grid(row=0,column=0) #có the grid ngay truc tiep dẻ dinh nghia vị tri tren screen
myLabel2 = Label(root, anchor=E, font=label_font, bg='blue',text="hi great").grid(row=0,column=3) 
myLabel3 = Label(root, anchor=E, font=label_font2, bg='red',text="check").grid(row=1,column=0)  

 #step2 : đóng gói ele và đưa element lên windown--------------------
# myLabel.pack()



#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()