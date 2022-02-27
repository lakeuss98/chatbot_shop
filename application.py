import time
from tkinter import *
from main1 import dialogue,chat1
#import mysql.connector
import time
def send():
    i=1
    edit.configure(state=NORMAL)
    time.sleep(2)
    print("test1")
    edit.insert(END,str("vous     :") + sendtext.get()+"\n")
    edit.insert(END,str("bot shop :")+chat1.respond(sendtext.get())+"\n\n")
    edit.tag_add("vous",1.0,END)
    edit.tag_add("bot",2.0,END)
    edit.tag_config("vous",foreground="blue")
    sendtext.delete(0,END)
    edit.configure(state=DISABLED)
    edit.see(END)
    i=i+1
def sende(event):
    send()

root=Tk()
root.title("messagerie shop")
root.iconbitmap("")
root.geometry("400x450")
root.minsize(400, 450)
root.maxsize(400, 450)
root.config(background="white")

frame=Frame(root,width=400,bg="yellow")
frame.pack(side="top")

framelabel=Frame(frame,bg="yellow",width=400,height=30)
framelabel.pack(fill=X)
label=Label(framelabel,text="bot shop",bg="yellow",justify="center",font="arial 20")
label.pack(fill=BOTH)
edit=Text(frame,width=200)
edit.pack()
edit.configure(cursor="arrow",state=DISABLED)

sendframe=Frame(root,bg="red")
sendframe.pack(fill=BOTH)

sendtext=Entry(sendframe,bg="yellow",width=30)
sendtext.focus()
sendtext.bind("<Return>",sende)
sendtext.pack(side="left")
btnsend=Button(sendframe,width=10,fg="black",bg="green",text="send",command=send)
btnsend.pack(side="right")
btndel=Button(sendframe,width=10,fg="black",bg="green",text="del",command= lambda :sendtext.delete(1.0,END))
btndel.pack(side="right")
root.mainloop()
"""  

def efface():
    saisie.delete(1.0,END)

def click1():
    con = mysql.connector.connect(host="127.0.0.1", user="root", database="chatbot", password='')
    if con:
      print("ok ,conection effectue pour l'envoi ")

    pointeur=con.cursor()
    i=0
    print("test 123")
    if saisie.get(1.0,END):
        print("je suis dans l existence de texte")
        mes = str(saisie.get(1.0,END))
        req='INSERT INTO message( contenu) VALUES ( %s )'
        pointeur.execute(req,( mes, ))
        con.commit()
        con.close()
        #frame.grid(row=0,column=0,sticky=NE)
        #note.insert(0,saisie.get(1.0,END))
        Label(frame,text=saisie.get(1.0,END),fg="blue",anchor=NW,bg="green").grid()
        saisie.delete(1.0,END)
        i=i+1


root=Tk()
root.title("messagerie shop")
root.iconbitmap("")
root.geometry("400x500")
root.minsize(400, 450)
root.maxsize(400, 500)
root.config(background="white")

id 294331821
mdp 03110583
#titre=Label(root,text="chat-bot",bg="white",fg="black",width=400,height=50)
#titre.grid(row=0)
frame=Frame(root,width=400,height=415,bg="green")
#frame.configure(width=400,height=415,bg="black")
frame.grid(row=0,column=0,padx=(0,0),pady=(0,0))
edittext=Text(frame,width=390,height=25,bg="yellow")
edittext.grid(padx=(0,0),pady=(0,0))
scrol=Scrollbar(edittext)
#scrol.grid()
scrol.configure(command=edittext.yview())



#note=Text(root,bg="green",relief=SUNKEN,width=400,height=26)
#note.grid(row=0,column=0,padx=(0,0),pady=(0,0))
saisie = Text(root,bg="red",height=4,relief=SUNKEN,border=2,width=40)
saisie.grid(row=1,column=0,sticky=W,padx=(5,0),pady=(6,2))
#saisie = Entry(root,bg="red",relief=SUNKEN,border=2,width=40)
#saisie.grid(row=1,sticky=W,padx=(5,0),pady=(6,2))

btns=Button(root,width=8,text="send",foreground="blue",bg="black",command=click1)
btns.grid(row=1,column=0,sticky=NE,pady=(4,3))
btne=Button(root,width=8,text="delete",foreground="blue",bg="black",command=efface)
btne.grid(row=1,column=0,sticky=SE,pady=(0,3))
#saisie.insert(0,"entrer votre mseesage")ac

root.mainloop()
"""
