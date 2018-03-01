from messenger.content_types import * # noqa ignore=F405
from messenger.templates import * # noqa ignore=F405
from messenger.buttons import * # noqa ignore=F405
from messenger.elements import * # noqa ignore=F405
from messenger.payment import * # noqa ignore=F405

import pprint

PriceList = [
    PaymentPriceList('Cerveja', '13.00'),
    PaymentPriceList('Hambúrguer Vegetariano', '18.50'),
]

ButtonList = [
    URLButton('http://example.com', 'Teste'),
    PostbackButton('Teste', 'PAYLOAD')
]

ElementList = [
    Element('Title'),
    Element('Title', 'Subtitle'),
    Element('Title', 'Subtitle', 'http://image.x'),
    Element('Title', 'Subtitle', 'http://image.url', URLButton('http://example2.com', 'Title 2')),
    Element('Title', 'Subtitle', 'http://image.url', URLButton('http://example3.com', 'Title 3'), [
        URLButton('http://example4.com', 'Title 4')
    ])
]

#
pprint.pprint(ListTemplate(ElementList).message())
pprint.pprint(ButtonTemplate('Title', ButtonList).message())
#pprint.pprint(GenericTemplate(ElementList, shareable=False, image_aspect_ratio='square').message())
#pprint.pprint(AudioAttachment('http://google.com/', is_reusable=True).message())
