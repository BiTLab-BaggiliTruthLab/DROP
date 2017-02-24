# Devon Clark
# DROP
# This script requires Python 3
# To run this tool use the following command:
# python DROP.py path/to/FLYXXX.DAT

import sys
import os
import datetime
import csv
import struct
from modules.Message import Message
from modules.ProcessFRCSV import ProcessFRCSV
import hashlib
import argparse
from modules import simplekml

DEBUG = False

curr_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('input', help='path to input DAT file or directory')
parser.add_argument('-o', '--output', help='path to output CSV File or directory. If none is specified the output will be saved in the current directory.')
parser.add_argument('-t', help='path to input Flight Record CSV file or directory')
parser.add_argument('-f', '--force', help='force processing of file(s) if correct file header is not found', action='store_true')

################################################# Custom Exceptions (Put in a seperate file later)

class NotDATFileError(Exception):
    ''' Raised when a file other than a DJI .DAT file is being processed '''
    def __init__(self, in_f):
        self.value = "Attempted to open non-DAT file: " + in_f
    def __str__(self):
        return repr(self.value)

class CorruptPacketError(Exception):
    def __init__(self, value="The Packet is corrupt."):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NoNewPacketError(Exception):
    def __init__(self, bytestr, offset):
        self.value = 'Expected start of packet (0x55) but found ' + str(bytestr) + ' instead. Located at byte ' + str(offset) + ' of input file.'
    def __str__(self):
        return repr(self.value)

################################################# Process command line args

args = parser.parse_args()
in_arg = args.input
out_arg = args.output
in_dir = ''
out_path = ''
in_files_list = []
if os.path.isfile(in_arg):          # file input
    in_files_list.append(in_arg)
    if out_arg == None:             # output not specified
        spl_path = os.path.split(in_arg)
        out_path = spl_path[len(spl_path)-1].split('.')[0] + '-Output.csv'
    else:    # file or directory output     os.path.isfile(out_arg) or os.path.isdir(out_arg)
        out_path = out_arg
elif os.path.isdir(in_arg):         # directory input
    in_files_list = [f for f in os.listdir(in_arg) if os.path.isfile(os.path.join(in_arg, f))]
    in_dir = in_arg

    if out_arg == None:             # output not specified
        out_path = curr_dir
    elif os.path.isdir(out_arg):
        out_path = out_arg
    else:
        print('Error: Output must be a valid directory or None.')
        exit()
else:                               # not a valid file or directory
    print('Error: Input must be a valid file or directory.')
    exit()
    
in_tf = args.t      # path to input text file(s)
force = args.force
if force:
    print('*** WARNING: The FORCE flag has been set. ALL files will be processed (not just standard DJI DAT files). ***')

################################################# Process TXT files

txtfiles = None
if in_tf != None:
    txtfiles = ProcessFRCSV(in_tf)

#################################################

