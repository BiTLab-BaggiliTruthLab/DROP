import struct


class RecSVOAVOID_1121:
    fields = ['osd_avoid_obstacle_enable','osd_user_avoid_enable','osd_avoid_obstacle_work_flag','osd_emergency_brake_work_flag',
              'go_home_avoid_enable','avoid_ground_force_landing_flag','radius_limit_work_flag','airport_limit_work_flag',
              'avoid_obstacle_work_flag','horiz_near_boundary_flag','is_avoid_overshoot_act_flag','vert_low_limit_work_flag',
              'vert_airport_limit_work_flag','roof_limit_flag','hit_ground_limit_work_flag']
    message_type = 1121
    label = 'RecSVOAVOID'
    _length = 15    # there's more
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'osd_avoid_obstacle_enable': struct.unpack('B', payload[0:1])[0],
            'osd_user_avoid_enable': struct.unpack('B', payload[1:2])[0],
            'osd_avoid_obstacle_work_flag': struct.unpack('B', payload[2:3])[0],
            'osd_emergency_brake_work_flag': struct.unpack('B', payload[3:4])[0],
            'go_home_avoid_enable': struct.unpack('B', payload[4:5])[0],
            'avoid_ground_force_landing_flag': struct.unpack('B', payload[5:6])[0],
            'radius_limit_work_flag': struct.unpack('B', payload[6:7])[0],
            'airport_limit_work_flag': struct.unpack('B', payload[7:8])[0],
            'avoid_obstacle_work_flag': struct.unpack('B', payload[8:9])[0],
            'horiz_near_boundary_flag': struct.unpack('B', payload[9:10])[0],
            'is_avoid_overshoot_act_flag': struct.unpack('B', payload[10:11])[0],
            'vert_low_limit_work_flag': struct.unpack('B', payload[11:12])[0],
            'vert_airport_limit_work_flag': struct.unpack('B', payload[12:13])[0],
            'roof_limit_flag': struct.unpack('B', payload[13:14])[0],
            'hit_ground_limit_work_flag': struct.unpack('B', payload[14:15])[0],
        }

        return data