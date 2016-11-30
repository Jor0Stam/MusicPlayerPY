import unittest
from crawler import MusicCrawler


class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.c1 = MusicCrawler("/home/jor0/Music/Upsurt")

    def test_crawling(self):
        self.assertTrue(self.c1.songs)


if __name__ == "__main__":
    unittest.main()
