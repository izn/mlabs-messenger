from messenger.content_types import ImageAttachment


class TestImageAttachmentMessage(object):
    def test_message(self):
        TestURL = "http://example.com/image.jpg"

        assert ImageAttachment(TestURL).message() == {
            'attachment': {'type': 'image', 'payload': {'url': TestURL, 'is_reusable': False}}
        }

        assert ImageAttachment(TestURL, True).message() == {
            'attachment': {'type': 'image', 'payload': {'url': TestURL, 'is_reusable': True}}
        }
