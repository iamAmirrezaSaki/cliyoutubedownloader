from pytube import YouTube
import tqdm
import os
from threading import Thread


class YouTubeDownloder:
    def __init__(self):
        self.url = str(input("Enter the url of video : "))
        self.youtube = YouTube(self.url)
        self.showTitle()

    def showTitle(self):
        print("title : {0}\n".format(self.youtube.title))
        self.showStreams()

    def showStreams(self):
        self.streamNo = 1
        for stream in self.youtube.streams:
            print("{0} => resolation:{1}/fps:{2}/type:{3}".format(self.streamNo,
                                                                  stream.resolution, stream.fps, stream.type))
            self.streamNo += 1
        self.chooseStream()

    def chooseStream(self):
        self.choose = int(input("please select one : "))
        self.validateChooseValue()

    def validateChooseValue(self):
        if self.choose in range(1, self.streamNo):
            self.main()
        else:
            print("please enter a currect option on the list.")
            self.chooseStream()

    def process(self):
        print("please wait downloading ... ")
        thread = Thread(target=self.download)
        thread.start()

    def download(self):
        self.youtube.streams[self.choose-1].download()

    def main(self):
        self.process()


if __name__ == "__main__":
    try:
        YouTubeDownloder()
    except Exception as e:
        print(e)
