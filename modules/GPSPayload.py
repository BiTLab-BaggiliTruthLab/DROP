# Devon Clark
# GPS Class
import struct
import math
from modules.Quaternion import Quaternion

class GPSPayload:
    fields = ['latitude', 'longitude', 'altitude', 'accelX', 'accelY', 'accelZ', 'gyroX', 'gyroY', 'gyroZ', 'baroAlt', 'quatW', 'quatX',
    'quatY', 'quatZ', 'errorX', 'errorY', 'errorZ', 'velN', 'velE', 'velD', 'x4', 'x5', 'x6', 'magX', 'magY', 'magZ', 'imuTemp', 'i2', 'i3',
    'i4', 'i5', 'satnum', 'vel', 'velH', 'error', 'accel', 'magMod', 'gyro', 'roll', 'pitch', 'yaw', 'yaw360', 'magYawX', 

    'velGPS-velH', 'totalGyroZ', 'distanceTravelled', 'directionOfTravel', 'directionOfTravelTrue'  # to be implemented in message class
    ]
    _type = 0xcf
    _subtype = 0x01
    _length = 0x84
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def convertpos(self, pos):
        # convert position from radians to degrees
        return math.degrees(pos)

    def mtoft(self, meter):
        # convert meters to feet
        return (meter * 3.2808)

    def parse(self, payload):
        #temp_file.write('packet has GPS\n')
        data = {}

        longitude = struct.unpack('d', payload[0:8])[0]     # parse double (float) longitude
        data['longitude'] = self.convertpos(longitude)

        latitude = struct.unpack('d', payload[8:16])[0]     # parse double (float) latitude
        data['latitude'] = self.convertpos(latitude)

        altitude = struct.unpack('f', payload[16:20])[0]    # parse float altitude
        data['altitude'] = self.mtoft(altitude)

        data['accelX'] = struct.unpack('f', payload[20:24])[0]
        data['accelY'] = struct.unpack('f', payload[24:28])[0]
        data['accelZ'] = struct.unpack('f', payload[28:32])[0]
        data['accel'] = float(math.sqrt(math.pow(data['accelX'],2) + math.pow(data['accelY'],2) + math.pow(data['accelZ'],2)))

        data['gyroX'] = struct.unpack('f', payload[32:36])[0]
        data['gyroY'] = struct.unpack('f', payload[36:40])[0]
        data['gyroZ'] = struct.unpack('f', payload[40:44])[0]
        data['gyro'] = float(math.sqrt(math.pow(data['gyroX'],2) + math.pow(data['gyroY'],2) + math.pow(data['gyroZ'],2)))

        data['baroAlt'] = self.mtoft(struct.unpack('f', payload[44:48])[0])

        data['quatW'] = struct.unpack('f', payload[48:52])[0]
        data['quatX'] = struct.unpack('f', payload[52:56])[0]
        data['quatY'] = struct.unpack('f', payload[56:60])[0]
        data['quatZ'] = struct.unpack('f', payload[60:64])[0]
        q = Quaternion(data['quatX'], data['quatY'], data['quatZ'], data['quatW'])
        eAngs = q.toEuler()
        data['pitch'] = math.degrees(eAngs[0])
        data['roll'] = math.degrees(eAngs[1])
        data['yaw'] = math.degrees(eAngs[2])
        data['yaw360'] = (data['yaw'] + 360.0) % 360.0

        data['errorX'] = struct.unpack('f', payload[64:68])[0]
        data['errorY'] = struct.unpack('f', payload[68:72])[0]
        data['errorZ'] = struct.unpack('f', payload[72:76])[0]
        data['error'] = float(math.sqrt(math.pow(data['errorX'],2) + math.pow(data['errorY'],2) + math.pow(data['errorZ'],2)))

        data['velN'] = struct.unpack('f', payload[76:80])[0]
        data['velE'] = struct.unpack('f', payload[80:84])[0]
        data['velD'] = struct.unpack('f', payload[84:88])[0]
        data['vel'] = float(math.sqrt(math.pow(data['velN'],2) + math.pow(data['velE'],2) + math.pow(data['velD'],2)))
        data['velH'] = float(math.sqrt(math.pow(data['velN'],2) + math.pow(data['velE'],2)))

        x4 = struct.unpack('f', payload[88:92])[0]
        x5 = struct.unpack('f', payload[92:96])[0]
        x6 = struct.unpack('f', payload[96:100])[0]

        data['magX'] = struct.unpack('h', payload[100:102])[0]
        data['magY'] = struct.unpack('h', payload[102:104])[0]
        data['magZ'] = struct.unpack('h', payload[104:106])[0]
        data['magMod'] = float(math.sqrt(math.pow(data['magX'],2) + math.pow(data['magY'],2) + math.pow(data['magZ'],2)))
        qAcc = Quaternion(eAngs[0], eAngs[1], 0.0)
        qMag = Quaternion(data['magX'], data['magY'], data['magZ'], 0.0)
        magXYPlane = qAcc.times(qMag).times(qAcc.conjugate())
        x = magXYPlane.x
        y = magXYPlane.y
        data['magYawX'] = math.degrees(-math.atan2(y, x))

        data['imuTemp'] = struct.unpack('h', payload[106:108])[0]

        i2 = struct.unpack('h', payload[108:110])[0]
        i3 = struct.unpack('h', payload[110:112])[0]
        i4 = struct.unpack('h', payload[112:114])[0]
        i5 = struct.unpack('h', payload[114:116])[0]
        
        data['satnum'] = payload[116]                               # parse the number of satalites

        # only output legitimate location data
        if data['latitude'] == 0 or data['longitude'] == 0 or abs(data['latitude']) <= 0.0175 or abs(data['longitude']) <= 0.0175 or data['satnum'] <= 2 or data['satnum'] >= 32:
            data['longitude'] = ''
            data['latitude'] = ''
        return data




