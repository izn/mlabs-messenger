from .buttons import BaseButton, ButtonGenerator
from .elements import BaseElement, ElementGenerator
from typing import Dict, List, Union, Optional, Collection, Sequence


class Template(object):
    def __init__(self, type: str) -> None:
        self.type = type
        self.payload: Dict[str, Union[
            ButtonGenerator,
            List[ButtonGenerator],
            ElementGenerator,
            str
        ]]

    def message(self) -> Dict[str, Collection[str]]:
        message: Dict[str, Collection[str]] = {
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
    '''The button template sends a text message with up to three attached
    buttons. This template is useful for offering the message recipient options
    to choose from, such as pre-determined responses to a question, or actions
    to take.
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-messages/template/button)
    '''

    def __init__(self, text: str, buttons: Union[BaseButton, List[BaseButton]]) -> None:
        self.payload = {
            'text': text,
            'buttons': ButtonGenerator(buttons)
        }

        super().__init__('button')


class GenericTemplate(Template):
    '''The generic template is a simple structured message
    that includes a title, subtitle, image, and up to three buttons.
    You may also specify a default_action object that sets a URL that will be
    opened in the Messenger webview when the template is tapped.
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic)
    '''

    def __init__(
        self,
        elements: List[BaseElement],
        shareable: Optional[str],
        image_aspect_ratio: Optional[str]
    ) -> None:
        self.payload = {
            'elements': ElementGenerator(elements)
        }

        if (shareable):
            self.payload['sharable'] = shareable

        if (image_aspect_ratio):
            self.payload['image_aspect_ratio'] = image_aspect_ratio

        super().__init__('generic')


class ListTemplate(Template):
    '''The list template is a list of 2-4 structured items with an optional
    global button rendered at the bottom. Each item may contain a thumbnail
    image, title, subtitle, and one button. You may also specify a
    default_action object that sets a URL that will be opened in the Messenger
    webview when the item is tapped.
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-messages/template/list)
    '''

    def __init__(
        self,
        elements: Sequence[BaseElement],
        buttons: Optional[List[BaseButton]] = None,
        top_element_style: Optional[str] = None
    ) -> None:
        self.payload = {
            'elements': ElementGenerator(elements)
        }

        if (buttons):
            self.payload['buttons'] = [ButtonGenerator(buttons)]

        if (top_element_style):
            self.payload['top_element_style'] = top_element_style

        super().__init__('list')
