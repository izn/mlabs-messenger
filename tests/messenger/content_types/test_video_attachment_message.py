from messenger.content_types import VideoAttachment


class TestVideoAttachmentMessage(object):
    def test_message(self):
        TestURL = "http://example.com/video.mp4"

        assert VideoAttachment(TestURL).message() == {
            'attachment': {'type': 'video', 'payload': {'url': TestURL, 'is_reusable': False}}
        }

        assert VideoAttachment(TestURL, True).message() == {
            'attachment': {'type': 'video', 'payload': {'url': TestURL, 'is_reusable': True}}
        }
