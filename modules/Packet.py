# Devon Clark
# Packet Class
import struct
from modules.GPSPayload import GPSPayload
from modules.MotorPayload import MotorPayload
from modules.HPPayload import HPPayload
from modules.RCPayload import RCPayload
from modules.TabletLocPayload import TabletLocPayload
from modules.BatteryPayload import BatteryPayload
from modules.GimbalPayload import GimbalPayload
from modules.FlightStatPayload import FlightStatPayload
from modules.AdvBatteryPayload import AdvBatteryPayload

class Packet:
    pktlen = 0
    header = 0
    pkttype = None
    pktsubtype = None
    label = None
    msg = None
    tickNo = 0
    payload = None

    def __init__(self, pktlen, header, payload):
        self.pktlen = pktlen
        self.header = header
        self.pkttype = 0xFF & self.header[0]
        self.pktsubtype = 0xFF & self.header[1]
        self.msg = header[2]
        if (0xFF & self.msg) == 128:
            self.pkttype = 255
            self.pktsubtype = 1
        if (0xFF & self.msg) == 255:
            self.pkttype = 255
            self.pktsubtype = 2
        self.tickNo = struct.unpack('I', self.header[3:7])[0]

        self.payload = self.processPayload(payload)

    def processPayload(self, payload):
        if self.pkttype == GPSPayload._type and self.pktsubtype == GPSPayload._subtype:      # GPS Packet
            self.label = 'GPS'
            #print(str(self.tickNo) + ' - GPS pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = GPSPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == MotorPayload._type and self.pktsubtype == MotorPayload._subtype:    # Motor Packet
            self.label = 'MOTOR'
            #print(str(self.tickNo) + ' - Motor pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = MotorPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == HPPayload._type and self.pktsubtype == HPPayload._subtype:    # Home Point Packet
            self.label = 'HP'
            #print(str(self.tickNo) + ' - HP pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = HPPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == RCPayload._type and self.pktsubtype == RCPayload._subtype:    # Remote Control Packet
            self.label = 'RC'
            #print(str(self.tickNo) + ' - RC pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = RCPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == TabletLocPayload._type and self.pktsubtype == TabletLocPayload._subtype:    # Tablet Location Packet
            self.label = 'TABLET'
            #print(str(self.tickNo) + ' - TABLET pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = TabletLocPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == BatteryPayload._type and self.pktsubtype == BatteryPayload._subtype:    # Battery Packet
            self.label = 'BATTERY'
            #print(str(self.tickNo) + ' - BATTERY pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = BatteryPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == GimbalPayload._type and self.pktsubtype == GimbalPayload._subtype:    # Gimbal Packet
            self.label = 'GIMBAL'
            #print(str(self.tickNo) + ' - GIMBAL pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = GimbalPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == FlightStatPayload._type and self.pktsubtype == FlightStatPayload._subtype:    # Flight Status Packet
            self.label = 'FLIGHT STAT'
            #print(str(self.tickNo) + ' - FLIGHT STAT pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = FlightStatPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        elif self.pkttype == AdvBatteryPayload._type and self.pktsubtype == AdvBatteryPayload._subtype:    # Advanced Battery Packet
            self.label = 'ADV BATTERY'
            #print(str(self.tickNo) + ' - ADV BATTERY pkt len: ' + str(self.pktlen))
            payload = self.decode(payload)
            pld_obj = AdvBatteryPayload(payload)
            if len(pld_obj.data) > 0:
                return pld_obj
        return None

    def getItems(self):
        try:
            return self.payload.data
        except:
            return {}

    ''' 
    original code snippet from DatCon project - Payload.java
    byte xorKey = (byte)(int)(this.tickNo % 256L);
    for (int i = 0; i < this.length; i++) {
        if (this.start + i >= this.datFile.getLength()) {
        throw new FileEnd();
        }
        this.datFile.setPosition(this.start + i);
        this.xorArray[i] = ((byte)(this.datFile.getByte() ^ xorKey));
    }
    '''

    def decode(self, payload):
        xorKey = int(self.tickNo % 256)
        decodedPld = []
        for byte in payload:
            decodedPld.append(byte ^ xorKey)    # byte and xorKey must be ints
        return bytes(decodedPld)













