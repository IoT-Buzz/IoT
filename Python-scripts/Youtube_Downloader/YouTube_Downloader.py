from tkinter import *


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  


root = Tk()
root.geometry('680x350')
root.resizable(0, 0)
root.config(bg=rgb_hack((170, 187, 233))) 
root.title("YouTube Video Downloader")

Label(root, text='Copy the link of the video you want to download from YouTube',
      font='Times').pack()

# enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=270, y=100)
Entry(root, width=100, textvariable=link).place(x=32, y=150)

# function to download video


def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=260, y=240)


Button(root,text='DOWNLOAD',font=('Times', 15),padx=10,bg='#4a7abc',command=Downloader,fg='yellow',activebackground='green',activeforeground='white').place(x=280, y=180)

root.mainloop()