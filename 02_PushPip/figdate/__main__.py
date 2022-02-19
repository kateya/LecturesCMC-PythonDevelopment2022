from argparse import ArgumentParser
from .figdate import date

parser = ArgumentParser()
parser.add_argument("format", default="%Y %d %b, %A", nargs='?')
parser.add_argument("font", default="graceful", nargs='?')
args = parser.parse_args()

date(args.format, args.font)