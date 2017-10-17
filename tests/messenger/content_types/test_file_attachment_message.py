from messenger.content_types import FileAttachment


class TestFileAttachmentMessage(object):
    def test_message(self):
        TestURL = "http://example.com/file.pdf"

        assert FileAttachment(TestURL).message() == {
            'attachment': {'type': 'file', 'payload': {'url': TestURL, 'is_reusable': False}}
        }

        assert FileAttachment(TestURL, True).message() == {
            'attachment': {'type': 'file', 'payload': {'url': TestURL, 'is_reusable': True}}
        }
