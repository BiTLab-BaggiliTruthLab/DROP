# Devon Clark
# TXT File Process Class
import os
import csv

class NotCSVFileError(Exception):
    ''' Raised when a file other than a DJI .DAT file is being processed '''
    def __init__(self, in_f):
        self.value = "Ignoring non-DJI CSV file: " + in_f
    def __str__(self):
        return repr(self.value)

class ProcessFRCSV:

    csv_data = {}

    def __init__(self, path):
        self.csv_data = {}
        # TODO: do path checking, add DJI flight record txt files to f_list
        print('Flight record files found:')
        if os.path.isfile(path):
            if self.isFRFile(path):
                self.csv_data[path] = {}
                print(path)
        elif os.path.isdir(path):
            #print(os.listdir(path))
            for e in os.listdir(path):
                if self.isFRFile(os.path.join(path, e)):
                    print(os.path.join(path, e))
                    self.csv_data[os.path.join(path, e)] = {}
        else:
            print(path + ' was not processed because it was not recognized as a file or directory')
            return None

        for f in self.csv_data:
            self.getData(f)

    def isFRFile(self, f):
        if os.path.isfile(f):
            #print(f + ' is a file.')
            # check the latitude and logitude and flight record number (all headers) for existance
            with open(f) as csvfile:
                try:
                    reader = csv.DictReader(csvfile)

                    fields = reader.fieldnames
                    if not ('latitude' in fields) or not ('longitude' in fields) or not ('time(millisecond)' in fields):
                        raise NotCSVFileError(f)
                except NotCSVFileError as e:
                    print(e.value)
                    return False
                except Exception as e:
                    print(e)
                    return False
            return True
        return False

    def getData(self, fname):
        #print('getting data from ' + fname)

        with open(fname) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                time = row['time(millisecond)']          # row['flightTime']time(millisecond)
                lat = row['latitude']
                lon = row['longitude']
                alt = row['altitude(feet)']
                sat = row['satellites']
                volt = row['voltage(v)']
                flyc = row['flycStateRaw']
                if lat != '' and lon != '' and time != '':
                    self.csv_data[fname][time] = [lat, lon, alt, sat, volt, flyc]

    def sortOut(ft_gps_dict):
        ft_list = []
        gps_list = []
        for d in ft_gps_dict:
            ft_list.append(d)

        ft_list.sort()

        for d in ft_list:
            gps_list.append(ft_gps_dict[d])

        return ft_list, gps_list

    def outToFiles(self):
        for f in self.csv_data:
            with open(f + '-output.txt', 'w') as of:
                ft_list, gps_list = self.sortOut(self.csv_data[f])
                for d in range(len(ft_list)):
                    of.write(str(ft_list[d]) + ',' + str(gps_list[d][0]) + ',' + str(gps_list[d][1]) + '\r\n')




'''

'''