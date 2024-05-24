import tkinter
from tkinter import filedialog
import os
from tkinter import *
import asyncio
import pyttsx3
from time import sleep


def speak(audio):
    engine =  pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("rate",180)
    engine.say(audio)
    engine.runAndWait()

async def browse_folder():
    folder_path = filedialog.askdirectory()
    selected_folder.config(text=folder_path)
    
    await asyncio.sleep(0.1)
    selected_folder.update()
    print(selected_folder.cget("text"))
    print(os.listdir(selected_folder.cget("text")))
    
    if folder_path == "No folder selected":
        return
    files = os.listdir(folder_path)

    files_list.delete(0, END)
    for file in files:
        files_list.insert(END, f" : {file}")
    await asyncio.sleep(0.1)
    files_list.update() 


# selected item fun
def selectedItem():
    # get the selected item
    selected_item = files_list.curselection()
    # get the text of the selected item
    selected_item_text = files_list.get(selected_item)
    # remove the colon from the text
    selected_item_text = (selected_item_text[2:])
    selected_item_text = selected_item_text.replace(" ","")
    selected_item_path = str(selected_folder.cget("text")+"//"+selected_item_text)
    # print(selected_item_path)
    return selected_item_path
     

# rename fun
def renameFile():
    # get the path of the selected item
    selected_item_path = selectedItem()
    # get the new name of the file
    new_name = renameInput.get()
    # get the extension of the file
    extension = os.path.splitext(selected_item_path)[1]
    new_path = str(selected_folder.cget("text")+"//"+new_name+extension)
    try:
        # rename the file
        os.rename(selected_item_path, new_path)
        # update the listbox
        files = os.listdir(selected_folder.cget("text"))
        files_list.delete(0, END)
        for file in files:
            files_list.insert(END, f" : {file}")
        # clear the rename input
        renameInput.delete(0, END)
        speak("File renamed")
        # disable the rename button
        renameButton.config(state=DISABLED)
    except:
        speak("Sorry! Try again")    
        # apply logo to right frame
    
    
    sleep(1)
    logo = PhotoImage(file="res//logo.gif")
    renameButton.place_forget()
    renameInput.place_forget()
    selected_folder.place_forget()
    files_list.place_forget()
    
    logoLabel = Label(rightFrame,image=logo,width=700,height=500,bg="#15202b")
    logoLabel.pack()
        
# delete fun
def deleteFile():    
    # get the path of the selected item
    selected_item_path = selectedItem()
    try:
        # delete the file
        os.remove(selected_item_path)
        # update the listbox
        files = os.listdir(selected_folder.cget("text"))
        files_list.delete(0, END)
        for file in files:
            files_list.insert(END, f" : {file}")
        # disable the delete button
        deleteButton.config(state=DISABLED)
        speak("File deleted")
    except:
        speak("Sorry! Try again") 

    sleep(1)
    logo = PhotoImage(file="res//logo.gif")
    deleteButton.place_forget()
    renameInput.place_forget()
    selected_folder.place_forget()
    files_list.place_forget()
    
    logoLabel = Label(rightFrame,image=logo,width=700,height=500,bg="#15202b")
    logoLabel.pack()
    
#  exit fun
def exit():
    # forcefully exit the program
    root.destroy()

    
        
root = Tk()
root.title("Ghost")
root.resizable(False,False)
root.geometry("800x500")


# framing the left and right frame
leftFrame = Frame(root, width = 200,height=500 ,bg="#f2f0e4",bd=0,relief="sunken")
rightFrame = Frame(root,height=500,width=700,bg="cyan",bd=0,relief="sunken")
leftFrame.pack(side=LEFT)
rightFrame.pack(side=RIGHT)


# right frame section
# logo
logo = PhotoImage(file="res//logo.gif")
logoLabel = Label(rightFrame,image=logo,width=700,height=500,bg="#15202b")
logoLabel.pack()


# title section
labelName = Label(leftFrame,text="Ghost",font=("Tahoma", 30),bg="#f2f0e4",fg="#15202b",width=8,height=1,justify="center",anchor="center")
labelName.place(x=5,y=0)
labelName.config(pady=20)

# description section
labelDesc = Label(leftFrame,text="An AI \nDesktop\n Assistant",font=("Tahoma", 20,"bold"),fg="#f2f0e4", justify="center",background="#1c1c1e",width=12,height=7,anchor="center")
labelDesc.place(x=0,y=100)

# Buttons section
# browse files button
button2 = Button(leftFrame,text="Browse Files",font=("Tahoma", 15),fg="#1c1c1e", justify="center",background="#00ACEE",width=13,height=1 ,anchor="center",cursor="hand2",command=lambda: asyncio.run(browse_folder()))
button2.place(x=20,y=400)

# exit button
button3 = Button(leftFrame,text="Exit",font=("Tahoma", 15),fg="#fff", justify="center",background="#ff2500",width=13,height=1 ,anchor="center",cursor="hand2",command=exit)
button3.place(x=20,y=450)



# Right frame section 
#  file operations section
# create a label to display the selected folder
selected_folder = Label(rightFrame, text="No folder selected", font=("Tahoma", 13),bg="#f2f0e4",fg="#15202b",width=60,height=2,justify="center",anchor="center",bd=0,highlightthickness=0 )
# selected_folder.place(x=20,y=50)


# rename GUI
renameInput = Entry(rightFrame,font=("Tahoma", 15),fg="#1c1c1e", justify="center",background="#f2f0e4",width=35)
# renameInput.place(x=20,y=95)
renameInput.config(highlightthickness=0,highlightbackground="#f2f0e4",highlightcolor="#f2f0e4",bd=0)

# add a placeholder text to the entry
renameInput.insert(0, "Enter new name for the file")
# remove the placeholder text when the user clicks on the entry
renameInput.bind("<Button-1>", lambda event: renameInput.delete(0, "end"))
# add the placeholder text back if the user leaves the entry empty
renameInput.bind("<FocusOut>", lambda event: renameInput.insert(0, "Enter new name for the file") if len(renameInput.get()) == 0 else None)


# rename button
renameButton = Button(rightFrame,text="rename file",font=("Tahoma", 10,"bold"),fg="#fff", justify="center",background="#15202b",width=10,height=1 ,cursor="hand2" ,command=lambda: renameFile())
# renameButton.place(x=420,y=93)
# deactivate the button by default
renameButton.config(state=DISABLED)


# delete button
deleteButton = Button(rightFrame,text="delete file",font=("Tahoma", 10,"bold"),fg="#fff", justify="center",background="#ff2500",width=10,height=1 ,cursor="hand2" ,command=lambda: deleteFile())
# deleteButton.place(x=420,y=93)
deleteButton.config(state=DISABLED)
 
    
# files list box 
files_list = Listbox(rightFrame, height=20, width=80, font=("Helvetica", 10),bd=0,highlightthickness=0)
# files_list.place(x=20,y=140)
files_list.config(bg="black",fg="white")


# root.mainloop()