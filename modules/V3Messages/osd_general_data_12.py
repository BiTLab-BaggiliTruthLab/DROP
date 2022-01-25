import struct


class osd_general_data_12:
    fields = ['longtitude','latitude','relative_height','vgx','vgy','vgz','pitch','roll','yaw','mode1','latest_cmd','controller_state','gps_nums','gohome_landing_reason','start_fail_reason','controller_state_ext','ctrl_tick','ultrasonic_height','motor_startup_time','motor_startup_times','bat_alarm1','bat_alarm2','version_match','product_type','imu_init_fail_reason','stop_motor_reason','motor_start_error_code','sdk_ctrl_dev','yaw_rate']
    message_type = 12
    label = 'osd_general_data'
    _length = 55    #there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'longtitude': struct.unpack('d', payload[0:8])[0],
            'latitude': struct.unpack('d', payload[8:16])[0],
            'relative_height': struct.unpack('h', payload[16:18])[0],
            'vgx': struct.unpack('h', payload[18:20])[0],
            'vgy': struct.unpack('h', payload[20:22])[0],
            'vgz': struct.unpack('h', payload[22:24])[0],
            'pitch': struct.unpack('h', payload[24:26])[0],
            'roll': struct.unpack('h', payload[26:28])[0],
            'yaw': struct.unpack('h', payload[28:30])[0],
            'mode1': struct.unpack('B', payload[30:31])[0],
            'latest_cmd': struct.unpack('B', payload[31:32])[0],
            'controller_state': struct.unpack('I', payload[32:36])[0],
            'gps_nums': struct.unpack('B', payload[36:37])[0],
            'gohome_landing_reason': struct.unpack('B', payload[37:38])[0],
            'start_fail_reason': struct.unpack('B', payload[38:39])[0],
            'controller_state_ext': struct.unpack('B', payload[39:40])[0],
            'ctrl_tick': struct.unpack('B', payload[40:41])[0],
            'ultrasonic_height': struct.unpack('B', payload[41:42])[0],
            'motor_startup_time': struct.unpack('H', payload[42:44])[0],
            'motor_startup_times': struct.unpack('B', payload[44:45])[0],
            'bat_alarm1': struct.unpack('B', payload[45:46])[0],
            'bat_alarm2': struct.unpack('B', payload[46:47])[0],
            'version_match': struct.unpack('B', payload[47:48])[0],
            'product_type': struct.unpack('B', payload[48:49])[0],
            'imu_init_fail_reason': struct.unpack('B', payload[49:50])[0],
            'stop_motor_reason': struct.unpack('B', payload[50:51])[0],
            'motor_start_error_code': struct.unpack('B', payload[51:52])[0],
            'sdk_ctrl_dev': struct.unpack('B', payload[52:53])[0],
            'yaw_rate': struct.unpack('h', payload[53:55])[0]
        }
        return data