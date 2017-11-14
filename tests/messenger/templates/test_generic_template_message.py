from messenger.elements import Element
from messenger.templates import GenericTemplate


class TestGenericTemplateMessage(object):
    def test_message(self):
        element_list = [
            Element('Title'),
            Element('Title', 'Subtitle'),
            Element('Title', 'Subtitle', 'http://example.com')
        ]

        assert GenericTemplate(
            element_list,
            shareable=False,
            image_aspect_ratio='square'
        ).message() == {
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
                    'image_aspect_ratio': 'square',
                    'template_type': 'generic'
                },
                'type': 'template'
            }
        }
