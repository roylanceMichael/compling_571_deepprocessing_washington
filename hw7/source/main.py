# Mike Roylance - roylance@uw.edu
import sys
import nltk

def main():
	# arg variables
	grammarFile = "file:" + sys.argv[1]
	grammar = sys.argv[2]

	# create grammar
	grammar = nltk.data.load(grammarFile)
	parser = nltk.parse.EarleyChartParser(grammar)

	# read sentences two at a time
	

if __name__ == '__main__':
        main()