from METADATA import *
from random import choice
from prettytable import PrettyTable
import json
from os import listdir
from os.path import isfile, join


class Song:

    def __init__(self, title=DEFAULT_TITLE, artist=DEFAULT_ARTIST,
                 album=DEFAULT_ALBUM, length=DEFAULT_LENGHT,
                 path_to_file=None):
        self.title = title
        self.path_to_file = path_to_file
        self.artist = artist
        self.album = album
        self.song_length = length
        self.formated_length = self.format_length(length)

    def __str__(self):
        return STR_RETURN. \
            format(artist=self.artist, title=self.title, album=self.album,
                   length=self.song_length)

    def __repr__(self):
        return STR_RETURN. \
            format(artist=self.artist, title=self.title, album=self.album,
                   length=self.song_length)

    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title and \
            self.album == other.album and self.song_length == other.song_length

    def __hash__(self):
        return hash(self.hash)

    def format_length(self, length):
        temp = length.split(":")
        temp.reverse()
        result = {}
        if len(temp) == 3:
            result["hour"] = int(temp[2])
        else:
            result["hour"] = 0
        result["min"] = int(temp[1])
        result["sec"] = int(temp[0])
        return result

    def lenght(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return str(self.formated_length["sec"] +
                       (self.formated_length["min"] * 60) +
                       (self.formated_length["hour"] * 3600))
        elif minutes:
            return str(self.formated_length["min"] +
                       self.formated_length["hour"] * 60)
        elif hours:
            return str(self.formated_length["hour"])
        return "{lenght}".format(lenght=self.song_length)

    def serialize(self):
        return self.__dict__

    def play_song(self):
        pass


class Playlist:

    def __init__(self, name="Chill", repeat=False,
                 shuffle=False, start_from=0):
        self.name = name
        self.songs = []
        self.size = 0
        self.repeat = repeat
        self.shuffle = shuffle
        self.curr_song = start_from
        self.played = []

    def __eq__(self, other):
        result = True
        for el in range(len(self.songs)):
            if self.songs[el] not in other.songs:
                result = False
        return result

    def __hash__(self):
        return hash(self(hash))

    def add_song(self, new_song):
        self.songs.append(new_song)
        self.size += 1

    def remove_song(self, old_song):
        self.songs.remove(old_song)
        self.size -= 1

    def add_songs(self, new_songs):
        self.songs.extend(new_songs)
        self.size += len(new_songs)

    def total_length(self):
        result = {"hour": 0, "min": 0, "sec": 0}
        for el in self.songs:
            result["hour"] += el.formated_length["hour"]
            result["min"] += el.formated_length["min"]
            result["sec"] += el.formated_length["sec"]
        result["min"] += result["sec"] // 60
        result["sec"] = result["sec"] % 60
        result["hour"] += result["min"] // 60
        result["min"] = result["min"] % 60
        return "{h}:{m}:{s}".format(h=result["hour"], m=result["min"],
                                    s=result["sec"])

    def artists(self):
        art = {}
        for el in self.songs:
            if el.artist not in art.keys():
                art[el.artist] = 1
            else:
                art[el.artist] += 1
        return art

    def next_song(self):
        self.played.append(self.curr_song)
        print("Playing - {}".format(self.songs[self.curr_song]))
        if self.curr_song == self.size - 1 and not self.repeat:
            self.curr_song = 0
            return False
        elif self.curr_song == self.size - 1 and self.repeat:
            self.curr_song = 0
            print("Coming now - {}".format(self.songs[self.curr_song]))
            return self.songs[self.curr_song]
        elif not self.shuffle:
            self.curr_song += 1
            print("Coming now - {}".format(self.songs[self.curr_song]))
            return self.songs[self.curr_song]
        elif self.shuffle:
            if len(self.played) == self.size:
                self.played = []
            while True:
                pass
            temp = choice(self.songs)
            if temp not in self.played:
                self.curr_song += 1
                print("Coming now - {}".format(self.songs[self.curr_song]))
                return self.songs[curr_song]

    def pprint_playlist(self):
        result = PrettyTable()
        result.field_names = ["Artist", "Song", "Length"]
        for el in self.songs:
            result.add_row([el.artist, el.title, el.song_length])
        return result

    def save(self):
        result = []
        with open("playlist-data/" + self.name.replace(" ", "-") +
                  ".json", "w") as json_data:
            for el in self.songs:
                result.append(el.serialize())
            json.dump(result, json_data, indent=4)

    def see_playlists(self):
        playlists = [f for f in listdir("playlist-data/")
                     if isfile(join("playlist-data/", f))]
        return playlists

    @staticmethod
    def load(to_load):
        with open("playlist-data/" + to_load, "r") as json_data:
            return json.load(json_data)


def main():
    pl1 = Playlist(name="My playlist", repeat=True)
    songs = [Song(), Song("Pretty Fly For A White Guy", "The Offspring",
                          "Americana", "3:14"), Song("Trepni", "Azis",
                                                     "Azis Special", "2:34")]
    pl1.add_songs(songs)
    # pl1.next_song()
    # pl1.next_song()
    # pl1.next_song()
    # print(pl1.pprint_playlist())
    # pl1.save()
    # a = Playlist(Playlist.load("My-playlist.json"))
    # print(a == pl1)
    # print(pl1.__dict__)
    print(pl1.see_playlists())


if __name__ == "__main__":
    main()
