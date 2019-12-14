import tkinter



#Callback funk
def deleteMessage():
    print("Your message sucks major balls so we deleted it")
def down():
    print("Going DOWN bitches")
def up():
    print("UP a.k.a ENZO is CHONK")




#Make a window
window = tkinter.Tk()



#Adding the buttons
delete_message = tkinter.Button(window, text = "Delete message", command = deleteMessage, bg = 'purple')
down_button =  tkinter.Button(window, text = "DOWN", command = down, bg = 'red')
up_button = tkinter.Button(window, text = "UP", command = up, bg = 'green')



#This one shows the messages
Lb = tkinter.Listbox(window)
Lb.insert(1, "M1")
Lb.insert(2, "M2")
Lb.insert(3, "M3")



#this is the other one
def onclick():
   pass
text = tkinter.Text(window)
text.insert(tkinter.INSERT, "Hello.....")
text.insert(tkinter.END, "Bye Bye.....")
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")



#Pack order
Lb.pack()
down_button.pack()
up_button.pack()

delete_message.pack()

text.pack()

#Doing the thing
window.mainloop()
