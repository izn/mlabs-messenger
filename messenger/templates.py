from .buttons import ButtonGenerator
from .elements import ElementGenerator


class Template(object):
    def __init__(self, type):
        self.type = type

    def message(self):
        message = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': self.type
                }
            }
        }

        message['attachment']['payload'].update(self.payload)

        return message


class ButtonTemplate(Template):
    def __init__(self, text, buttons):
        self.payload = {
            'text': text,
            'buttons': ButtonGenerator(buttons)
        }

        super().__init__('button')


class GenericTemplate(Template):
    def __init__(self, elements, shareable, image_aspect_ratio):
        self.payload = {
            'elements': ElementGenerator(elements)
        }

        if (shareable):
            self.payload['sharable'] = shareable

        if (image_aspect_ratio):
            self.payload['image_aspect_ratio'] = image_aspect_ratio

        super().__init__('generic')


class ListTemplate(Template):
    def __init__(self, elements, buttons=None, top_element_style=None):
        self.payload = {
            'elements': ElementGenerator(elements)
        }

        if (buttons):
            self.payload['buttons'] = [ButtonGenerator(buttons)]

        if (top_element_style):
            self.payload['top_element_style'] = top_element_style

        super().__init__('list')
