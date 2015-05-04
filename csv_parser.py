from sys import argv
import csv
import argparse
import os
import ast

parser = argparse.ArgumentParser()
parser.add_argument("-infile", type=str,
                    help="gives input file")
parser.add_argument("-delim", type=str,
                    help="field delimiter")
parser.add_argument("-tq", type=str,
                    help="text qualifier")
args = parser.parse_args()

if not args.infile:
    print "What file would you like to use?"
    args.infile = raw_input("> ")

if not args.delim:
    print "What field delimiter would you like to use? i.e. for space type ' '. Default is tab delimiter."
    args.delim = raw_input("> ")
    if len(args.delim) == 0:
        args.delim = '\t'
    # elif len(args.delim) > 1:
    #     args.delim = repr(args.delim)
        # print ast.literal_eval(raw_input())

if not args.tq:
    print "What text qualifier would you like to use? i.e. for vertical bar type '|'. Default is double quote."
    args.tq = raw_input("> ")
    if len(args.tq) == 0:
        args.tq = '"'

outfile = os.path.splitext(args.infile)[0] + "_out.txt"
target = open(outfile, 'w')
lineCt = 0

with open(args.infile, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=args.delim, quotechar=args.tq, skipinitialspace=True)
     for row in spamreader:
         lineCt += 1
         for item in row:
             item = item.strip()
         target.write(args.delim.join(row))

print "File %r trim spaces complete. Line count: %d" % (args.infile, lineCt)
target.close()
