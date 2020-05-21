
from  tkinter import *
from tkinter import messagebox as mb
def frame1():
    windown=Tk()

    windown.title("My App")
    windown.geometry("450x150")
    def gameon():
        name=str(entry.get())
        passw=entry1.get()
        a="Bạn Nhập sai thông tin tài khoản"
        b="Bạn chưa nhập đầy đủ thông tin"
        if(name=="AndTee" and passw=="123456"):
            return show2()
        elif(name=="" or passw==""):
            return mb.showerror("Error",b)
        else:
            return mb.showerror("Error",a)
    def show2():
        gre=frame2()
        gre.tkraise()
    #--Label--Button--entru--checkbutton--Text
    label1=Label(windown,text="Today is Good day to learn")
    label1.grid(column=0,row=0)
    label2=Label(windown,text="Learn is EZ")
    label2.grid(column=0,row=1)
    #----entry--Label--
    label3=Label(windown,text="UserName")
    label3.grid(column=1,row=1)
    label4=Label(windown,text="PassWork")
    label4.grid(column=1,row=2)
    entry=Entry(windown,width=30,bd=5)
    entry.grid(column=2,row=1)
    entry1=Entry(windown,width=30,bd=5,show="*")
    entry1.grid(column=2,row=2)
    #----Button--
    btn=Button(windown,text="Sign In",bd=4,fg="Green",width=12,command=gameon)
    btn2=Button(windown,text="Cancel",bd=4,fg="Red",width=12)
    btn.grid(column=1,row=3)
    btn2.grid(column=2,row=3)
    #--checkbutton--
    checkbutton=Checkbutton(windown,text="I'M NOT ROBOT")
    checkbutton.grid(columnspan=3)
    windown.mainloop()
def frame2():
    windown2=Tk()
    windown2.title("My APP Trang 2!")
    windown2.geometry("600x600")
    windown2.mainloop()
if __name__=="__main__":
    frame1()
