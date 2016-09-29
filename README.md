# DROP - DROne Parser
### Devon Clark

This open source forensics tool can be used to extract data from FLY???.DAT files found on DJI Phantom III drone internal storage. It requires Python 3 to run. Additionally this tool will also attempt to form a correlation between the input DAT file and an optionally specified DJI GO generated flight record file or set of files.

File structure, packet structure, and payload decryption was understood through reverse engineering the [DatCon](https://datfile.net/) application

**usage**: `python DJIDATParse.py input [-h] [-o OUTPUT] [-t T] [-f]`

**positional arguments**:

  `input`               path to input DAT file or directory

**optional arguments**:

  `-h`, `--help`        show this help message and exit
  
  `-o OUTPUT`, `--output OUTPUT`
                        path to output CSV File or directory. If none is
                        specified the output will be saved in the current
                        directory.
                        
  `-t T`                path to input Flight Record CSV file or directory
  
  `-f`, `--force        force processing of file(s) if correct file header is
                        not found
