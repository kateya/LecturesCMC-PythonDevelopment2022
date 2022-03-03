from argparse import ArgumentParser
from .bullcows import gameplay, ask, inform
import urllib.request

parser = ArgumentParser()
parser.add_argument("dictionary", type=str, nargs=1)
parser.add_argument("strlen", type=int, default=5, nargs='?')
args = parser.parse_args()

response = urllib.request.urlopen(args.dictionary[0])
data = response.read()
text = data.decode('utf-8')
words = text.split()
strlen_words = [w for w in words if len(w) == args.strlen]

print(gameplay(ask, inform, strlen_words))