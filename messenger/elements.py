import validators


class Element(object):
    def __init__(
        self,
        title=None,
        subtitle=None,
        image_url=None,
        default_action=None,
        buttons=None
    ):
        self.elem_dict = dict({
            'title': title
        })

        if (subtitle):
            self.elem_dict['subtitle'] = subtitle

        if (image_url):
            self.elem_dict['image_url'] = image_url

        if (default_action):
            self.elem_dict['default_action'] = default_action

        if (buttons):
            self.elem_dict['buttons'] = [
                button.invoke() for button in buttons
            ]

    def invoke(self):
        return self.elem_dict


class OpenGraphElement(object):
    def __init__(self, url, buttons=None):
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.elem_dict = {
            'url': url
        }

        if (buttons):
            if (not all(isinstance(button, Button) for button in buttons)):
                raise ValueError('Invalid Buttons instances.')

            self.elem_dict['buttons'] = [
                button.invoke() for button in buttons
            ]

    def invoke(self):
        return self.elem_dict


class ReceiptElement(object):
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

    def invoke(self):
        return self.elem_dict
