from sys import argv
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('strings', metavar='N', type=str, nargs='+')

args = parser.parse_args()

if len(args.strings) > 0:
    infile = args.strings[0]
else:
    print "What file would you like to use?"
    infile = raw_input("> ")

if len(args.strings) > 1:
    inputDelim = args.strings[1]
else:
    print "What field delimiter would you like to use? i.e. for space type ' '. Default is tab delimiter."
    inputDelim = raw_input("> ")
    if len(inputDelim) == 0:
        inputDelim = '\t'

if len(args.strings) > 2:
    inputQuote = args.strings[2]
else:
    print "What text qualifier would you like to use? i.e. for vertical bar type '|'. Default is double quote."
    inputQuote = raw_input("> ")
    if len(inputQuote) == 0:
        inputQuote = '"'

target = open(infile + "_out.txt", 'w')
lineCt = 0

with open(infile, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=inputDelim, quotechar=inputQuote, skipinitialspace=True)
     for row in spamreader:
         lineCt += 1
         for item in row:
             item = item.strip()
         target.write('|'.join(row))

print "%r line count: %d" % (infile, lineCt)
target.close()
