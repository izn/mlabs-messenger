from messenger.content_types import TextMessage


class TestTextMessage(object):
    def test_message(self):
        assert TextMessage('Message').message() == {'text': 'Message'}
