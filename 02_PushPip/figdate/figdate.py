from time import strftime
from pyfiglet import Figlet
import locale

def date(format="%Y %d %b, %A", font="graceful"):
    f = Figlet(font=font)
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    print(f.renderText(strftime(format)))
