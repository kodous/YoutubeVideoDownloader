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

    # def updateProgressBar(self, totalBytes, bytesDownloaded, ratioDownloaded, downloadRate, ETAsec):
    #     self.progressBar['value'] = ratioDownloaded * 100
    #     self.root.update_idletasks()

    def downloadPlaylist(self, directory, audio=False):

        # create an object containing all the playlist items
        playlist = pafy.get_playlist(self.url)

        if audio:
            for vid in playlist['items']:
                video_name = vid['pafy'].title
                filepath = directory + '/' + video_name.replace('/', '')
                try:
                    vid['pafy'].getbestaudio().download(filepath=filepath + '.mp3')
                except Exception as e:
                    print(e)
        else:
            for vid in playlist['items']:
                video_name = vid['pafy'].title
                filepath = directory + '/' + video_name.replace('/', '')
                try:
                    vid['pafy'].getbestvideo().download(filepath=filepath + '.mp4')
                except Exception as e:
                    print(e)
            print("PlayList downloaded")

    def downloadVideo(self, directory, audio=False):

        video = pafy.new(self.url)
        filepath = directory + '/' + video.title.replace('/', '')
        try:
            if audio:
                video.getbestaudio().download(filepath=(filepath + '.mp3'), callback=self.updateProgressBar)
            else:
                video.getbestvideo().download(filepath=(filepath + '.mp4'), callback=self.updateProgressBar)
            messagebox.showinfo("info", "Download Complete")
        except Exception as e:
            print(str(e))
            messagebox.showerror('Error', 'an Error happened while Download')


if __name__ == "__main__":
    ThreadMan = ThreadManager()
