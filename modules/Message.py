# Devon Clark
# Message Class
import struct
import datetime
from modules.Packet import Packet
from modules.GPSPayload import GPSPayload
from modules.MotorPayload import MotorPayload
from modules.HPPayload import HPPayload
from modules.RCPayload import RCPayload
from modules.TabletLocPayload import TabletLocPayload
from modules.BatteryPayload import BatteryPayload
from modules.GimbalPayload import GimbalPayload
from modules.FlightStatPayload import FlightStatPayload
from modules.AdvBatteryPayload import AdvBatteryPayload
import simplekml

class Message:
    # *** add the other field names later
    #fieldnames = ['messageid'] + GPSPayload.fields + MotorPayload.fields + HPPayload.fields + RCPayload.fields + TabletLocPayload.fields + BatteryPayload.fields + GimbalPayload.fields + FlightStatPayload.fields + AdvBatteryPayload.fields
    fieldnames = [ 'messageid', 'offsetTime', 'logDateTime', 'time(millisecond)',
    'latitude', 'longitude', 'satnum', 'gpsHealth', 'altitude', 'baroAlt', 
    #'vpsHeight',       # not implemented
    'height', 'accelX', 'accelY', 'accelZ', 'accel', 'gyroX', 'gyroY', 'gyroZ', 'gyro', 'errorX', 'errorY', 'errorZ', 'error', 'magX', 'magY', 'magZ', 'magMod', 
    'velN', 'velE', 'velD', 'vel', 'velH', 
    #'velGPS-velH',     # not implemented
    'quatW', 'quatX', 'quatY', 'quatZ', 'roll', 'pitch', 'yaw', 'yaw360', 
    #'totalGyroZ',      # not implemented
    'magYawX', 'thrustAngle', 'latitudeHP', 'longitudeHP', 
    #'altitudeHP', 'geoMagDeclination', 'geoMagInclination', 'distanceHP', 'distanceTravelled', 'directionOfTravel', 'directionOfTravelTrue',   # not implemented
    'imuTemp', 'flyc_state', 'flycStateStr', 'nonGPSError', 'nonGPSErrStr', 
    'DWflyCState', 'connectedToRC', 'current', 'volt1', 'volt2', 'volt3', 'volt4', 'volt5', 'volt6', 'totalVolts', 'voltSpread', 'Watts', 'batteryTemp(C)', 'ratedCapacity', 
    'remainingCapacity', 'percentageCapacity', 'batteryUsefulTime', 'voltagePercent', 'batteryCycleCount', 'batteryLifePercentage', 'batteryBarCode', 'minCurrent', 'maxCurrent', 
    'avgCurrent', 'minVolts', 'maxVolts', 'avgVolts', 'minWatts', 'maxWatts', 'avgWatts', 'Gimbal:roll', 'Gimbal:pitch', 'Gimbal:yaw', 'Gimbal:Xroll', 'Gimbal:Xpitch', 'Gimbal:Xyaw', 
    'rFront', 'lFront', 'lBack', 'rBack', 
    # **** DJI Phantom Standard does not log the motor speed/load. Other versions do (Advanced/Inspire).
    'rFrontSpeed', 'lFrontSpeed', 'lBackSpeed', 'rBackSpeed', 'rFrontLoad', 'lFrontLoad', 'lBackLoad', 'rBackLoad', 
    'aileron', 'elevator', 'throttle', 'rudder', 'modeSwitch', 'latitudeTablet', 'longitudeTablet', 'droneModel'
    ]
    fieldnames_v3 = ['messageid', 'offsetTime', 'logDateTime', 'time(millisecond)',
                     # 32768
                     'text',
                     # 2096
                     'latitude', 'longitude', 'altitude', 'velN', 'velE', 'velD', 'date', 'time', 'hdop', 'pdop', 'hacc', 'sacc', 'numGPS', 'numGLN', 'numSV',
                     # 1712
                     'goHome', 'land', 'goHomeTime', 'landTime',
                     # 2048
                     'longRad', 'latRad', 'longitudeDegrees', 'latitudeDegrees', 'baroPress', 'accelX', 'accelY',
                     'accelZ', 'gyroX', 'gyroY', 'gyroZ', 'baroAlti', 'quatW', 'quatX', 'quatY', 'quatZ', 'ag_X',
                     'ag_Y', 'ag_Z', 'velN', 'velE', 'velD', 'gb_X', 'gb_Y', 'gb_Z', 'magX', 'magY', 'magZ', 'imuTemp',
                     'ty', 'tz', 'sensor_stat', 'filter_stat', 'numSats', 'atti_cnt',
                     # 2064
                     'vo_vx_00', 'vo_vy_00', 'vo_vz_00', 'vo_px_00', 'vo_py_00', 'vo_pz_00', 'us_v_00', 'us_p_00',
                     'vo_flag_navi_00', 'imu_err_flag_00', 'vo_flag_rsv_00', 'imu_ex_cnt_00',
                     # 1001
                     'int_fsm', 'fsm_state', 'last_fsm', 'near_gnd', 'UP_state', 'land_state', 'safe_fltr',
                     # 20350, 20351, 2256, 2257
                     'magX', 'magY', 'magZ',
                     # 1700
                     'cur_cmd', 'fail_safe', 'vedio_lost', 'data_lost', 'app_lost', 'frame_lost', 'rec_cnt', 'sky_con',
                     'gnd_con', 'connected', 'm_changed', 'arm_status', 'wifi_en', 'in_wifi',
                     # 1710
                     'ad_v', 'r_time', 'ave_I', 'vol_t', 'pack_ve', 'I', 'r_cap', 'cap_per', 'temp', 'right', 'l_cell',
                     'dyna_cnt', 'f_cap', 'out_ctl', 'out_ctl_f',
                     # 1000
                     'ctrl_tick', 'ctrl_pitch', 'ctrl_roll', 'ctrl_yaw', 'ctrl_thr', 'ctrl_mode', 'mode_switch',
                     'motor_state', 'sig_level', 'ctrl_level', 'sim_model', 'max_height', 'max_radius', 'D2H_x',
                     'D2H_y', 'act_req_id', 'act_act_id', 'cmd_mod', 'mod_req_id', 'fw_flag', 'mot_sta', 'OH_take',
                     'rc_cnt', 'sup_rc',
                     # 1711
                     'not_ready', 'comm_err', 'first_auth', 'auth_fail', 'need_re', 'volVerylow','volNotsafe', 'volLevel1',
                     'vollevel2', 'capLevel1', 'capLevel2', 'smartCap1',
                     'smartCap2', 'd_flg', 'ccsc', 'all',
                     # 1307
                     'pwm1','pwm2','pwm3','pwm4','pwm5','pwm6','pwm7','pwm8',
                     # 1306
                     'raw_tilt_x','raw_tilt_y','raw_tors','raw_lift','fix_tilt_x','fix_tilt_y','fix_tor','fix_lift','bound_max','bound_min','tors_limit_scale','tilt_scale',
                     # 16
                     'usonic_h', 'usonic_flag', 'usonic_cnt',
                     # 12
                     'longtitude', 'latitude', 'relative_height', 'vgx', 'vgy', 'vgz', 'pitch', 'roll', 'yaw', 'mode1',
                     'latest_cmd', 'controller_state', 'gps_nums', 'gohome_landing_reason', 'start_fail_reason',
                     'controller_state_ext', 'ctrl_tick', 'ultrasonic_height', 'motor_startup_time',
                     'motor_startup_times', 'bat_alarm1', 'bat_alarm2', 'version_match', 'product_type',
                     'imu_init_fail_reason', 'stop_motor_reason', 'motor_start_error_code', 'sdk_ctrl_dev', 'yaw_rate',
                     #

                     ]
    tickNo = None
    tickOffset = 0
    row_out = {}
    packetNum = 0
    packets = []
    addedData = False
    unknownPackets = []#TODO use this
    addedUnknownData = False
    meta = None
    startUNIXTime = None
    gps_fr_dict = {}
    kmlFile = None
    kmlWriter = None
    kml_res = 1   # kml resolution: kml_res = X, where 1:X represents the ratio of original points to output points for the kml. Used to scale down prevent large datasets from not opening in google earth
    point_cnt = kml_res # for counting the points before writing to kml
    is_v3 = False
    
    def __init__(self, meta, kmlFile=None, kmlScale=1, is_v3=False):
        #self.fieldnames = ['messageid'] + GPSPayload.fields + MotorPayload.fields + HPPayload.fields + RCPayload.fields + TabletLocPayload.fields + BatteryPayload.fields + GimbalPayload.fields + FlightStatPayload.fields + AdvBatteryPayload.fields
        self.tickNo = None
        self.row_out = {}
        self.packetNum = 0
        self.packets = []
        self.addedData = False
        self.meta = meta
        self.gps_fr_dict = {}
        self.is_v3 = is_v3
        
        self.kmlFile = kmlFile
        self.kmlWriter = None
        if self.kmlFile != None:
            self.kmlWriter = simplekml.Kml()
            self.kml_res = kmlScale
        # *********************************************
        # **** WARNING: THIS IS NOT THE PREFERED METHOD TO OBTAIN THE START TIME
        # ctime is the time the meta data (permissions) were last changed
        # THIS IS NOT THE CREATION TIME
        # We are assuming here that the last time the permissions were
        # touched was when the file was created. This may not be true.
        # If you do not wish to use this, just comment it out. It won't break anything ;)
        # *********************************************
        self.startUNIXTime = int(meta.st_ctime)
        # *********************************************
        # *********************************************

    def setTickNo(self, tickNo):
        self.tickNo = tickNo

    def addPacket(self, pktlen, header, payload):
        # everything we need to do with the packet obj should be done here because we dont retain them
        packet = Packet(pktlen, header, payload, self.is_v3)
        tickNoRead = struct.unpack('I', packet.header[3:7])[0]
        if packet.payload != None and tickNoRead >= 0:
            self.addedData = True
            self.setTickNo(tickNoRead)
            self.row_out = dict(self.row_out, **packet.getItems())
            self.packetNum += 1
            if packet.pkttype == GPSPayload._type and packet.pktsubtype == GPSPayload._subtype:      # GPS Packet
                if self.row_out.get('latitude') and self.row_out.get('longitude') and self.row_out.get('time(millisecond)'):
                    if self.row_out['latitude'] != '' and self.row_out['longitude'] != '' and self.row_out['time(millisecond)'] != '':
                        self.gps_fr_dict[self.row_out['time(millisecond)']] = [self.row_out['latitude'], self.row_out['longitude'], self.row_out.get('baroAlt', ''), self.row_out.get('satnum', ''), self.row_out.get('totalVolts', ''), self.row_out.get('flyc_state', '')]
            return True
        # package unknown -> log for analysis
        if self.is_v3:
            self.addedUnknownData = True
            self.unknownPackets.append({"pktType": struct.unpack("<H", header[1:3])[0], "tick": tickNoRead,
                                        "pktLen": pktlen, "header": header, "payload": payload})
        return False

    def getRow(self):
        if self.tickNo != None:
            offsetTime = float(self.tickNo - self.tickOffset)/600.0
        else:
            offsetTime = ''
        #logDateTime = datetime.datetime.fromtimestamp(self.startUNIXTime + int(offsetTime)).strftime('%Y-%m-%d %H:%M:%S')
        logDateTime = ''
        return dict(self.row_out, **{'messageid':self.tickNo, 'offsetTime':offsetTime, 'logDateTime':logDateTime})

    def writeKml(self, row):
        if self.kmlWriter != None:
            if row.get('latitude', False) and row.get('longitude', False):
                if self.point_cnt % self.kml_res == 0:
                    self.kmlWriter.newpoint(name=str(row.get('messageid')), coords=[(row.get('longitude'), row.get('latitude'))])    
                self.point_cnt += 1

    def writeRow(self, writer, newTickNo):
        if newTickNo != self.tickNo:
            if self.addedData:
                writer.writerow(self.getRow())   # write the current message before starting a new one (only if we have new data)
                self.addedData = False           # reset addedData because just wrote all the most recent info to the csv
            self.writeKml(self.getRow())  # write to KML file.
            self.tickNo = newTickNo

    def outToFile(self, fname):
        if self.gps_fr_dict != {}:
            with open(fname + '-output.txt', 'w') as of:
                for d in self.gps_fr_dict:
                    of.write(str(d) + ': ' + str(self.gps_fr_dict[d]) + '\n')

    def finalizeKml(self):
        if self.kmlWriter != None and self.kmlFile != None:
            self.kmlWriter.save(self.kmlFile)