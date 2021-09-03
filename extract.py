from tkinter import *
import PyPDF2
from tkinter import filedialog
#clear textbox
def clear_text_box():
    my_text.delete(1.0, END)
#Open pdf
def open_pdf():
    #grab the filename of pdf
    open_file = filedialog.askopenfilename(
        initialdir="file:///home/lindokuhle/pdf_app/",
        title="open PDF",
        filetypes=(
            ("PDF File","*.pdf"),
            ("all files","*.*")))
    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)
        page = pdf_file.getPage(3)
        page_stuff= page.extractText()
        my_text.insert(1.0,page_stuff)

root = Tk()
#Create a texbook
my_text = Text(root)
my_text.pack()
#create a Menu
my_Menu = Menu(root)
root.config(menu=my_Menu)
#add to menu
file_menu = Menu(my_Menu,tearoff=False)
my_Menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="open",command=open_pdf)
file_menu.add_command(label="clear text",command=clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)


root.mainloop()
