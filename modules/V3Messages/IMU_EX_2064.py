import struct


class IMU_EX_2064:
    fields = ['vo_vx_00','vo_vy_00','vo_vz_00','vo_px_00','vo_py_00','vo_pz_00','us_v_00','us_p_00','vo_flag_navi_00','imu_err_flag_00','vo_flag_rsv_00','imu_ex_cnt_00']
    message_type = 2064
    label = 'IMU_EX'
    _length = 40    #todo evtl 64 laut toller Notes-Liste?
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'vo_vx_00': struct.unpack('f', payload[0:4])[0],
            'vo_vy_00': struct.unpack('f', payload[4:8])[0],
            'vo_vz_00': struct.unpack('f', payload[8:12])[0],
            'vo_px_00': struct.unpack('f', payload[12:16])[0],
            'vo_py_00': struct.unpack('f', payload[16:20])[0],
            'vo_pz_00': struct.unpack('f', payload[20:24])[0],
            'us_v_00': struct.unpack('f', payload[24:28])[0],
            'us_p_00': struct.unpack('f', payload[28:32])[0],
            'vo_flag_navi_00': struct.unpack('H', payload[32:34])[0],
            'imu_err_flag_00': struct.unpack('H', payload[34:36])[0],
            'vo_flag_rsv_00': struct.unpack('H', payload[36:38])[0],
            'imu_ex_cnt_00': struct.unpack('H', payload[38:40])[0]
        }

        return data