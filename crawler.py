from mutagen.mp3 import MP3
from os import listdir
from song import Playlist, Song
# http://stackoverflow.com/questions/4040605/does-anyone-have-good-examples-of-using-mutagen-to-write-files


class MusicCrawler:

    def __init__(self, path="/home/jor0/Music"):
        self.path = path
        self.songs = self.see_playlists()

    def generate_playlist(self):
        pl = Playlist(name="New_Generated_Playlist")
        for el in self.songs:
            album = MP3(self.path + "/" + el).tags["TALB"]
            artist = MP3(self.path + "/" + el).tags["TPE1"]
            title = MP3(self.path + "/" + el).tags["TIT2"]
            secs = MP3(self.path + "/" + el).info.pprint().split(", ")[-1]
            secs = self.format_length(int(secs.split(".")[0]))
            pl.add_song(Song(title=str(title),
                             artist=str(artist),
                             album=str(album),
                             length=secs,
                             path_to_file=self.path + "/" + el))
        return pl

    def format_length(self, lnght):
        m, s = divmod(lnght, 60)
        h, m = divmod(m, 60)
        if h:
            return "{}:{}:{}".format(h, m, s)
        return"{}:{}".format(m, s)

    def see_playlists(self):
        playlists = []
        for file in listdir(self.path):
            if file.endswith(".mp3"):
                playlists.append(file)
        return playlists


def main():
    crawl = MusicCrawler("/home/jor0/Music/Upsurt")
    pl = crawl.generate_playlist()
    print(pl.songs)
    # print(crawl.see_playlists())
    # print([el for el in pl.songs])
    # print(crawl.songs)


if __name__ == "__main__":
    main()
