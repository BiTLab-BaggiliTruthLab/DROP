import struct

class RecDefs_65533:
    fields = ['text']
    message_type = 65533
    label = 'RecDefs'
    _length = -1
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        if type(payload) == bytes:
            self.data = self.parse(payload.decode(encoding='UTF-8', errors='backslashreplace'))
            return
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'text': payload}
        return data