from sys import argv
import csv

script, inputFilename, inputDelim, inputQuote = argv
# python csv_parser.py lydia

target = open(inputFilename + "_output.txt", 'w')
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
with open(inputFilename, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=inputDelim, quotechar=inputQuote)
    #  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         lineCt += 1
         print inputDelim.join(row)
         target.write(inputDelim.join(row))

print "Line count: %d" % rowCt
target.close()
