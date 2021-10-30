import struct

class RecFlyLog_32768:
    fields = ['text']
    message_type = 32768
    label = 'RecFlyLog'
    _length = -1
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'text': payload}
        return data