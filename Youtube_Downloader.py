from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title(" Youtube Video Download  ")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#function to download video
def download_video():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'Video_Download', font = 'arial 15').place(x= 150 , y = 210)

def download_audio():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first()
    audio.download()
    Label(root, text = 'Audio_Download', font = 'arial 15').place(x= 150 , y = 250)

Button(root,text = 'Video Download', font = 'arial 12 bold' ,bg = 'pale violet red', padx = 2, command = download_video).place(x=100 ,y = 150)
Button(root,text = 'Audio Download', font = 'arial 12 bold' ,bg = 'light blue', padx = 2, command = download_audio).place(x=300 ,y = 150)

root.mainloop()

print("Create By Yasser-Fekry ☕💻");