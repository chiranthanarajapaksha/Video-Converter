#!/usr/bin/env python3

import os
import sys
import time
import pipes
import tkinter as tk
from tkinter import filedialog

def video_to_audio(fileName):
    try:
        file, file_extension = os.path.splitext(fileName)
        file = pipes.quote(file)
        video_to_wav = 'ffmpeg -i ' + file + file_extension + ' ' + file + '.wav'
        final_audio = 'lame '+ file + '.wav' + ' ' + file + '.mp3'
        os.system(video_to_wav)
        os.system(final_audio)
        print("Successfully converted ", fileName, " into audio!")
    except OSError as err:
        print(err)
        exit(1)

def convert():
    filePath = file_entry.get()
    if not os.path.exists(filePath):
        print("File not found!")
        return
    video_to_audio(filePath)
    time.sleep(1)

def browse_file():
    filePath = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filePath)

# GUI setup
root = tk.Tk()
root.title("Video to Audio Converter")

file_label = tk.Label(root, text="Select Video File:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

root.mainloop()

#developed by Chiranthana Subhavitha Rajapaksha
#github.com/chiranthanarajapaksha