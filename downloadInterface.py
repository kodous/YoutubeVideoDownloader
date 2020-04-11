import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os


class GraphicInterface(object):

    def __init__(self):
        self.root = tk.Tk()
        self.dir = os.getcwd()
        self.progressBar = None
        self.createWidgets()
        self.root.title("Youtube Playlist Downloader")
        self.root.config(relief=tk.GROOVE, bd=3, bg="#515151")
        self.root.geometry("500x400")
        self.root.mainloop()

    def createWidgets(self):
        # create the superior frame
        supframe = tk.Frame(self.root, bd=8, bg="#515151")
        supframe.pack()
        # create Text Entry to get the URL for the youtube Playlist
        tk.Label(supframe, text="Enter a youtube playlist URL", fg="white", bg="#515151").pack(side=tk.LEFT, padx=20,
                                                                                               pady=5)
        self.playlistURL = tk.Entry(supframe, fg="#515151", width="40")
        self.playlistURL.pack(side=tk.RIGHT, expand=True, pady=5)

        # create the frame that contains check buttons
        checkframe = tk.Frame(self.root, bd=3, pady=50, padx=10, height=10, bg="#515151")

        self.downloadVideoVar = tk.IntVar()
        self.downloadAudioVar = tk.IntVar()

        tk.Checkbutton(checkframe, text="DownLoadVideo", fg="white", bg="#515151", selectcolor="#515151",
                       variable=self.downloadVideoVar).grid(row=0, column=1, padx=3, pady=3)
        tk.Checkbutton(checkframe, text="DownloadAudio", fg="white", bg="#515151", selectcolor="#515151",
                       variable=self.downloadAudioVar).grid(row=0, column=2, padx=3, pady=3)

        tk.Button(checkframe, text="Choose Directory", bg="#515151", fg="white", command=self.ChooseDirectory).grid(
            column=0, row=0, pady=3, padx=5)
        checkframe.pack()

        # create the frame that contains the progressBar

        beginFrame = tk.Frame(self.root, bd=3, pady=10, bg="#515151")

        tk.Button(beginFrame, text="Begin", fg="white", bg="#515151",
                  command=self.beginProcess).grid(row=0, column=0)

        self.progressBar = ttk.Progressbar(beginFrame, length=280, orient=HORIZONTAL, mode='determinate')
        self.progressBar.grid(row=1, column=0, pady=10)

        beginFrame.pack()

    def beginProcess(self):
        pass

    def ChooseDirectory(self):
        self.dir = filedialog.askdirectory()

    def GetDir(self):
        return self.dir

    def updateProgressBar(self, x, y, value, a, b):
        print('here')
        print(self.progressBar['value'])
        self.progressBar['value'] = value * 100
        self.root.update_idletasks()
