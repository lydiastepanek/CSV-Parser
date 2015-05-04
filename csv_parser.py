from sys import argv
import csv

script, infile, inputDelim, inputQuote = argv
# python csv_parser.py randomjs.js ' ' '|'
# python csv_parser.py '/Users/lydiastepanek/Desktop/randomjs.js' ' ' '|'

# target = open(infile + "_output.txt", 'w')
target = open(infile + "_out.txt", 'w')
lineCt = 0
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# wholetext = txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")

# lineCt =
# indata = txt.readline()

# with open(filename) as infile:
#     for line in infile:
#         target.write(line)
#         target.write("\n")
#
with open(infile, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=inputDelim, quotechar=inputQuote, skipinitialspace=True)
    #  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         lineCt += 1
         for item in row:
             item = item.strip()
         target.write('|'.join(row))

print "Line count: %d" % lineCt
target.close()
