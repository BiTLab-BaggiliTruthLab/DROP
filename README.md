# Devon Clark
# DJIDATParse

usage: DJIDATParse.py [-h] [-o OUTPUT] [-t T] [-f] input

positional arguments:
  input                 path to input DAT file or directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output CSV File or directory. If none is
                        specified the output will be saved in the current
                        directory.
  -t T                  path to input Flight Record CSV file or directory
  -f, --force           force processing of file(s) if correct file header is
                        not found
