import validators
from .buttons import ButtonGenerator, BaseButton
from typing import Dict, List, Any, Union, Optional

class BaseElement(object):
    elem_dict: Dict[str, str]


class ElementGenerator(BaseElement):
    def __new__(self, elements: List[BaseElement]) -> List[Dict[str, str]]:
        if (not all(isinstance(element, BaseElement) for element in elements)):
            raise ValueError('Invalid Elements instances.')

        return [element.elem_dict for element in elements]


class Element(BaseElement):
    def __init__(
        self,
        title: str,
        subtitle: Optional[str] = None,
        image_url: Optional[str] = None,
        default_action: Optional[str] = None,
        buttons: Optional[BaseButton] = None
    ) -> None:
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
    def __init__(self, url: str, buttons: Optional[BaseButton] = None) -> None:
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
        title: str,
        price: str,
        subtitle: Optional[str] = None,
        quantity: Optional[str] = None,
        currency: Optional[str] = None,
        image_url: Optional[str] = None
    ) -> None:
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
