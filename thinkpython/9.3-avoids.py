from itertools import combinations
from collections import OrderedDict, _itemgetter
from operator import itemgetter

def avoids(words, escapes):
	goodwords = []
	for word in words:
		isin = False
		for i in escapes:
			if i in word:
				isin = True
				continue
		if not isin:
			goodwords.append(word)

	return len(goodwords)


def generate_five():
	abc = list('abcdefghijklmnopqrstuvwxyz')
	escapes = combinations(abc, 5)
	return escapes



combi_dict = {}

def process_all(words, escapes):
	for escape in escapes:
		combi_dict[escape] = avoids(words, escape)
	return combi_dict

final = {}
def low5(dictionary):
	lowest = dict(sorted(dictionary.iteritems(), key=itemgetter(1), reverse=True)[:5])
	return lowest



# words = ['aahs', 'aal', 'aalii', 'aaliis', 'aals', 'aardvark', 'aardvarks', 'aardwolf', 'aardwolves', 'aas', 'aasvogel']
# words = str(raw_input('> ')).lower().split()

def readwords():
	words = []
	for line in open('words.txt', 'r').read().split('\n'):
		words.append(line)

	return words

#escapes = ['abcde', 'bcdef', 'cdefgh']
# escapes = generate_five()

print low5(process_all(readwords(), generate_five()))

