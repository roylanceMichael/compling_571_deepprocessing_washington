# Mike Roylance - roylance@uw.edu
import sys
import nltk

def main():
	# arg variables
	informationContentMeasureFile = sys.argv[1]
	wsdContextsFile = sys.argv[2]

	# optional - compute own ic measure
	# load the information content measure
	informationContentMeasureStream = open(informationContentMeasureFile)
	informationContentMeasure = informationContentMeasureStream.read()

	wsdContextsStream = open(wsdContextsFile)
	wsdContextsLine = wsdContextsStream.readline()

	while wsdContextsLine:
		# do something with line
		wsdContextsLine = wsdContextsStream.readline()

if __name__ == '__main__':
        main()