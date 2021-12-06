#TODO post-processing: evtl komplizierte Berechnungen aus RecIMU nachholen (extended by IMU120_2048)
import struct


class IMU_ATTI_2048:
    fields = ['longRad','latRad','longitudeDegrees','latitudeDegrees','baroPress','accelX', 'accelY','accelZ','gyroX',
              'gyroY','gyroZ','baroAlti','quatW','quatX','quatY', 'quatZ','ag_X','ag_Y','ag_Z','velN','velE','velD','gb_X',
              'gb_Y','gb_Z','magX', 'magY','magZ','imuTemp','ty','tz','sensor_stat','filter_stat','numSats','atti_cnt']
    message_type = 2048
    label = 'imu_atti'
    _length = 120
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'longRad': struct.unpack('d', payload[0:8])[0],
            'latRad': struct.unpack('d', payload[8:16])[0],
            'baroPress': struct.unpack('f', payload[16:20])[0],         #TODO baroPress vs. alti_00 (16)
            'accelX': struct.unpack('f', payload[20:24])[0],
            'accelY': struct.unpack('f', payload[24:28])[0],
            'accelZ': struct.unpack('f', payload[28:32])[0],
            'gyroX': struct.unpack('f', payload[32:36])[0],
            'gyroY': struct.unpack('f', payload[36:40])[0],
            'gyroZ': struct.unpack('f', payload[40:44])[0],
            'baroAlti': struct.unpack('f', payload[44:48])[0],          #TODO baroAlti vs. press_00 (44)
            'quatW': struct.unpack('f', payload[48:52])[0],
            'quatX': struct.unpack('f', payload[52:56])[0],
            'quatY': struct.unpack('f', payload[56:60])[0],
            'quatZ': struct.unpack('f', payload[60:64])[0],
            'ag_X': struct.unpack('f', payload[64:68])[0],
            'ag_Y': struct.unpack('f', payload[68:72])[0],
            'ag_Z': struct.unpack('f', payload[72:76])[0],
            'velN': struct.unpack('f', payload[76:80])[0],
            'velE': struct.unpack('f', payload[80:84])[0],
            'velD': struct.unpack('f', payload[84:88])[0],
            'gb_X': struct.unpack('f', payload[88:92])[0],
            'gb_Y': struct.unpack('f', payload[92:96])[0],
            'gb_Z': struct.unpack('f', payload[96:100])[0],
            'magX': struct.unpack('h', payload[100:102])[0],
            'magY': struct.unpack('h', payload[102:104])[0],
            'magZ': struct.unpack('h', payload[104:106])[0],
            'imuTemp': struct.unpack('h', payload[106:108])[0],
            'ty': struct.unpack('h', payload[108:110])[0],
            'tz': struct.unpack('h', payload[110:112])[0],
            'sensor_stat': struct.unpack('H', payload[112:114])[0],
            'filter_stat': struct.unpack('H', payload[114:116])[0],
            'numSats': struct.unpack('H', payload[116:118])[0],           #TODO = svn_00 ?
            'atti_cnt': struct.unpack('H', payload[118:120])[0]
        }
        return data