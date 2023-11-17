from tkinter import *
from tkinter import messagebox
new=Tk()
new.title("Contact Book")
new.geometry("925x500+300+200")
new.state("zoomed")
new.configure(bg="white")
wel=Label(new,text="Contact Book",bg='white',fg='blue',font=('Fort',40,'bold'))
wel.place(x=500,y=50)

name_label =Label(new, text="Name:",bg='white',fg='blue',font=('Fort',25,'bold'))
name_label.place(x=330,y=150)
name_entry =Entry(new, width=10,border=3,font=('Fort',20,'bold'))
name_entry.place(x=450,y=160,width=400,height=30)

phone_label =Label(new, text="Phone:",bg='white',fg='blue',font=('Fort',25,'bold'))
phone_label.place(x=330,y=250)
phone_entry =Entry(new,border=3,font=('Fort',20,'bold'))
phone_entry.place(x=450,y=260,width=400,height=30)

frm=Frame(new,width=1000,height=70,bg='white',border=6)
frm.place(x=200,y=300)

contacts = []

def add_contact():
        name =name_entry.get()
        phone =phone_entry.get()

        if name and phone:
            contact_info = f"{name}: {phone}"
            contacts.append(contact_info)
            contacts_listbox.insert(END, contact_info)
            name_entry.delete(0, END)
            phone_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")


add_button =Button(frm, text="Add Contact", command=add_contact)
add_button.place(x=150,y=10,width=90,height=40)

def delete_contact():
        selected_index = contacts_listbox.curselection()
        if selected_index:
            contacts_listbox.delete(selected_index)
            contacts.pop(selected_index[0])
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

delete_button =Button(frm, text="Delete Contact", command=delete_contact)
delete_button.place(x=280,y=10,width=90,height=40)

def clear_list():
            contacts.clear()
            contacts_listbox.delete(0, 'end')

clear_button =Button(frm, text='Clear', command=clear_list,font=('Fort',10,'bold'))
clear_button.place(x=410,y=10,width=90,height=40)

def close():
        new.destroy()

close_button =Button(frm, text='close', command=close,font=('Fort',10,'bold'))
close_button.place(x=550,y=10,width=90,height=40)
    
contacts_listbox =Listbox(new)
contacts_listbox.place(x=00,y=400,width=2000,height=1000)

new.mainloop()
