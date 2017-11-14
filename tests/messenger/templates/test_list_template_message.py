from messenger.elements import Element
from messenger.templates import ListTemplate


class TestListTemplateMessage(object):
    def test_message(self):
        element_list = [
            Element('Title'),
            Element('Title', 'Subtitle'),
            Element('Title', 'Subtitle', 'http://example.com')
        ]

        assert ListTemplate(element_list).message() == {
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
                    }],
                    'template_type': 'list'
                },
                'type': 'template'
            }
        }
