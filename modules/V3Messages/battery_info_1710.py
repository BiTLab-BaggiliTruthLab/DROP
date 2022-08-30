import struct


class battery_info_1710:
    fields = ['ad_v','r_time','ave_I','vol_t','pack_ve','I','r_cap','cap_per','temp','right','l_cell','dyna_cnt','f_cap','out_ctl','out_ctl_f']
    message_type = 1710
    label = 'battery_info'
    _length = -1    #there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        if len(payload) == 46:
            data = {
                'ad_v': struct.unpack('H',payload[0:2])[0],
                'r_time': struct.unpack('H',payload[2:4])[0],
                'ave_I': struct.unpack('f',payload[4:8])[0],
                'vol_t': struct.unpack('f',payload[8:12])[0],
                'pack_ve': struct.unpack('i',payload[12:16])[0],
                'I': struct.unpack('i',payload[16:20])[0],
                'r_cap': struct.unpack('H',payload[20:22])[0],
                'cap_per': struct.unpack('B',payload[22:23])[0],
                'temp': struct.unpack('h',payload[23:25])[0],
                'right': struct.unpack('B',payload[25:26])[0],
                'l_cell': struct.unpack('H',payload[26:28])[0],
                'dyna_cnt': struct.unpack('I',payload[28:32])[0],
                'f_cap': struct.unpack('I',payload[32:36])[0],
                'out_ctl': struct.unpack('f',payload[36:40])[0],
                'out_ctl_f': struct.unpack('f',payload[40:44])[0]
            }
        elif len(payload) == 42:
            data = {  # only a subset of available data; matching with data from len == 46
                'vol_t': struct.unpack('f',payload[0:4])[0],
                'I': struct.unpack('f',payload[4:8])[0],
                'r_time': struct.unpack('H', payload[8:10])[0],
                'ad_v': struct.unpack('H', payload[16:18])[0],
                'cap_per': struct.unpack('B',payload[28:29])[0],
                'temp': struct.unpack('h', payload[29:31])[0],
                'f_cap': struct.unpack('I', payload[36:40])[0],
            }
        elif len(payload) == 106:
            data = {  # only a subset of available data; matching with data from len == 46
                'vol_t': struct.unpack('f',payload[0:4])[0],
                'I': struct.unpack('f',payload[4:8])[0],
                'r_time': struct.unpack('H', payload[8:10])[0],
                'ad_v': struct.unpack('I', payload[20:24])[0],
                'cap_per': struct.unpack('B',payload[32:33])[0],
                'temp': struct.unpack('h', payload[33:35])[0],
            }
        else:
            print(self.label + " missing length definition for length of " + str(len(payload)))
            data = {}

        return data