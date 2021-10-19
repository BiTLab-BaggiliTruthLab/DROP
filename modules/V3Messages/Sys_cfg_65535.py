import struct


class Sys_cfg_65535:
    fields = ['text']
    message_type = 65535
    label = 'Sys_cfg'
    _length = -1
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'text': payload}
        return data
