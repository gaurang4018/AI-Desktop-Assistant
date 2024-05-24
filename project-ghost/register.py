#  Register a new user
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
import pymysql
import ast


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)

def connectdb():
    if emailEntry.get()=="" or usernameEntry.get()=="" or passwordEntry.get()=="" or confirmpasswordEntry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif emailEntry.get().find("@")==-1 or emailEntry.get().find(".com")==-1:
        messagebox.showerror("Error","Invalid Email")        
    elif passwordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror("Error","Password and Confirm Password must be same")    
    elif len(passwordEntry.get())<5:
        messagebox.showerror("Error","Password must be at least 5 characters")
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password='2003')    
            mycursor = con.cursor()
        except:
            messagebox.showerror("Database connectivity error","Please try again later")
            return           

        try:
            query = "create database ghost"
            mycursor.execute(query)
            query = "use ghost"
            mycursor.execute(query)
            query = "create table userinfo(id int auto_increment primary key not null ,email varchar(50),username varchar(50),password varchar(20))"
            mycursor.execute(query)
            
        except:
            mycursor.execute("use ghost")
        
        query = "select * from userinfo where username=%s"
        mycursor.execute(query,(usernameEntry.get()))
        
        row = mycursor.fetchone()
        
        if row!=None:
            messagebox.showerror("Error","Username already exists")
            return
        
        else:
            query = "insert into userinfo(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            
            messagebox.showinfo("Success","Account created successfully")
            clear()
            register_window.destroy()
            import login
        

def login_page():
    register_window.destroy()
    import login

register_window = Tk()


register_window.resizable(False, False)
register_window.title("SignUp")
register_window.geometry("890x500+300+200")
register_window.config(bg="white")


bgimage = ImageTk.PhotoImage(file="res//l.png")
bglabel = Label(register_window , image=bgimage,border = 0,bg="white")
bglabel.place(x=0, y=0)

# # app name
# heading = Label(register_window, text="  Ghost  \nAI Desktop Assistant", font=("Brush Script MT ",20, "bold","italic" ), bg="white", fg="#5711f8")
# heading.place(x=100, y=60)


# frame
frame = Frame(register_window,bg="white",width=400,height=400,bd=0)
frame.place(x=490, y=30)

# email
heading = Label(frame, text="Create an Account", font=("Microsoft Yahei UI Light", 23, "bold"), bg="white", fg="#5711f8")
heading.grid(row=0, column=0, padx=20, pady=20)


emailLabel = Label(frame, text="Email", font=("Microsoft Yahei UI Light", 12, "bold"), bg="white", fg="#5711f8")
emailLabel.grid(row=1, column=0, sticky=W , padx=25)

emailEntry = Entry(frame, font=("Microsoft Yahei UI Light", 12), bg="#5711f8", fg="white" , width=25)   
emailEntry.grid(row=2, column=0, sticky=W , padx=25)



# username
usernameLabel = Label(frame, text="Username", font=("Microsoft Yahei UI Light", 12, "bold"), bg="white", fg="#5711f8")
usernameLabel.grid(row=3, column=0, sticky=W , padx=25,pady=(10,0))

usernameEntry = Entry(frame, font=("Microsoft Yahei UI Light", 12), bg="#5711f8", fg="white" , width=25)   
usernameEntry.grid(row=4, column=0, sticky=W , padx=25)

# password
passwordLabel = Label(frame, text="Password", font=("Microsoft Yahei UI Light", 12, "bold"), bg="white", fg="#5711f8")
passwordLabel.grid(row=5, column=0, sticky=W , padx=25,pady=(10,0))

passwordEntry = Entry(frame, font=("Microsoft Yahei UI Light", 12), bg="#5711f8", fg="white" , width=25)   
passwordEntry.grid(row=6, column=0, sticky=W , padx=25)
passwordEntry.config(show="*")

# password
confirmpasswordLabel = Label(frame, text="Confirm Password", font=("Microsoft Yahei UI Light", 12, "bold"), bg="white", fg="#5711f8")
confirmpasswordLabel.grid(row=7, column=0, sticky=W , padx=25,pady=(10,0))

confirmpasswordEntry = Entry(frame, font=("Microsoft Yahei UI Light", 12), bg="#5711f8", fg="white" , width=25)   
confirmpasswordEntry.grid(row=8, column=0, sticky=W , padx=25)
confirmpasswordEntry.config(show="*")

# submit button 
registerBtn = Button(frame, text="Create new Account", font=("Open Sans", 12, "bold"), bg="#5711f8", fg="white", activebackground="#5711f8",activeforeground="white",width=17,height=1, bd=0, cursor="hand2",pady=10,command=connectdb)
registerBtn.grid(row=9, column=0, padx =(50,0),pady=(20,0),sticky=W)


# login link
loginLink = Button(frame, text="Already have an Account ?\n Login", font=("Open Sans", 10, "bold"), bg="white", fg="#5711f8", bd=0, activeforeground="#5711f8",activebackground="white",cursor="hand2",border=0,command=login_page)
loginLink.grid(row=10, column=0, padx=(50,0), pady=15,sticky=W)


register_window.mainloop()