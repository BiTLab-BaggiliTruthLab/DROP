import struct

class Record_SDlogs_65280:
    fields = ['text']
    message_type = 65280
    label = 'Recors_SDlogs'
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