from messenger.content_types import AudioAttachment


class TestAudioAttachmentMessage(object):
    def test_message(self):
        TestURL = "http://example.com/audio.mp3"

        assert AudioAttachment(TestURL).message() == {
            'attachment': {'type': 'audio', 'payload': {'url': TestURL, 'is_reusable': False}}
        }

        assert AudioAttachment(TestURL, True).message() == {
            'attachment': {'type': 'audio', 'payload': {'url': TestURL, 'is_reusable': True}}
        }
