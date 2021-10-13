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
from modules.V3Messages.Controller_1000 import Controller_1000
from modules.V3Messages.flylog_32768 import flylog_32768
from modules.V3Messages.GPS_GLNS_5 import GPS_GLNS_5
from modules.V3Messages.GPS_2096 import GPS_2096
from modules.V3Messages.RecSmartBatt_1712 import RecSmartBatt_1712
from modules.V3Messages.IMU_ATTI_2048 import IMU_ATTI_2048
from modules.V3Messages.IMU_EX_2064 import IMU_EX_2064
from modules.V3Messages.aircraft_condition_1001 import aircraft_condition_1001
from modules.V3Messages.RecMagRaw_20350 import RecMagRaw_20350
from modules.V3Messages.RecMagRaw_20351 import RecMagRaw_20351
from modules.V3Messages.RecMag_2256 import RecMag_2256
from modules.V3Messages.RecMag_2257 import RecMag_2257
from modules.V3Messages.rc_debug_info_1700 import rc_debug_info_1700
from modules.V3Messages.battery_info_1710 import battery_info_1710
from modules.V3Messages.battery_status_1711 import battery_status_1711
from modules.V3Messages.MotorCtrl_1307 import MotorCtrl_1307
from modules.V3Messages.CtrlAllocation_1306 import CtrlAllocation_1306
from modules.V3Messages.usonic_16 import usonic_16
from modules.V3Messages.osd_general_data_12 import osd_general_data_12



availableMessageClasses = {
    GPS_GLNS_5.message_type: GPS_GLNS_5,
    flylog_32768.message_type: flylog_32768,
    GPS_2096.message_type: GPS_2096,
    RecSmartBatt_1712.message_type: RecSmartBatt_1712,
    IMU_ATTI_2048.message_type: IMU_ATTI_2048,
    IMU_EX_2064.message_type: IMU_EX_2064,
    aircraft_condition_1001.message_type: aircraft_condition_1001,
    RecMagRaw_20350.message_type: RecMagRaw_20350,
    RecMagRaw_20351.message_type: RecMagRaw_20351,
    RecMag_2256.message_type: RecMag_2256,
    RecMag_2257.message_type: RecMag_2257,
    rc_debug_info_1700.message_type: rc_debug_info_1700,
    battery_info_1710.message_type: battery_info_1710,
    Controller_1000.message_type: Controller_1000,
    battery_status_1711.message_type: battery_status_1711,
    MotorCtrl_1307.message_type: MotorCtrl_1307,
    # TODO unknown length... (we want 20, but only have code for 48) CtrlAllocation_1306.message_type: CtrlAllocation_1306,
    usonic_16.message_type: usonic_16,
    osd_general_data_12.message_type: osd_general_data_12,

}

class Packet:
    pktlen = 0
    header = 0
    pkttype = None
    pktsubtype = None
    label = None
    msg = None
    tickNo = 0
    payload = None
    is_v3 = False

    def __init__(self, pktlen, header, payload, is_v3):
        self.pktlen = pktlen
        self.header = header
        self.is_v3 = is_v3
        if is_v3:
            self.pkttype = struct.unpack("<H", header[1:3])[0]
        else:
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

        if self.is_v3:
            self.payload = self.processPayloadV3(payload)
        else:
            self.payload = self.processPayloadV2(payload)

    def processPayloadV2(self, payload):
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

    def processPayloadV3(self, payload):
        message_class = availableMessageClasses.get(self.pkttype)
        if message_class:
            payload = self.decode(payload)
            pld_obj = message_class(payload)
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