for ifn in in_files_list:
    if os.path.isdir(out_path):
        spl_path = os.path.split(ifn)
        out_fn = os.path.join(out_path, spl_path[len(spl_path)-1].split('.')[0] + '-Output.csv')
    else:
        out_fn = out_path

    in_fn = os.path.join(in_dir, ifn)
    # *** make sure to read file meta data BEFORE doing anything with the file ;)
    meta = os.stat(in_fn)

    b_hashmd5 = hashlib.md5()
    b_hashsha1 = hashlib.sha1()
    b_hashsha512 = hashlib.sha512()
    with open(in_fn, 'rb') as afile:
        buf = afile.read()
        b_hashmd5.update(buf)
        b_hashsha1.update(buf)
        b_hashsha512.update(buf)
    #********************

    in_file = open(in_fn, 'rb')
    try:
        file_header = in_file.read(128)
        #print(file_header)
        build = struct.unpack('5s', file_header[16:21])[0]     # attempt to read the word "BUILD" in the file header
        #print(build)
        #print(b"BUILD".decode('ascii'))
        if build.decode('ascii') != b"BUILD".decode('ascii'):
            if not force:
                raise NotDATFileError(in_fn)
            else:
                print('*** WARNING: ' + in_fn + ' is not a recognized DJI DAT file but will be processed anyway because the FORCE flag was set. ***')
                in_file.seek(0)     # set the pointer to the beginging of the file because this is an unrecognized file type and we dont want to risk missing data ;)
    except NotDATFileError as e:
        print(e.value)
        continue
    except Exception as e:
        print(e)
        continue

    out_file = open(out_fn, 'w')
    #---------------------

    writer = csv.DictWriter(out_file, lineterminator='\n', fieldnames=Message.fieldnames)
    writer.writeheader()

    p_subtypes = []
    alternateStructure = False
    try:
        strt_datetime = datetime.datetime.now()    # Time we started processing the DAT file

        print('\n=====================================================')
        print('Processing Date/Time Start: ' + strt_datetime.strftime('%Y-%m-%d %H:%M:%S'))
        print('Command Used: ' + ' '.join(sys.argv))
        print('Input File Name: ' + in_fn)
        print('Output File Name: ' + out_fn)
        #print('File Access Rights: ' + str(meta.st_mode))
        #print('I-node: ' + str(meta.st_ino))
        #print('Device Number: ' + str(meta.st_dev))
        #print('User ID: ' + str(meta.st_uid))
        #print('Group ID: ' + str(meta.st_gid))
        print('File Size (MB): ' + str(os.path.getsize(in_fn)))
        #print('Last Access Time: ' + datetime.datetime.fromtimestamp(meta.st_atime).strftime('%Y-%m-%d %H:%M:%S'))
        #print('Last Modified Time: ' + datetime.datetime.fromtimestamp(meta.st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
        #print('Last Changed Time: ' + datetime.datetime.fromtimestamp(meta.st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
        print('BEFORE MD5 Hash Digest: ' + str(b_hashmd5.hexdigest()))
        print('BEFORE SHA1 Hash Digest: ' + str(b_hashsha1.hexdigest()))
        print('BEFORE SHA512 Hash Digest: ' + str(b_hashsha512.hexdigest()) + '\n')
        print('Analizing DAT File...')

        # *** Pointer has been set to byte 128 (unless we are forcing an non-standard DAT file) 
        # to start reading (the msg start byte of the first record, we already read the file header)
        byte = in_file.read(1)   # read the first byte of the first message

        if byte[0] != 0x55:
            alternateStructure = True
        message = None
        message = Message(meta)      # create a new, empty message
        
        start_issue = True
        while len(byte) != 0:

            try:
                if byte[0] != 0x55:
                    raise NoNewPacketError(byte, in_file.tell())

                start_issue = True  # reset start issue here
                pktlen = 0xFF & int(in_file.read(1)[0])    # length of the packet
                padding = in_file.read(1)                  # padding
                if padding[0] == 0:
                    header = in_file.read(7)

                    current = in_file.tell()
                    in_file.seek(current + pktlen - 10)     # seek to the byte that should be the starting byte of the next packet
                    #print('read from: ' + str(current + pktlen - 10))
                    next_start = in_file.read(1)
                    if len(next_start) <= 0:
                        break
                    if next_start[0] != 0x55:          # something is wrong with the packet length
                        #print('error at byte: ' + str(current + pktlen - 10 + 1))
                        in_file.seek(current)               # reset file pointer to just after header
                        byte = in_file.read(1)
                        raise CorruptPacketError("Packet length error at byte " + str(current-9))
                    in_file.seek(current)                   # go back to where we were if packet length is ok
                    
                    payload = in_file.read(pktlen - 10)
                    thisPacketTickNo = struct.unpack('I', header[3:7])[0]
                    if thisPacketTickNo < 0:
                        # Legacy code from DatCon: (thisPacketTickNo < 0) or 
                        # ((alternateStructure) and (thisPacketTickNo > 4500000)) or 
                        # ((not alternateStructure) and (thisPacketTickNo > 1500000))
                        byte = padding
                        raise CorruptPacketError("Corrupted tick number. Tick No: " + str(thisPacketTickNo) + ", alternate structure? " + str(alternateStructure))
                    if pktlen == 0:
                        byte = padding
                        raise CorruptPacketError()
                    if message.tickNo == None:
                        message.setTickNo(thisPacketTickNo)

                    message.writeRow(writer, thisPacketTickNo)

                    message.addPacket(pktlen, header, payload)
                    byte = in_file.read(1)
                else:
                    byte = padding
            except CorruptPacketError as e:
                print(e.value)
            except NoNewPacketError as e:
                if start_issue:     # first time around the loop with this problem
                    print(e.value)
                    start_issue = False     # set to false so we dont flood the screen with error statements
                byte = in_file.read(1)
            except Exception as e:
                print(e)
        writer.writerow(message.getRow())           # write the last row
    finally:
        end_dattime = datetime.datetime.now()
        t_diff = end_dattime - strt_datetime
        log_file = open('processlog.txt', 'a')
        log_file.write('=====================================================\n')
        log_file.write('Processing Date/Time Start: ' + strt_datetime.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        log_file.write('Command Used: ' + ' '.join(sys.argv) + '\n')
        log_file.write('Input File Name: ' + in_fn + '\n')
        log_file.write('Output File Name: ' + out_fn + '\n')
        log_file.write('Number of Records Processed: ' + str(message.packetNum) + '\n')
        #log_file.write('File Access Rights: ' + str(meta.st_mode) + '\n')
        #log_file.write('I-node: ' + str(meta.st_ino) + '\n')
        #log_file.write('Device Number: ' + str(meta.st_dev) + '\n')
        #log_file.write('User ID: ' + str(meta.st_uid) + '\n')
        #log_file.write('Group ID: ' + str(meta.st_gid) + '\n')
        log_file.write('File Size (MB): ' + str(os.path.getsize(in_fn)) + '\n')
        #log_file.write('Last Access Time: ' + datetime.datetime.fromtimestamp(meta.st_atime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        #log_file.write('Last Modified Time: ' + datetime.datetime.fromtimestamp(meta.st_mtime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        #log_file.write('Last Changed Time: ' + datetime.datetime.fromtimestamp(meta.st_ctime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        log_file.write('Processing Date/Time End: ' + end_dattime.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        log_file.write('Processing Time: ' + str(t_diff) + '\n')
        log_file.write('BEFORE MD5 Hash Digest: ' + str(b_hashmd5.hexdigest()) + '\n')
        log_file.write('BEFORE SHA1 Hash Digest: ' + str(b_hashsha1.hexdigest()) + '\n')
        log_file.write('BEFORE SHA512 Hash Digest: ' + str(b_hashsha512.hexdigest()) + '\n')

        in_file.close()
        out_file.close()

        if txtfiles != None:
            print('\n============== DAT to TXT Correlation ==============')
            #message.outToFile(in_fn)
            dat_ft_records = len(message.gps_fr_dict)
            print('Number of DAT flight time records: ' + str(dat_ft_records))
            for f in txtfiles.csv_data:
                ft_matches = 0
                gps_matches = 0

                dat_matches = {}
                txt_matches = {}

                for d in message.gps_fr_dict:
                    #print('flight time: ' + str(d))
                    #print('csv = ' + str(txtfiles.csv_data[f].get(str(d), None)) + ', dat = ' + str(message.gps_fr_dict[d]))
                    if str(d) in txtfiles.csv_data[f]:
                        #if txtfiles.csv_data[f][d] == message.gps_fr_dict[d]:
                        #print('found a match for flight time: csv = ' + str(txtfiles.csv_data[f][str(d)]) + ', dat = ' + str(message.gps_fr_dict[d]))
                        # * * * * * * * * * * * * * * * * * * * * * *
                        dat_matches[d] = message.gps_fr_dict[d]
                        txt_matches[str(d)] = txtfiles.csv_data[f][str(d)]

                        ft_matches += 1
                        csv_data = txtfiles.csv_data[f][str(d)]
                        dat_data = message.gps_fr_dict[d]

                        lat_cnt = 0
                        csv_lat = csv_data[0].split('.')
                        dat_lat = str(dat_data[0]).split('.')
                        if csv_lat[0] == dat_lat[0]:            # check before the decimal point
                            for i in range(len(csv_lat[1])):
                                if i < len(dat_lat[1]):
                                    if csv_lat[1][i] == dat_lat[1][i]:
                                        lat_cnt += 1

                        lon_cnt = 0
                        csv_lon = csv_data[1].split('.')
                        dat_lon = str(dat_data[1]).split('.')
                        if csv_lon[0] == dat_lon[0]:            # check before the decimal point
                            for i in range(len(csv_lon[1])):
                                if i < len(dat_lon[1]):
                                    if csv_lon[1][i] == dat_lon[1][i]:
                                        lon_cnt += 1

                        if lat_cnt >= 5 and lon_cnt >= 5:
                            gps_matches += 1
                        #else:
                            #print('low correlation: lat_cnt = ' + str(lat_cnt) + ', lon_cnt = ' + str(lon_cnt))

                        # * * * * * * * * * * * * * * * * * * * * * *
                if dat_ft_records != 0:
                    print('            Number of flight time matches: ' + str(ft_matches))
                    print('Number of GPS matches (given flight time): ' + str(gps_matches))
                    if ft_matches > 0:
                        print(in_fn + ' --> ' + f + ' Confidence: ' + str((gps_matches / ft_matches)*100) + '%\n')
                        log_file.write(in_fn + ' --> ' + f + ' Confidence: ' + str((gps_matches / ft_matches)*100) + '%')
                        #print(in_fn + ' --> ' + f + ' Overall correlation: ' + str((gps_matches / dat_ft_records)*100) + '%')
                    else:
                        print(in_fn + ' --> ' + f + ' Confidence: 0.0%\n')
                        log_file.write(in_fn + ' --> ' + f + ' Confidence: 0.0%')

                if DEBUG == True:
                    with open('out.txt', 'w') as o_file:
                        o_file.write('time(milisecond),DAT_Lat,DAT_Lon,DAT_alt,DAT_sats,DAT_volt,DAT_flyc,TXT_Lat,TXT_Lon,TXT_alt,TXT_sats,TXT_volt,TXT_flyc\r\n')

                        #print(dat_matches[10100])
                        dat_ft_list, dat_list = ProcessFRCSV.sortOut(dat_matches)
                        txt_ft_list, txt_list = ProcessFRCSV.sortOut(txt_matches)

                        for i in range(0, len(dat_ft_list)):
                            o_file.write(str(dat_ft_list[i]) + ',' + str(dat_list[i][0]) + ',' + str(dat_list[i][1]) + ',' + str(dat_list[i][2]) + ',' + 
                                str(dat_list[i][3]) + ',' + str(dat_list[i][4]) + ',' + str(dat_list[i][5]) + ',' + 
                                str(txt_list[i][0]) + ',' + str(txt_list[i][1]) + ',' + str(txt_list[i][2]) + ',' + 
                                str(txt_list[i][3]) + ',' + str(txt_list[i][4]) + ',' + str(txt_list[i][5]) + '\r\n')

        a_hashmd5 = hashlib.md5()
        a_hashsha1 = hashlib.sha1()
        a_hashsha512 = hashlib.sha512()
        with open(in_fn, 'rb') as afile:
            buf = afile.read()
            a_hashmd5.update(buf)
            a_hashsha1.update(buf)
            a_hashsha512.update(buf)
        log_file.write('AFTER MD5 Hash Digest: ' + str(a_hashmd5.hexdigest()) + '\n')
        log_file.write('AFTER SHA1 Hash Digest: ' + str(a_hashsha1.hexdigest()) + '\n')
        log_file.write('AFTER SHA512 Hash Digest: ' + str(a_hashsha512.hexdigest()) + '\n')

        log_file.close()
        print('AFTER MD5 Hash Digest: ' + str(a_hashmd5.hexdigest()))
        print('AFTER SHA1 Hash Digest: ' + str(a_hashsha1.hexdigest()))
        print('AFTER SHA512 Hash Digest: ' + str(a_hashsha512.hexdigest()))
        if b_hashmd5.hexdigest() != a_hashmd5.hexdigest() or b_hashsha1.hexdigest() != a_hashsha1.hexdigest() or b_hashsha512.hexdigest() != a_hashsha512.hexdigest():
            print("*** HASHES DO NOT MATCH - FILE MAY HAVE BEEN MODIFIED ***")
        else:
            print("Hashes match")
        print('Processing Date/Time End: ' + end_dattime.strftime('%Y-%m-%d %H:%M:%S'))
        print('Processing Time: ' + str(t_diff))
        print('=====================================================\n')

print("Processing complete.")
    
