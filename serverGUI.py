from tkinter import*
import time, socket, sys
from tkinter import filedialog
import threading
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("Server GUI")
root.geometry("700x600")


def Connect():
    s.bind(("127.0.0.1",8080))
    s.listen(1)
    lstConv.insert(END,"waiting for any conn...\n")

    global conn
    conn,addr = s.accept()

    global name
    name=sNameent.get()
    nm=name
    name=nm+">"

    lstConv.insert(END,"Received connection from", addr[0], "(", addr[1], ")\n  ")
    lstConv.insert(END,'Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
    global client_name
    client_name = conn.recv(1024)

    client_name = client_name.decode()
    lstConv.insert(END,client_name + ' has connected.\n')
    lstConv.insert(END,"Type bye to leave the chat room\n")

    conn.send(name.encode())
    clinm=client_name
    client_name=clinm+">"
    





def recv():
        
        message = conn.recv(1024)
        message = message.decode()
        lstConv.insert(END,client_name,">",message)
        lstConv.insert(END,"\n")
        lstConv.grid(row=6,column=0,columnspan=8)
            
def Send():
    
    global i,j
        
    message = msgEnt.get()
    msg.set("")
    lstConv.insert(END,name,">",message)
    lstConv.insert(END,"\n")
        
    if message == 'bye':
       message = 'Server left the conversation.....Say bye to EXIT...\n'
       conn.send(message.encode())
       lstConv.insert(END,"\n")
       
    conn.send(message.encode())
    


def Send_File():
    File=File_Category.get()
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes=(("All files","*.*"),("png files","*.png"),("jpg files","*.jpg")))
        

    if(File=="Text File"):
        print("Text File",filename)
        
        

        file=open(filename,'rb')
        filedata=file.read(1024)
        conn.send(filedata)
        print("datahasbeentransmitted")
        
    if(File=="Image File"):
        print("Image File")
        f = open(filename, 'rb')
        while True:
            l = f.read(1024)
            while (l):
                
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            if not l:
                f.close()
                conn.close()
                break
        

    if(File=="Video File"):
        print("Video File")
        f = open(filename, 'rb')
        while True:
            l = f.read(1024)
            while (l):
                
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            if not l:
                f.close()
                conn.close()
                break

    if(File=="PDF File"):
        print("PDF File")
    

    
    

    

global msg
msg=StringVar()


hostlbl=Label(root,text="Host addr").grid(row=0,column=1)
hostent=Entry(root)
hostent.grid(row=0,column=2)

port=IntVar()
portlbl=Label(root,text="Port addr").grid(row=1,column=1)
portent=Entry(root)
portent.grid(row=1,column=2)

s=socket.socket()

hostent.insert(END,"127.0.0.1")
portent.insert(END,8080)

sNamelbl=Label(root,text="Enter Name for server").grid(row=3,column=1)
sNameent=Entry(root)
sNameent.grid(row=3,column=2)





global lstConv
lstConv=Text(root,width="100")

lstConv.grid(row=6,column=0,columnspan=8)


Connctbtn=Button(root,text="Connect",command=lambda :Connect()).grid(row=4,column=0)

msgEnt=Entry(root,textvariable=msg)
msgEnt.grid(row=30,column=0)

Sendbtn=Button(root,text="SEND",command=lambda :Send()).grid(row=30,column=1)
Recvbtn=Button(root,text="RECV",command=lambda :recv()).grid(row=30,column=2)

Filelbl=Label(root,text="Choose File Type").grid(row=50,column=0)

File_Category=ttk.Combobox(root,values=["Text File","Image File","Word File","PDF File"])
File_Category.grid(row=50,column=1)

SendFilebtn=Button(root,text="Send File",command=lambda :Send_File()).grid(row=50,column=2)



root.mainloop()

