from tkinter import*
from tkinter import ttk
from tkinter import messagebox

a=Tk()
a.title('form')
a.geometry('600x700' )
a.config(background='#42f5f5')

def system():
  
        Label(a,text=' Registred Sucessfully',bg='blue',fg="white",font=('times',10,'bold')).place(x=190,y=740)
   
        messagebox.infoerror('Message','Registerd sucessfully')
   
Label(a,text='EMPLOYEE REGISTRATION FORM',bg='white',fg='black',pady=10,font=('times',20,'bold')).place(x=55,y=60)
Label(a,text='First Name',bg='white',fg="black",font=('times',15)).place(x=63,y=150)
Entry(a,width=20,font=('times',15)).place(x=290,y=150)
Label(a,text=' Last Name',bg='white',fg="black",font=('times',15)).place(x=63,y=200)
Entry(a,width=20,font=('times',15)).place(x=290,y=200)
Label(a,text='D.O.B',bg='white',fg='black',font=('times',15)).place(x=63,y=250)
Entry(a,width=20,font=('times',15)).place(x=290,y=250)
Label(a,text='Contact Number',bg='white',fg='black',font=('times',15)).place(x=63,y=300)
Entry(a,width=20,font=('times',15)).place(x=290,y=300)
Label(a,text='Select Gender',bg='white',fg='black',font=('times',15)).place(x=63,y=350)
mVar=IntVar()
k=Radiobutton(a,text='Male',bg='white',fg='black',variable=mVar,value=1,font=('times',13,'bold')).place(x=290,y=350)
b=Radiobutton(a,text='Female',bg='white',fg='black',variable=mVar,value=2,font=('times',13,'bold')).place(x=360,y=350)
c=Radiobutton(a,text='others',bg='white',fg='black',variable=mVar,value=3,font=('times',13,'bold')).place(x=450,y=350)
Label(a,text='Select Country',bg='white',fg='black',font=('times',15)).place(x=63,y=400)
select=StringVar()
select.set("United States")
OptionMenu(a,select,'America','Australia','China','Germany','France','India','italy').place(x=290,y=400)
Label(a,text='Address',bg='white',fg='black',font=('times',15)).place(x=63,y=450)
Entry(a,width=20,font=('times',15)).place(x=290,y=450)
Label(a,text='Skills',bg='white',fg='black',font=('times',15)).place(x=63,y=500)
cb=ttk.Combobox(a,width=20,font=('tims',14))
cb['values']=('c','c++','Java','Python','PHP','SQL','HTML','CSS','JavaScript','JQuery','React JS','Bootsrap')
cb.place(x=290,y=500)
Label(a,text='Enter Email',bg='white',fg='black',font=('times',15)).place(x=63,y=550)
Entry(a,width=20,font=('times',15)).place(x=290,y=550)
Label(a,text='Enter Password',bg='white',fg='black',font=('times',15)).place(x=63,y=600)
Entry(a,width=20,font=('times',15)).place(x=290,y=600)
Button(a,text='Register',bg='white',fg='black',font=('times',15),command=system).place(x=225,y=670)
a.mainloop()
