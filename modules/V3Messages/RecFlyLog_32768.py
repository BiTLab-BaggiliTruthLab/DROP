

class RecFlyLog_32768:
    fields = ['text']
    message_type = 32768
    label = 'RecFlyLog'
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