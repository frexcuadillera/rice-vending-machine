def register_password():

#get password
    password_info = password.get()
#open file in write mode
    file = open(password_info, "w")
#write password
    file.write(password_info)
    file.close

    password_entry.delete(0,END)

    Label(administrator, text"Login Success", fg="green").pack()
    
