import struct


class Controller_1000:
    fields = ['ctrl_tick', 'ctrl_pitch', 'ctrl_roll', 'ctrl_yaw', 'ctrl_thr', 'ctrl_mode', 'mode_switch', 'motor_state', 'sig_level', 'ctrl_level', 'sim_model', 'max_height', 'max_radius', 'D2H_x', 'D2H_y', 'act_req_id', 'act_act_id', 'cmd_mod', 'mod_req_id', 'fw_flag', 'mot_sta', 'OH_take', 'rc_cnt', 'sup_rc']
    message_type = 1000
    label = 'Controller'
    _length = 39  # there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'ctrl_tick': struct.unpack('I', payload[0:4])[0],
                'ctrl_pitch': struct.unpack('h', payload[4:6])[0],
                'ctrl_roll': struct.unpack('h', payload[6:8])[0],
                'ctrl_yaw': struct.unpack('h', payload[8:10])[0],
                'ctrl_thr': struct.unpack('h', payload[10:12])[0],
                'ctrl_mode': struct.unpack('B', payload[12:13])[0],
                'mode_switch': struct.unpack('B', payload[13:14])[0],
                'motor_state': struct.unpack('B', payload[14:15])[0],
                'sig_level': struct.unpack('B', payload[15:16])[0],
                'ctrl_level': struct.unpack('B', payload[16:17])[0],
                'sim_model': struct.unpack('B', payload[17:18])[0],
                'max_height': struct.unpack('H', payload[18:20])[0],
                'max_radius': struct.unpack('H', payload[20:22])[0],
                'D2H_x': struct.unpack('f', payload[22:26])[0],
                'D2H_y': struct.unpack('f', payload[26:30])[0],
                'act_req_id': struct.unpack('B', payload[30:31])[0],
                'act_act_id': struct.unpack('B', payload[31:32])[0],
                'cmd_mod': struct.unpack('B', payload[32:33])[0],
                'mod_req_id': struct.unpack('B', payload[33:34])[0],
                'fw_flag': struct.unpack('B', payload[34:35])[0],
                'mot_sta': struct.unpack('B', payload[35:36])[0],
                'OH_take': struct.unpack('B', payload[36:37])[0],
                'rc_cnt': struct.unpack('B', payload[37:38])[0],
                'sup_rc': struct.unpack('B', payload[38:39])[0]
                }

        return data