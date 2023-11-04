from random import *
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for _ in range(randint(3,4))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]

    password_list=password_letter+password_symbols+password_numbers
    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_my_password():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()
    new_data={
        website:{
        "email":email,
        "password":password,
    }
    }

    if len(website_entry.get())==0:
        messagebox.showerror(title="Validation Error", message="Put your Website Name")
    elif len(email_entry.get())==0:
        messagebox.showerror(title="Validation Error", message="Put your Email")
    elif len(password_entry.get())==0:
        messagebox.showerror(title="Validation Error", message="Password cannot be blank")
    else:
        try:
            with open("data.json", "r") as f:
                # read old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json","w")as f:
                json.dump(new_data,f,indent=4)
        else:
            # update old data with new
            data.update(new_data)



            with open("data.json", "w") as f:
                json.dump(data,f,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()



# ---------------------------- Find Password ------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="NO File", message="Create File first")
        website_entry.delete(0,END)
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"email:{email}\n password:{password}")
            website_entry.delete(0, END)
        else:
            messagebox.showinfo(title="Error", message=f"NO details for {website}")
            website_entry.delete(0,END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

#image creation
canvas=Canvas(width=200,height=180,bg="white",highlightthickness=0)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

#website label and entrys
website_label=Label(text="Website:",bg="white")
website_label.grid(row=1,column=0)


website_entry=Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

website_button=Button(text="Search",width=8,command=find_password)
website_button.grid(row=1,column=2)
#email/username label and entrys
email_label=Label(text="Email/Username:",bg="white")
email_label.grid(row=2,column=0)

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"tenzin@gmail.com")

#password label and entrys
password_label=Label(text="Password:",bg="white")
password_label.grid(row=3,column=0)

password_entry=Entry(width=21, )
password_entry.grid(row=3,column=1)

#buttons
generate_password=Button(text="Generate Password",bg="white",command=generate_password)
generate_password.grid(row=3,column=2)

add_button=Button(text="Add",width=36,bg="white",command=save_my_password)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()
