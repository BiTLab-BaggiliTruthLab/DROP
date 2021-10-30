import struct

class adv_gh_debug_data_1014:
    fields = ['SL_req','SL_F','SL_last_F','home_type','home_cnt','start_set','in_AL','GH_req','GH_S','GH_T','GH_cnt','GH_ok','GH_cur_H','AL_need','AL_in','AL_req','AL_status','AL_need_T','AL_is_ok','AL__cnt','AL_gnd','AL_suc','AL_OK','chg_ht_F','adv_ctrl_F','adv_brake_F','adv_roll_x','adv_pitch_y','adv_thr_z','adv_yaw','adv_fdfd_x','adv_fdfd_y','ctrl_cnt','ctrl_OK']
    message_type = 1014
    label = 'adv_gh_debug_data'
    _length = 42
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'SL_req': struct.unpack('b', payload[0:1])[0],
            'SL_F': struct.unpack('b', payload[1:2])[0],
            'SL_last_F': struct.unpack('b', payload[2:3])[0],
            'home_type': struct.unpack('B', payload[3:4])[0],
            'home_cnt': struct.unpack('B', payload[4:5])[0],
            'start_set': struct.unpack('B', payload[5:6])[0],
            'in_AL': struct.unpack('B', payload[6:7])[0],
            'GH_req': struct.unpack('B', payload[7:8])[0],
            'GH_S': struct.unpack('B', payload[8:9])[0],
            'GH_T': struct.unpack('h', payload[9:11])[0],
            'GH_cnt': struct.unpack('B', payload[11:12])[0],
            'GH_ok': struct.unpack('B', payload[12:13])[0],
            'GH_cur_H': struct.unpack('B', payload[13:14])[0],
            'AL_need': struct.unpack('B', payload[14:15])[0],
            'AL_in': struct.unpack('B', payload[15:16])[0],
            'AL_req': struct.unpack('B', payload[16:17])[0],
            'AL_status': struct.unpack('B', payload[17:18])[0],
            'AL_need_T': struct.unpack('h', payload[18:20])[0],
            'AL_is_ok': struct.unpack('B', payload[20:21])[0],
            'AL__cnt': struct.unpack('B', payload[21:22])[0],
            'AL_gnd': struct.unpack('B', payload[22:23])[0],
            'AL_suc': struct.unpack('B', payload[23:24])[0],
            'AL_OK': struct.unpack('B', payload[24:25])[0],
            'chg_ht_F': struct.unpack('B', payload[25:26])[0],
            'adv_ctrl_F': struct.unpack('B', payload[26:27])[0],
            'adv_brake_F': struct.unpack('B', payload[27:28])[0],
            'adv_roll_x': struct.unpack('h', payload[28:30])[0],
            'adv_pitch_y': struct.unpack('h', payload[30:32])[0],
            'adv_thr_z': struct.unpack('h', payload[32:34])[0],
            'adv_yaw': struct.unpack('h', payload[34:36])[0],
            'adv_fdfd_x': struct.unpack('h', payload[36:38])[0],
            'adv_fdfd_y': struct.unpack('h', payload[38:40])[0],
            'ctrl_cnt': struct.unpack('B', payload[40:41])[0],
            'ctrl_OK': struct.unpack('B', payload[41:42])[0],
        }

        return data