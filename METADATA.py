# Song

DEFAULT_TITLE = "Odin"
DEFAULT_ARTIST = "Manowar"
DEFAULT_ALBUM = "The Sons of Odin"
DEFAULT_LENGHT = "3:44"

STR_RETURN = "{artist} - {title} from {album} - {length}"

# Jor0Namp

USR_INP = "What is thy bidding my master :)\n"
WELCOME_MSSG = '''Welcome to Jor0Namp v1.2, the best player since winamp.
For list of avaliable commands enter 'help'\n\n''' + 20 * "=" + "\n"
CMDS = ["add", "current", "exit", "help", "info", "jump", "list", "move",
        "next", "pause", "play", "prev", "remove", "stop", "search", "seek",
        "toggle"]
BAD_INP = "It seems you've entered wrong command, try with some of those :)"
EXECUTE_XMMS2 = "--command=xmms2"
PLAY_SONG = ["lame" "--decode" "{}" "-" "|" "play" "-"]
NOW_PLAYING = "\nYou're listening to {song} - {status}.\n"
PLAY = "playing"
PAUSE = "paused"
TERMINAL = "gnome-terminal"
COMMAND = "--command=xmms2 {cmd}"
HELP = '''
play - play curr song
pause - pause curr song
help - summons this awesome guide
next - calls previous song
prev - calls next song
shuffle - shuffle songs
repeat - repeat playlist
repeats - repeat curr song
'''
