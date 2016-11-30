import unittest
from song import Song, Playlist


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song()

    def test_init(self):
        self.assertEqual(self.song.__str__(),
                         "Manowar - Odin from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertEqual(self.song, Song("Odin", "Manowar",
                                         "The Sons of Odin",
                                         "3:44"))

    def test_lenght_(self):
        song1 = Song(length="1:1:12")
        self.assertEqual(song1.lenght(seconds=True), "3672")
        self.assertEqual(song1.lenght(minutes=True), "61")
        self.assertEqual(song1.lenght(hours=True), "1")
        self.assertEqual(song1.lenght(), "1:1:12")


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.pl1 = Playlist()

    def test_add_song(self):
        self.assertFalse(self.pl1.songs)
        self.pl1.add_song(Song())
        self.assertTrue(self.pl1.songs)

    def test_remove_song(self):
        song = Song()
        self.pl1.add_song(song)
        self.pl1.remove_song(song)
        self.assertFalse(self.pl1.songs)

    def test_add_songs(self):
        songs = [Song(), Song("Pretty Fly")]
        self.pl1.add_songs(songs)
        self.assertEqual(len(self.pl1.songs), 2)

    def test_toatl_length(self):
        songs = [Song(), Song("Pretty Fly", "The Offspring")]
        self.pl1.add_songs(songs)
        self.assertEqual(self.pl1.total_length(), "0:7:28")

    def test_artist(self):
        songs = [Song(), Song("Pretty Fly", "The Offspring")]
        self.pl1.add_songs(songs)
        self.assertEqual(self.pl1.artists(), {"Manowar": 1,
                                              "The Offspring": 1})


if __name__ == "__main__":
    unittest.main()
