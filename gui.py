from tkinter import *
import func

def clicked():
    func.set_query("serie", txt_name.get(), txt_season.get(), txt_episode.get(), txt_lang.get())

wm = Tk()
wm.title("Sub Accsess")
wm.geometry('250x200')

lbl_name = Label(wm, text="TV Serie Name")
lbl_name.grid(column=0, row=0)
txt_name = Entry(wm,width=10)
txt_name.grid(column=1, row=0)

lbl_season = Label(wm, text="Season")
lbl_season.grid(column=0, row=1)
txt_season = Entry(wm,width=10)
txt_season.grid(column=1, row=1)

lbl_episode = Label(wm, text="Episode")
lbl_episode.grid(column=0, row=2)
txt_episode = Entry(wm,width=10)
txt_episode.grid(column=1, row=2)

lbl_lang = Label(wm, text="Lang(eng, tur)")
lbl_lang.grid(column=0, row=3)
txt_lang = Entry(wm,width=10)
txt_lang.grid(column=1, row=3)

btn = Button(wm, text="Search", command=clicked)
btn.grid(column=2, row=0)

wm.mainloop()
