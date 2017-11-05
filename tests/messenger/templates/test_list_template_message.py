from messenger.elements import Element
from messenger.buttons import URLButton
from messenger.templates import ListTemplate


class TestListTemplateMessage(object):
    def test_message(self):
        ElementList = [
            Element('Title'),
            Element('Title', 'Subtitle'),
            Element('Title', 'Subtitle', 'http://example.com'),
            Element(
                'Title',
                'Subtitle',
                'http://example.com',
                'Default Action'
            ),
            Element(
                'Title',
                'Subtitle',
                'http://example.com',
                'Default Action',
                [URLButton('Title', 'http://example.com')]
            )
        ]

        assert ListTemplate(ElementList).message() == {
            'attachment': {
                'payload': {
                    'elements': [{
                        'title': 'Title'
                    }, {
                        'subtitle': 'Subtitle',
                        'title': 'Title'
                    }, {
                        'image_url': 'http://example.com',
                        'subtitle': 'Subtitle',
                        'title': 'Title'
                    }, {
                        'default_action': 'Default Action',
                        'image_url': 'http://example.com',
                        'subtitle': 'Subtitle',
                        'title': 'Title'
                    }, {
                        'buttons': [{
                            'title': 'Title',
                            'type': 'web_url',
                            'url': 'http://example.com'
                        }],
                        'default_action': 'Default Action',
                        'image_url': 'http://example.com',
                        'subtitle': 'Subtitle',
                        'title': 'Title'
                    }],
                    'template_type': 'list'
                },
                'type': 'template'
            }
        }
