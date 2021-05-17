import tkinter as t
window = t.Tk()
#vr=t.StringVar()
#passw=t.StringVar()
txt=t.Entry(window,width=10)
txt.grid(column=2,row=1,ipadx=70)
txt1=t.Entry(window,width=10)
txt1.grid(column=2,row=3,ipadx=70)

def pressed():
   t.Label( window,text="Your username is "+txt.get()).grid(column=1,row=10)
   t.Label( window,text="Your password is "+txt1.get()).grid(column=1,row=11)
window.title("SignUp")
label=t.Label(window,text="Enter your Username").grid(column=1,row=1)
abel=t.Label(window,text="Enter your Password").grid(column=1,row=3)
bt=t.Button(window,text="Preview",bg="orange",fg="White",command=pressed,activebackground="White",activeforeground="Black")
bt.grid(column=1,row=15)
def save():
	f=open("Data.txt","a")
	f.write(txt.get()+" "+txt1.get()+"\n")
	f.close()
bts=t.Button(text="Sign Up(Register)",command=save,bg="Orange",fg="White",activebackground="White",activeforeground="Black")
bts.grid(column=1,row=16)
window.mainloop()