from messenger.content_types import QuickReply


class TestQuickReply(object):
    def test_quick_reply(self):
        text = 'Message'
        quick_reply_one = {
            'content_type': 'text',
            'payload': 'random_payload1',
            'title': 'title1',
            'image_url': None
        }
        quick_reply_two = {
            'content_type': 'location'
        }

        assert QuickReply(text, [quick_reply_one, quick_reply_two]).message() == {
            'text': 'Message',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'payload': 'random_payload1',
                    'title': 'title1',
                    'image_url': None

                },
                {
                    'content_type': 'location'
                }
            ]}
