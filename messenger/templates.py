from .buttons import *  # noqa ignore=F405
from .elements import *  # noqa ignore=F405
from .payment import *  # noqa ignore=F405

class Template(object):
    def __init__(self, type, payload):
        self.type = type
        self.payload = payload

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
    def __init__(self, title, buttons):
        if (not all(isinstance(button, Button) for button in buttons)):
            raise ValueError('Invalid Buttons instances.')

        payload = {
            'title': title,
            'buttons': [
                button.invoke() for button in buttons
            ]
        }

        super().__init__('button', payload)

    def message(self):
        return super(ButtonTemplate, self).message()


class GenericTemplate(Template):
    def __init__(self, elements, shareable, image_aspect_ratio):
        if (not all(isinstance(element, Element) for element in elements)):
            raise ValueError('Invalid Elements instances.')

        payload = {
            'elements': [
                element.invoke() for element in elements
            ]
        }

        if (shareable):
            payload['sharable'] = shareable

        if (image_aspect_ratio):
            payload['image_aspect_ratio'] = image_aspect_ratio

        super(GenericTemplate, self).__init__('generic', payload)

    def message(self):
        return super().message()


class ListTemplate(Template):
    def __init__(self, elements, buttons=None, top_element_style=None):
        if (not all(isinstance(element, Element) for element in elements)):
            raise ValueError('Invalid Elements instances.')

        payload = {
            'elements': [
                element.invoke() for element in elements
            ]
        }

        if (buttons):
            if (not all(isinstance(button, Button) for button in buttons)):
                raise ValueError('Invalid Buttons instances.')

            payload['buttons'] = [
                button.invoke() for button in buttons
            ]

        if (top_element_style):
            payload['top_element_style'] = top_element_style

        super().__init__('list', payload)

    def message(self):
        return super().message()
