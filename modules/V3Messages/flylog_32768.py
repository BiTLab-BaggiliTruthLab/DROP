class flylog_32768:
    fields = ['text']
    message_type = 32768
    label = ''
    _length = -1
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'text': payload}
        return data