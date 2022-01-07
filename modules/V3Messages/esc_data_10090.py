import struct

class esc_data_10090:
    fields = ['rfStatus','rfCurrent','rfSpeed','rfVolts','rfTemp','rfPPM_recv','rfV_out','rfPPM_send','lfStatus','lfCurrent','lfSpeed','lfVolts','lfTemp','lfPPM_recv','lfV_out','lfPPM_send','lbStatus','lbCurrent','lbSpeed','lbVolts','lbTemp','lbPPM_recv','lbV_out','lbPPM_send','rbStatus','rbCurrent','rbSpeed','rbVolts','rbTemp','rbPPM_recv','rbV_out','rbPPM_send']
    message_type = 10090
    label = 'esc_data'
    _length = 185
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'rfStatus': struct.unpack('b', payload[0:1])[0],
            'rfCurrent': struct.unpack('h', payload[1:3])[0]/100.0,
            'rfSpeed': struct.unpack('h', payload[3:5])[0],
            'rfVolts': struct.unpack('h', payload[5:7])[0]/10.0,
            'rfTemp': struct.unpack('h', payload[7:9])[0],
            'rfPPM_recv': struct.unpack('H', payload[9:11])[0]/19.2,
            'rfV_out': struct.unpack('h', payload[11:13])[0]/10.0,
            'rfPPM_send': struct.unpack('H', payload[19:21])[0]/19.2,
            'lfStatus': struct.unpack('b', payload[23:24])[0],
            'lfCurrent': struct.unpack('h', payload[24:26])[0]/100.0,
            'lfSpeed': struct.unpack('h', payload[26:28])[0],
            'lfVolts': struct.unpack('h', payload[28:30])[0]/10.0,
            'lfTemp': struct.unpack('h', payload[30:32])[0],
            'lfPPM_recv': struct.unpack('H', payload[32:34])[0]/19.2,
            'lfV_out': struct.unpack('h', payload[34:36])[0]/10.0,
            'lfPPM_send': struct.unpack('H', payload[42:44])[0]/19.2,
            'lbStatus': struct.unpack('b', payload[46:47])[0],
            'lbCurrent': struct.unpack('h', payload[47:49])[0]/100.0,
            'lbSpeed': struct.unpack('h', payload[49:51])[0],
            'lbVolts': struct.unpack('h', payload[51:53])[0]/10.0,
            'lbTemp': struct.unpack('h', payload[53:55])[0],
            'lbPPM_recv': struct.unpack('H', payload[55:57])[0]/19.2,
            'lbV_out': struct.unpack('h', payload[57:59])[0],
            'lbPPM_send': struct.unpack('H', payload[65:67])[0]/19.2,
            'rbStatus': struct.unpack('b', payload[69:70])[0],
            'rbCurrent': struct.unpack('h', payload[70:72])[0]/100.0,
            'rbSpeed': struct.unpack('h', payload[72:74])[0],
            'rbVolts': struct.unpack('h', payload[74:76])[0]/10.0,
            'rbTemp': struct.unpack('h', payload[76:78])[0],
            'rbPPM_recv': struct.unpack('H', payload[78:80])[0]/19.2,
            'rbV_out': struct.unpack('h', payload[80:82])[0]/10.0,
            'rbPPM_send': struct.unpack('H', payload[88:90])[0]/19.2,
        }

        return data