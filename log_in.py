from tkinter import *
win=Tk()
txt=Entry(win,width=10)
txt.grid(column=2,row=1,ipadx=70)
txt1=Entry(win,width=10)
txt1.grid(column=2,row=3,ipadx=70)

win.title("SignIn(Login)")
label=Label(win,text="Enter your Username").grid(column=1,row=1)
abel=Label(win,text="Enter your Password").grid(column=1,row=3)

print=Label(text="")
def check():
	f=open("Data.txt","r")
	for line in f:
		if (txt.get()+" "+txt1.get()==line.strip()):
			print.config(text="LogStatus:\nYou have\n sucessfully\n Logged In!!",fg="Red") 
			print.grid(column=1,row=20)

  
		else:
			print.config(text="LogStatus:\nUser not registerd\n/Wrong Details!",fg="Red") 
			print.grid(column=1,row=20)

  
	f.close()
login=Button(text="Log In",command=check,bg="Orange",fg="White",activebackground="White",activeforeground="Black")
login.grid(column=1,row=5)
win.mainloop()