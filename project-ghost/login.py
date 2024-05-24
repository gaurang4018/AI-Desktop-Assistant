#  Login form
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
import pymysql



def login():
    if usernameEntry.get() == '' or passwordEntry.get()=="":
        messagebox.showerror("Error", "All fields are required")

    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="2003")
            mycursor = con.cursor()
        except:
            messagebox.showerror("Database connectivity error","Please try again later")
            return  
        mycursor.execute("use ghost")
        query = "select * from userinfo where username=%s and password=%s"
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid Username or Password")
            return
        else:
            messagebox.showinfo("Success","Login Successful")
            login_window.destroy()
            import ghost



def register_page():
    login_window.destroy()
    import register

login_window = Tk()


login_window.resizable(False, False)
login_window.title("Login")
login_window.geometry("850x480+200+50")
login_window.config(bg="white")

# image
bgimage = ImageTk.PhotoImage(file="res//l.png",width=400,height=400)
bglabel = Label(login_window, image=bgimage,bg="white")
bglabel.place(x=0, y=-10)

# # app name
# heading = Label(login_window, text="  Ghost  \nAI Desktop Assistant", font=("Brush Script MT ",20, "bold","italic" ), bg="white", fg="#5711f8")
# heading.place(x=100, y=60)

# frame
frame = Frame(login_window,bg="white",width=400,height=400,bd=0)
frame.place(x=490, y=30)

heading = Label(frame, text="User Login", font=("Microsoft Yahei UI Light", 25, "bold"), bg="white", fg="#5711f8")
heading.grid(row=0, column=0, padx=10, pady=30)

# username
usernameEntry = Entry(frame,width=25,font=("Microsoft Yahei UI Light", 13, "bold"),bd=0,fg="#5711f8")
usernameEntry.grid(row=1,column=0 ,padx=10,pady=10)
usernameEntry.insert(0, "Username")
usernameEntry.bind('<FocusIn>', lambda args: usernameEntry.delete('0', 'end'))

frame1 = Frame(frame, width=250, height=2, bg="#5711f8")
frame1.grid(row=2, column=0, padx=10, pady=(0,20)) 


# password
passwordEntry = Entry(frame,width=25,font=("Microsoft Yahei UI Light", 13, "bold"),bd=0,fg="#5711f8")
passwordEntry.grid(row=3,column=0 ,padx=10,pady=10)
passwordEntry.insert(0, "Password")
passwordEntry.bind('<FocusIn>', lambda args: passwordEntry.delete('0', 'end'))

frame2 = Frame(frame, width=250, height=2, bg="#5711f8")
frame2.grid(row=4, column=0, padx=10, pady=(0,20))
passwordEntry.config(show="*")

# submit btn
loginBtn = Button(frame, text="Login", font=("Open Sans", 17, "bold"), bg="#5711f8", fg="white", bd=0, width=15, height=1,activeforeground="white",activebackground="#5711f8",cursor="hand2",border=0,command=login)
loginBtn.grid(row=5, column=0, padx=10, pady=30)


# Link
registerlink = Button(frame, text="Dont have an Account ? \nCreate an Account", font=("Open Sans", 12, "bold"), bg="white", fg="#5711f8", bd=0, width=20, height=2,activeforeground="#5711f8",activebackground="white",cursor="hand2",border=0,command=register_page)
registerlink.grid(row=6, column=0, padx=10, pady=10)



login_window.mainloop()









