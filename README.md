# DROP - DROne Parser
### Devon Clark

This open source tool can be used to extract data from FLY???.DAT files found on DJI Phantom III drone internal storage. It requires Python 3 to run.

Decryption and decoding methods were obtained through reverse engineering the [DatCon](https://datfile.net/) application

usage: `python DJIDATParse.py [-h] [-o OUTPUT] [-t T] [-f] input`

positional arguments:

  `input`               path to input DAT file or directory

optional arguments:

  `-h`, `--help`        show this help message and exit
  
  `-o OUTPUT`, `--output OUTPUT`
                        path to output CSV File or directory. If none is
                        specified the output will be saved in the current
                        directory.
                        
  `-t T`                path to input Flight Record CSV file or directory
  
  `-f`, `--force        force processing of file(s) if correct file header is
                        not found
