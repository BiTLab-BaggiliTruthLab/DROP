from __future__ import division
# Devon Clark
# Flight Status Class
import struct
import math

class FlightStatPayload:
    fields = ['FSlongitude', 'FSlatitude', 'height', 'FSpitch', 'FSroll', 'FSyaw', 'flyc_state', 'flycStateStr', 'connectedToRC', 'failure', 'nonGPSError', 'nonGPSErrStr', 
    'time(millisecond)', 'DWflyCState']
    NGPEErrs = {1:"FORBIN", 2:"GPSNUM_NONENOUGH", 3:"GPS_HDOP_LARGE", 4:"GPS_POSITION_NON_MATCH", 5:"SPEED_ERROR_LARGE", 6:"YAW_ERROR_LARGE", 7:"COMPASS_ERROR_LARGE"}
    FLCSStates = {0:"MANUAL", 1:"ATTI", 2:"ATTI_CL", 3:"ATTI_HOVER", 4:"HOVER", 5:"GSP_BLAKE", 6:"GPS_ATTI", 7:"GPS_CL", 8:"GPS_HOME_LOCK", 9:"GPS_HOT_POINT", 
    10:"ASSISTED_TAKEOFF", 11:"AUTO_TAKEOFF", 12:"AUTO_LANDING", 13:"ATTI_LANDING", 14:"NAVI_GO", 15:"GO_HOME", 16:"CLICK_GO", 17:"JOYSTICK", 23:"ATTI_LIMITED", 
    24:"GPS_ATTI_LIMITED", 25:"FOLLOW_ME", 100:"OTHER"}
    flyc_to_dw = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:20, 10:30, 11:40, 12:50, 13:60, 14:70, 15:80, 16:90, 17:200, 23:300, 24:400}
    _type = 0x2A
    _subtype = 0x0C
    _length = 0x3E
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def convertpos(self, pos):
        # convert position from radians to degrees
        return math.degrees(pos)

    def parse(self, payload):
        data = {}

        FSlongitude = self.convertpos(struct.unpack('d', payload[0:8])[0])
        FSlatitude = self.convertpos(struct.unpack('d', payload[8:16])[0])
        data['height'] = struct.unpack('h', payload[16:18])[0] / 10

        FSpitch = struct.unpack('h', payload[24:26])[0] / 10
        FSroll = struct.unpack('h', payload[26:28])[0] / 10
        FSyaw = struct.unpack('h', payload[28:30])[0] / 10

        data['flyc_state'] = 0x7f & payload[30]
        if not self.FLCSStates.get(data['flyc_state'], False):
            data['flyc_state'] = ''
        data['flycStateStr'] = self.FLCSStates.get(data['flyc_state'], "UNKNOWN")
        data['connectedToRC'] = 0
        if 0x80 & payload[30] == 0:
            data['connectedToRC'] = 1
        failure = payload[38]
        data['nonGPSError'] = 0x7 & payload[39]
        data['nonGPSErrStr'] = self.NGPEErrs.get(data['nonGPSError'], "UNKNOWN")
        data['time(millisecond)'] = struct.unpack('h', payload[42:44])[0] * 100

        data['DWflyCState'] = self.flyc_to_dw[data['flyc_state']]
        return data


''' Example packet
55 - start byte
3E - length (62 bytes)
00 - padding
2A - type
0C - sub type
00 - msg
97 0A 00 00 - tick No. (2711)
97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 97 96 B7 97 97 97 97 97 97 97 97 97 97 97 89 1D 9F 93 97 E2 16 55 28 00 6C 5C 00 98 0A 00 00 8A 98 B7 98 98 98 73 67 95 98 2C 6F 98 98 98 98 98 98 98 98 98 98 98 98 AA 98 98 98 F8 5B
'''















