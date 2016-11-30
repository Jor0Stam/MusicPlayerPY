from crawler import MusicCrawler
from subprocess import call, Popen
from METADATA import *
from time import sleep


class Player:

    def __init__(self, to_play):
        self.to_play = to_play
        self.exit = False
        self.stat = PAUSE

    # def boot_up(self):
    #     pid = Popen(args=[CALL_NEW_TERMINAL, EXECUTE_XMMS2]).pid
    #     while not self.exit:
    #         print(WELCOME_MSSG)
    #         usr_cmd = self.validate(str(input(USR_INP)))
    #         self.summon(pid, usr_cmd)
    #         sleep(1)

    def boot_up(self):
        print(WELCOME_MSSG)
        while not self.exit:
            print(NOW_PLAYING.format(
                song=self.to_play.songs[self.to_play.curr_song],
                status=self.stat))
            self.summon(self.validate(str(input(USR_INP))))
            sleep(0.5)

    def summon(self, usr_cmd):
        Popen(args=[TERMINAL, COMMAND.format(cmd=usr_cmd)])

    def validate(self, usr_cmd):
        if usr_cmd not in CMDS:
            print(BAD_INP)
            return "help"
        if usr_cmd == "exit":
            usr_cmd == "pause"
            self.exit = True
        if usr_cmd == "play":
            self.stat = PLAY
        if usr_cmd == "pause":
            self.stat = PAUSE
        if usr_cmd == "help":
            print(HELP)
        if usr_cmd == "next":
            self.to_play.next_song()
        return usr_cmd


def main():
    pl = MusicCrawler("/home/jor0/Music/Upsurt").generate_playlist()
    play_me = Player(pl)
    play_me.boot_up()


if __name__ == "__main__":
    main()

    #  add
    # current
    # exit
    # help
    # info
    # jump
    # list
    # move
    # next
    # pause
    # play
    # prev
    # remove
    # stop
    # search
# seek
# toggle
