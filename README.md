# DROP - DROne Parser
### Devon Clark - 2016
### [UNHcFREG](https://www.unhcfreg.com/)

This open source forensics tool can be used to extract data from FLY???.DAT files found on DJI Phantom III drone internal storage. It requires Python 3 to run. Additionally this tool will also attempt to form a correlation between the input DAT file and an optionally specified DJI GO generated flight record file or set of files.

File structure, packet structure, and payload decryption was understood through reverse engineering the [DatCon](https://datfile.net/) application

**usage**: `python DROP.py [-h] [-o OUTPUT] [-t T] [-f] input`

**positional arguments**:

  `input`               path to input DAT file or directory

**optional arguments**:

  `-h`, `--help`        show help message and exit
  
  `-o OUTPUT`, `--output OUTPUT`
                        path to output CSV File or directory. If none is
                        specified the output will be saved in the current
                        directory.
                        
  `-t T`                path to input Flight Record CSV file or directory
  
  `-f`, `--force`       force processing of file(s) if correct file header is
                        not found
# Extended Version for V3 .DAT files
### Andreas Hellmich, Annika Knepper - 2022
### [andreas.hellmich@fau.de](mailto:andreas.hellmich@fau.de)

The tool has been modified to also support the .DAT files found on DJI Phantom 4 Advanced drones (and similar models with limited compatibility).\
The usage has therefore been changed to support drones using the V3 .DAT file format:

**usage**: `python DROP.py [-h] [-o OUTPUT] [-t T] [-f] [-a] [-g] [-v] [-j] input`

**positional arguments**:

  `input`               path to input DAT file or directory

**optional arguments**:

  `-h`, `--help`        show help message and exit
  
  `-o OUTPUT`, `--output OUTPUT`
                        path to output directory. If none is
                        specified the output will be saved in the current
                        directory. A single file can no longer be set, as the application might create multiple files per input file.
                        
  `-t T`                path to input Flight Record CSV file or directory
  
  `-f`, `--force`       force processing of file(s) if correct file header is
                        not found

  `-a`                  creates additional output files containing all unknown messages

  `-g`                  creates additional output files containing only GPS messages

  `-v`                  includes all messages in standard output file, normally only the more necessary information is added to limit file size.

  `-j`                  creates additional JSON output files for use within the `DroneWebGui`

### further extending the V3 capabilities

To further extend the capabilities of decoding V3 .DAT files additional message files can be added within the `V3Messages` directory. Therefor the `00example.py` file can be copied and modified.\
The available types are only implemented to support the Phantom 4 Advanced, if the same message type with another payload length is needed, you can include this into the parse function, as already done in `battery_info_1710.py`.