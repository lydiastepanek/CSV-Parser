# CSV Parser

## About
Simple csv parser to trim spaces on a csv file.

## Interesting Features

* doesn't store whole file in memory
* accepts std unless you give it a file name
* collects stats about what data was loaded
* uses argparse and csv libraries

## How to Use

* Download csv_parser.py
* Run with input filename
* Can pass two optional extra arguments for field delimiter, and text qualifier
* Command prompt will ask for delimiter and text qualifier, will default to tab delimited and " if none given

## Examples

* With no arguments
  * python csv-parser3.py
* With some arguments
  * python csv-parser3.py -infile '/Users/lydiastepanek/Desktop/randomjs.js'
* With all arguments
  * python csv-parser3.py -infile '/Users/lydiastepanek/Desktop/randomjs.js' -delim ',' -tq '|'

## To Do

* Allow '\t' and other escaped characters as delimiter
* Make python library
