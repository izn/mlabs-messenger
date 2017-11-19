import validators
from .buttons import ButtonGenerator


class BaseElement(object):
    def __init__(self):
        pass


class ElementGenerator(BaseElement):
    def __new__(self, elements):
        if (not all(isinstance(element, BaseElement) for element in elements)):
            raise ValueError('Invalid Elements instances.')

        return [element.elem_dict for element in elements]


class Element(BaseElement):
    def __init__(
        self,
        title=None,
        subtitle=None,
        image_url=None,
        default_action=None,
        buttons=None
    ):
        self.elem_dict = {
            'title': title
        }

        if (subtitle):
            self.elem_dict['subtitle'] = subtitle

        if (image_url):
            self.elem_dict['image_url'] = image_url

        if (default_action):
            self.elem_dict['default_action'] = ButtonGenerator(default_action)

        if (buttons):
            self.elem_dict['buttons'] = ButtonGenerator(buttons)


class OpenGraphElement(BaseElement):
    def __init__(self, url, buttons=None):
        if (not validators.url(url)):
            raise ValueError('Invalid URL.')

        self.elem_dict = {
            'url': url
        }

        if (buttons):
            self.elem_dict['buttons'] = ButtonGenerator(buttons)


class ReceiptElement(BaseElement):
    def __new__(
        self,
        title,
        price,
        subtitle=None,
        quantity=None,
        currency=None,
        image_url=None
    ):
        self.elem_dict = {
            'title': title,
            'price': price
        }

        if (subtitle):
            self.elem_dict['subtitle'] = subtitle

        if (quantity):
            self.elem_dict['quantity'] = quantity

        if (currency):
            self.elem_dict['currency'] = currency

        if (image_url):
            self.elem_dict['image_url'] = image_url
