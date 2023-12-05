from tkinter import *
from tkinter import filedialog
from pptx import Presentation

# định nghĩa chương trình chính
root = Tk()
root.title("Window With a Title Bar")
root.geometry("400x300")

def clickFunc():
    filename = filedialog.askopenfilename(initialdir ='C:/Users/ADMIN/Desktop/code/python/powerpoint/testPP', title="select a file powerpoint", filetypes=(("Powerpoint Files", "*.pptx"),("All Files", "*.*")))
    ppt = Presentation(filename)
   

    # Count the number of slides
    num_slides = len(ppt.slides)
    print(f'The presentation has {num_slides} slides.')
    myLabel = Label(root, text = filename)
    myLabel.grid(row=1,column=1)
    
# Print the result
myBtn = Button(root, text="chon file", command=clickFunc)
myBtn.grid(row=0,column=1)

#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()