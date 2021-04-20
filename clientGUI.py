from tkinter import*

import time, socket, sys
import threading
root=Tk()
root.title("Client GUI")
root.geometry("700x600")


def Connect():
    
    soc.connect(("127.0.0.1",8080))
    lstConv.insert(END,"connected....\n")
    
    

    
    global name
    name=sNameent.get()
    
    name=soc.send(name.encode('utf8'))
    global server_name 
    server_name = soc.recv(1024)
    
    server_name = server_name.decode()
    
    lstConv.insert(END,'{} has joined...'.format(server_name),'\n')
    lstConv.insert(END,'Type bye to exit.\n')
    
    sernm=server_name
    server_name=sernm+">"
    
def Receive_File():
    to=Tk()
    filelbl=Label(to,text="Enter filename with extension.")
    filelbl.grid(row=0,column=0)
    fileent=Entry(to)
    fileent.grid(row=0,column=1)
    btn=Button(to,text="Receive",command=lambda :Receive()).grid(row=0,column=3)
    def Receive():
        filename=fileent.get()
        file=open(filename,'wb')
        filedata=soc.recv(1024)
        file.write(filedata)
        file.close()
        #print("filehasbeenreceivedsuccefully")

def Receive_IFile():
    to=Tk()
    filelbl=Label(to,text="Enter filename with extension.")
    filelbl.grid(row=0,column=0)
    fileent=Entry(to)
    fileent.grid(row=0,column=1)
    btn=Button(to,text="Receive",command=lambda :Receive()).grid(row=0,column=3)
    def Receive():
        filename=fileent.get()
        recived_f = 'imgt_thread'+str(time.time()).split('.')[0]+'.jpeg'
        with open(filename, 'wb') as f:
            print('file opened')
            while True:
                #print('receiving data...')
                data = soc.recv(1024)
                #print('data=%s', (data))
                if not data:
                    f.close()
                    print('file close()')
                    break
                # write data to a file
                f.write(data)


def Receive_VFile():
    to=Tk()
    filelbl=Label(to,text="Enter filename with extension.")
    filelbl.grid(row=0,column=0)
    fileent=Entry(to)
    fileent.grid(row=0,column=1)
    btn=Button(to,text="Receive",command=lambda :Receive()).grid(row=0,column=3)
    def Receive():
        filename=fileent.get()
        recived_f = 'imgt_thread'+str(time.time()).split('.')[0]+'.mp4'
        with open(filename, 'wb') as f:
            print('file opened')
            while True:
                #print('receiving data...')
                data = soc.recv(1024)
                #print('data=%s', (data))
                if not data:
                    f.close()
                    print('file close()')
                    break
                # write data to a file
                f.write(data)
     
 
def Send():
    message = msgEnt.get()
    msg.set("")
    name=sNameent.get()
    nm=name
    name=nm+">"
    lstConv.insert(END,name,">",message)
    print("nameis",name)
    lstConv.insert(END,"\n")
       
    if message == "bye":
       message = "Leaving the Chat room"
       soc.send(message.encode())
       print("\n")
      
    soc.send(message.encode())
    
    
    
    
def recvmsg():
    try:
        message = soc.recv(1024)
        message = message.decode()
        lstConv.insert(END,server_name,">", message)
        lstConv.insert(END,"\n")
    except Exception as e:
        print("Exception is ",e)   


    
    



msg=StringVar() 
hostlbl=Label(root,text="Host addr").grid(row=0,column=1)
hostent=Entry(root)
hostent.grid(row=0,column=2)

port=IntVar()
portlbl=Label(root,text="Port addr").grid(row=1,column=1)
portent=Entry(root)
portent.grid(row=1,column=2)

global soc
soc=socket.socket()

hostent.insert(END,"127.0.0.1")
portent.insert(END,8080)

sNamelbl=Label(root,text="Enter Name for client").grid(row=3,column=1)
sNameent=Entry(root)
sNameent.grid(row=3,column=2)

Connctbtn=Button(root,text="Connect",command=lambda :Connect()).grid(row=4,column=0)

global lstConv
lstConv=Text(root,width="100")


    
lstConv.grid(row=6,column=0,columnspan=8)

msgEnt=Entry(root,textvariable=msg)
msgEnt.grid(row=30,column=0)

Sendbtn=Button(root,text="SEND",command=lambda :Send()).grid(row=30,column=1)
Recvbtn=Button(root,text="RECV",command=lambda :recvmsg()).grid(row=30,column=2)

ReceiveFilebtn=Button(root,text="Receive File",command=lambda :Receive_File()).grid(row=50,column=2)

ReceiveIFilebtn=Button(root,text="Receive IFile",command=lambda :Receive_IFile()).grid(row=50,column=3)

ReceiveVFilebtn=Button(root,text="Receive VFile",command=lambda :Receive_VFile()).grid(row=60,column=3)

root.mainloop()
