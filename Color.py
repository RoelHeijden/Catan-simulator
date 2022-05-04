
class Color:

    def __init__(self):
        pass

    def bold(self, s):
        return '\033[1m' + s + '\033[0m'

    def underline(self, s):
        return '\033[4m' + s + '\033[0m'

    def blocked(selfself, s, resource):
        end = '\033[0m'
        switcher = {
            "wood": '\033[107;92m' + s + end,
            "wheat": '\033[107;33m' + s + end,
            "sheep": '\033[107;32m' + s + end,
            "brick": '\033[107;31m' + s + end,
            "ore": '\033[107m' + s + end,
        }
        return switcher.get(resource)

    def color(self, s, color):
        end = '\033[0m'
        switcher = {
            "white": '\033[30m' + s + end,
            "red": '\033[31m' + s + end,
            "green": '\033[32m' + s + end,
            "yellow": '\033[33m' + s + end,
            "blue": '\033[34m' + s + end,
            "purple": '\033[35m' + s + end,
            "cyan": '\033[36m' + s + end,
            "gray": '\033[37m' + s + end,

            "dark gray": '\033[90m' + s + end,
            "red2": '\033[91m' + s + end,
            "green2": '\033[92m' + s + end,
            "yellow2": '\033[93m' + s + end,
            "blue2": '\033[94m' + s + end,
            "pink": '\033[95m' + s + end,
            "cyan2": '\033[96m' + s + end,
            "black": '\033[97m' + s + end,

            "wood": '\033[92m' + s + end,
            "wheat": '\033[33m' + s + end,
            "sheep": '\033[32m' + s + end,
            "brick": '\033[31m' + s + end,
            "ore": s
        }
        return switcher.get(color)

    def background_color(self, s, color, with_end=True):
        end = '\033[0m'
        switcher = {
            "white": '\033[40m' + s,
            "red": '\033[41m' + s,
            "green": '\033[42m' + s,
            "yellow2": '\033[43m' + s,
            "blue": '\033[44m' + s,
            "purple": '\033[45m' + s,
            "cyan": '\033[46m' + s,
            "gray": '\033[47m' + s,

            "dark gray": '\033[100m' + s,
            "red2": '\033[101m' + s,
            "green2": '\033[102m' + s,
            "yellow": '\033[103m' + s,
            "blue2": '\033[104m' + s,
            "pink": '\033[105m' + s,
            "cyan2": '\033[106m' + s,
            "black": '\033[107m' + s,
        }
        if not with_end:
            return switcher.get(color)
        return switcher.get(color) + end

    def show_all(self, s="reee", n=150):
        for i in range(n):
            print('\033[' + str(i) + 'm' + s + '\033[0m', i)
