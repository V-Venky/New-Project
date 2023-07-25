from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube 
def downloader(link, directory, filename):
    yt_link = link.get()
    save_path = directory.get()
    aftersave_filename = filename.get()

    try:
        yt = YouTube(yt_link)
        video = yt.streams.first()#extracts the video
        video.download(save_path, aftersave_filename)
    except:
        mb.showerror('Error', 'Connection Error! You are offline!')


def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set('')
    d_strvar.set('')
    fn_strvar.set('')

#Initializing the window
root = Tk()
root.title('Online Videos Downloader')
root.geometry('900x400')
root.resizable(0, 0)
root.config(bg='green')

#labels
Label(root, text='Online Videos Downloader', font=("Algerian", 15), bg='blue').place(relx=0.25, rely=0.0)

#Creating window
Label(root, text='Enter the Youtube link:', font=("Times New Roman", 13), bg='yellow').place(relx=0.05, rely=0.2)

link_strvar = StringVar(root)
link_entry = Entry(root, width=50, textvariable=link_strvar)
link_entry.place(relx=0.5, rely=0.2)


Label(root, text='Enter the save location:', font=("Harlow Solid Italic", 13), bg='orange').place(relx=0.05, rely=0.4)

dir_strvar = StringVar(root)
dir_entry = Entry(root, width=50, textvariable=dir_strvar)
dir_entry.place(relx=0.5, rely=0.4)


Label(root, text='Enter the filename:', font=("Cascadia Code", 13), bg='red').place(relx=0.05, rely=0.6)

filename_strvar = StringVar(root)
filename_entry = Entry(root, width=50, textvariable=filename_strvar)
filename_entry.place(relx=0.5, rely=0.6)

# Creating the buttons
download_btn = Button(root, text='Download', font=7, bg='Aquamarine',
                      command=lambda: downloader(link_entry, dir_entry, filename_entry)).place(relx=0.3, rely=0.75)

reset_btn = Button(root, text='Reset', font=7, bg='Aquamarine',
                   command=lambda: reset(link_strvar, dir_strvar, filename_strvar)).place(relx=0.5, rely=0.75)

root.update()
root.mainloop()
