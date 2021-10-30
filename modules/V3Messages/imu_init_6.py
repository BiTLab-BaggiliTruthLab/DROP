import struct

class imu_init_6:
    fields = ['imu_offset_x','imu_offset_y','imu_offset_z','gps_offset_x','gps_offset_y','gps_offset_z','imu_dir',
              'imu_key','o_sw','mag_bias_x','mag_bias_y','mag_bias_z','mag_scale_x','mag_scale_y','mag_scale_z','init_counter']
    message_type = 6
    label = 'imu_init'
    _length = 54
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'imu_offset_x': struct.unpack('f', payload[0:4])[0],
            'imu_offset_y': struct.unpack('f', payload[4:8])[0],
            'imu_offset_z': struct.unpack('f', payload[8:12])[0],
            'gps_offset_x': struct.unpack('f', payload[12:16])[0],
            'gps_offset_y': struct.unpack('f', payload[16:20])[0],
            'gps_offset_z': struct.unpack('f', payload[20:24])[0],
            'imu_dir': struct.unpack('H', payload[24:26])[0],
            'imu_key': struct.unpack('B', payload[26:27])[0],
            'o_sw': struct.unpack('B', payload[27:28])[0],
            'mag_bias_x': struct.unpack('f', payload[28:32])[0],
            'mag_bias_y': struct.unpack('f', payload[32:36])[0],
            'mag_bias_z': struct.unpack('f', payload[36:40])[0],
            'mag_scale_x': struct.unpack('f', payload[40:44])[0],
            'mag_scale_y': struct.unpack('f', payload[44:48])[0],
            'mag_scale_z': struct.unpack('f', payload[48:52])[0],
            'init_counter': struct.unpack('H', payload[52:54])[0],
        }

        return data