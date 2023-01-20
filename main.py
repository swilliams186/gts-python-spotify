import threading
import time
from tkinter import *
from spotify_handler import SongGrabber, Track
from music_box import MusicBox
from gamerino import Gamerino

from PIL import ImageTk, Image

# Creating a new window and configurations
window = Tk()
window.title("Guess the song!")
window.minsize(width=500, height=500)
window.config(padx= 100)
window.config(background="purple")






mb = MusicBox()
game = Gamerino()
current_track = Track
q_mark = ImageTk.PhotoImage(Image.open("q_mark.jpg"))
title_img = ImageTk.PhotoImage(Image.open("title.jpg"))
background_img = ImageTk.PhotoImage(Image.open("cosmic-dust.jpg"))

lbl_background = Label(image=background_img)
lbl_background.place(x=-120, y=0)

lbl_info = Label(text="Guess the Song", font=("trajan-bold", 25))
#lbl_info.pack()
lbl_info.grid(column=0,row=0, columnspan=2)

def play():
    lbl_artist.config(text="Song playing")
    lbl_track_title.config(text="Guess what it is!")
    canvas.create_image(0, 0, image=q_mark, anchor=NW)
    game.play_track()

    update_info()


btn_play = Button(text="Play", command=play)
btn_play.grid(column=1, row=5)


def next_track():
    global current_track, q_mark
    canvas.create_image(0, 0, image=q_mark, anchor=NW)
    current_track = game.next_track()
    lbl_artist.config(text="Next track ready")
    lbl_track_title.config(text="Press play to start!")


def update_info():
    global album_art
    lbl_track_title.config(text=current_track.name)
    lbl_artist.config(text=current_track.artist)
    album_art = ImageTk.PhotoImage(Image.open("temp.jpg"))
    # album_art = album_art.resize((200,200), Image.ANTIALIAS)
    canvas.create_image(0, 0, image=album_art, anchor=NW)
    # lbl_image.config(window, image=album_art)


def search():
    global current_track
    if entry_search.get() == "":
        game.search_genre_year(genre=listbox_genre.get(listbox_genre.curselection()),
                               year=listbox_year.get(listbox_year.curselection()))
    else:
        game.search(entry_search.get())

    current_track = game.get_current_track_info()
    lbl_artist.config(text="Tracks ready")
    lbl_track_title.config(text="Press play to start!")
    #update_info()


entry_search = Entry(width=30)
entry_search.insert(END, string="")
entry_search.grid(column=0, row=4)

lbl_track_title = Label(text="Song Title")
lbl_track_title.grid(column=1, row=1)

lbl_artist = Label(text="Artist")
lbl_artist.grid(column=0, row=1)

listbox_year = Listbox(height=5, exportselection=0)
years = ["1970", "1980", "1990", "2000", "2010", "2020"]
listbox_year.insert(END, *years)
listbox_year.select_set(0)
listbox_year.grid(column=0, row=3)

listbox_genre = Listbox(height=5, exportselection=0)
genres = ["Rock", "Pop", "Metal", "Country", "Dance"]
listbox_genre.insert(END, *genres)
listbox_genre.select_set(0)
listbox_genre.grid(column=1, row=3)


canvas = Canvas(window, width=300, height=300)
canvas.grid(row=2, column=0,columnspan=2)
canvas.create_image(0, 0, image=title_img, anchor=NW)
# lbl_image = Label()
# lbl_image.pack()

btn_search = Button(text="Search", command=search)
btn_search.grid(column=1, row=4)
btn_next_track = Button(text="NEXT!", command=next_track)
btn_next_track.grid(column=0, row=5)
sg = SongGrabber()
sg.get_sample_list("Bring Me The Horizon")
#search()
window.mainloop()
