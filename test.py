from subprocess import Popen, call
from time import sleep


# pid = Popen(args=[
#         "gnome-terminal", "--command=python /home/jor0/101-v5/week07/modulesNpandas/music_player/Jor0Namp.py"]).pid
# print(pid)
# call["xmms2", "play"]

pid = Popen(args=[
        "gnome-terminal", "--command=xmms2 pause"]).pid

# pid = Popen(args=[
#         "gnome-terminal", "--command=play"]).pid

# call["lame", "--decode", "home/jor0/Music/Upsurt/Usurd - 01 - Popfolk.mp3 -", "|", " play -"]

sleep(5)
