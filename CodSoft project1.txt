from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("To-Do-List")
root.geometry("925x500+300+200")
root.state("zoomed")
root.configure(bg="white")

def signin():
    username=user.get()
    password=code.get()
    if username=='admin' and password=='1234':
        new=Toplevel(root)
        new.title("To-Do-List")
        new.geometry("925x500+300+200")
        new.state("zoomed")
        new.configure(bg="white")
        wel=Label(new,text="WELCOME",bg='white',fg='blue',font=('Fort',40,'bold'))
        wel.place(x=550,y=50)

        txt=Label(new,text="Enter Task:",bg='white',fg='blue',font=('Fort',20,'bold'))
        txt.place(x=250,y=150)

        task_field =Entry(new,border=3)
        task_field.place(x=420,y=160,width=600,height=25)

        frm=Frame(new,width=900,height=70,bg='white',border=6)
        frm.place(x=200,y=200)

        def addtask():
                task =task_field.get()
                todo_list.append(task)
                task_field.delete(0, END)
                to_do_listbox.insert(END, task)


        add_task_button =Button(frm, text="Add ", command=addtask,border=3,font=('Fort',10,'bold'))
        add_task_button.place(x=150,y=10,width=90,height=40)

        todo_list = []
        def delete_item():
            index = to_do_listbox.curselection()
            if index != ():
                todo_list.pop(index[0])
                to_do_listbox.delete(index[0])
        delete_button = Button(frm, text='Delete', command=delete_item,border=4,font=('Fort',10,'bold'))
        delete_button.place(x=280,y=10,width=90,height=40)

        def update_item():
            index = to_do_listbox.curselection()
            if index != ():
                task = task_field.get()
                todo_list[index[0]] = task
                to_do_listbox.delete(index[0])
                to_do_listbox.insert(index[0], task)
                task_field.delete(0, 'end')

        update_button = Button(frm, text='Update', command=update_item,border=5,font=('Fort',10,'bold'))
        update_button.place(x=410,y=10,width=90,height=40)

        def clear_list():
            todo_list.clear()
            to_do_listbox.delete(0, 'end')

        clear_button =Button(frm, text='Clear', command=clear_list,border=5,font=('Fort',10,'bold'))
        clear_button.place(x=550,y=10,width=90,height=40)

        def close():
            new.destroy()

        close_button =Button(frm, text='close', command=close,border=5,font=('Fort',10,'bold'))
        close_button.place(x=680,y=10,width=90,height=40)
    
        frm1=Frame(new,width=2000,height=900,bg='white',border=6)
        frm1.place(x=000,y=270)

        to_do_listbox =Listbox(frm1)
        to_do_listbox.place(x=00,y=00,width=2000,height=900)

        new.mainloop()




img=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\login1.png')
img1=Label(root,image=img,bg="white")
img1.place(x=100,y=100,width=450,height=500)

frame=Frame(root,width=500,height=500,bg='white')
frame.place(x=550,y=110)

h1=Label(frame,text="Sign in",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
h1.place(x=190,y=10)
def on_enter(e):
        user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft Yahei UI Light",11))
user.place(x=100,y=100)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind("<FocusOut>",on_leave)

def on_enter(e):
        code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
         code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft Yahei UI Light",11))
code.place(x=100,y=180)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind("<FocusOut>",on_leave)

##code.config(show="*")
f2=Frame(frame,width=295,height=2,bg='black')
f2.place(x=100,y=200)
f2=Frame(frame,width=295,height=2,bg='black')
f2.place(x=100,y=120)

b1=Button(frame,width=39,pady=7,text="Sign in",bg='white',fg="black",border=0,command=signin)
b1.place(x=100,y=230)

l1=Label(frame,text="Don't have a account?",fg="Black",bg="white",font=("Microsoft Yahei UI Light",11))
l1.place(x=100,y=260)

b1=Button(frame,width=6,text="sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=None)
b1.place(x=260,y=260)







root.mainloop()
