import pafy
import threading
from downloadInterface import GraphicInterface
from tkinter import messagebox


class ThreadManager(GraphicInterface):

    def __init__(self):
        print("init")
        self.url = ''
        GraphicInterface.__init__(self)

    def beginProcess(self):

        directory = self.GetDir()
        self.url = self.playlistURL.get()

        if "playlist?" in self.playlistURL.get():
            t1 = threading.Thread(target=self.downloadPlaylist, args=(directory, self.downloadAudioVar.get(),))
            t1.start()

        else:
            t1 = threading.Thread(target=self.downloadVideo, args=(directory, self.downloadAudioVar.get(),))
            t1.start()

    def downloadPlaylist(self, directory, audio=False):

        # create an object containing all the playlist items
        playlist = pafy.get_playlist(self.url)

        playlist_length = len(playlist['items'])
        video_downloaded = 0
        if audio:
            for vid in playlist['items']:
                video_name = vid['pafy'].title
                filepath = directory + '/' + video_name.replace('/', '')
                try:
                    vid['pafy'].getbestaudio().download(filepath=filepath + '.mp3')
                    video_downloaded += 1
                    ratio = (video_downloaded / playlist_length)
                    self.updateProgressBar(0, 0, ratio, 0, 0)
                except Exception as e:
                    print(e)
                    messagebox.showerror('Error', 'an Error happened while Downloading: \n' + video_name)
        else:
            for vid in playlist['items']:
                video_name = vid['pafy'].title
                filepath = directory + '/' + video_name.replace('/', '')
                try:
                    vid['pafy'].getbestvideo().download(filepath=filepath + '.mp4')
                    video_downloaded += 1
                    ratio = (video_downloaded / playlist_length)
                    self.updateProgressBar(0, 0, ratio, 0, 0)
                except Exception as e:
                    print(e)
                    messagebox.showerror('Error', 'an Error happened while Downloading: \n' + video_name)

    def downloadVideo(self, directory, audio=False):

        video = pafy.new(self.url)
        filepath = directory + '/' + video.title.replace('/', '')
        try:
            if audio:
                video.getbestaudio().download(filepath=(filepath + '.mp3'), callback=self.updateProgressBar)
            else:
                video.getbestvideo().download(filepath=(filepath + '.mp4'), callback=self.updateProgressBar)
        except Exception as e:
            print(str(e))
            messagebox.showerror('Error', 'an Error happened while Download')


if __name__ == "__main__":
    ThreadMan = ThreadManager()
