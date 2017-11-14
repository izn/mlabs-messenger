# mlabs-messenger

[![PyPI](https://img.shields.io/pypi/v/mlabs-messenger.svg)](https://pypi.python.org/pypi/mlabs-messenger)
[![Build Status](https://travis-ci.com/magrathealabs/mlabs-messenger.svg?token=29BMExP3EzBfkxDUwoyJ&branch=master)](https://travis-ci.com/magrathealabs/mlabs-messenger)
[![Code Climate](https://codeclimate.com/github/magrathealabs/mlabs-messenger/badges/gpa.svg)](https://codeclimate.com/github/magrathealabs/mlabs-messenger)
[![Test Coverage](https://codeclimate.com/github/magrathealabs/mlabs-messenger/badges/coverage.svg)](https://codeclimate.com/github/magrathealabs/mlabs-messenger/coverage)
[![license](https://img.shields.io/github/license/magrathealabs/mlabs-messenger.svg)](https://github.com/magrathealabs/mlabs-messenger/blob/master/LICENSE)

A Python wrapper for the Facebook Messenger API

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Documentation](#documentation)

## Installation

Directly from [PyPI](https://pypi.python.org/pypi/mlabs-messenger):

```bash
pip install mlabs-messenger
```

You can also install directly from the GitHub repository to have the newest features by running:

```bash
git clone https://github.com/magrathealabs/mlabs-messenger.git
cd mlabs-messenger
python setup.py install
```

## Usage

#### Text message:

```python
from messenger import MessengerClient
from messenger.content_types import TextMessage


client = MessengerClient(os.environ.get('FACEBOOK_PAGE_TOKEN'))
client.send('recipient_id', TextMessage('message'))
```

### Templates

#### Buttons Template

```python
from messenger import MessengerClient
from messenger.buttons import (
	URLButton,
	PostbackButton,
	CallButton,
	ShareButton,
	LogInButton,
	LogOutButton
)
from messenger.templates import ButtonTemplate


button_list = [
    URLButton('https://example.com', 'Title'),
    PostbackButton('Title', 'PAYLOAD_HERE'),
    CallButton('Title', '+0000000000')
]

client = MessengerClient(os.environ.get('FACEBOOK_PAGE_TOKEN'))
client.send('recipient_id', ButtonTemplate('Title', button_list))
```

#### Generic Template

```python
from messenger import MessengerClient
from messenger.elements import Element
from messenger.templates import GenericTemplate


element_list = [
    Element('Title', 'Subtitle', 'https://example.com/image.jpg'),
    Element('Title', 'Subtitle', 'https://example.com/image.jpg')
]

client = MessengerClient(os.environ.get('FACEBOOK_PAGE_TOKEN'))
client.send('recipient_id', GenericTemplate(element_list, shareable=False, image_aspect_ratio='square'))
```

#### List Template

```python
from messenger import MessengerClient
from messenger.elements import Element
from messenger.templates import ListTemplate


element_list = [
    Element('Title', 'Subtitle', 'https://example.com/image.jpg'),
    Element('Title', 'Subtitle', 'https://example.com/image.jpg')
]

client = MessengerClient(os.environ.get('FACEBOOK_PAGE_TOKEN'))
client.send('recipient_id', ListTemplate(element_list))
```

### Payment

```python
from messenger import MessengerClient
from messenger.buttons import BuyButton
from messenger.payment import PaymentSummary, PaymentPriceList
from messenger.templates import ButtonTemplate


price_list = [
    PaymentPriceList('Beer', '5.00'),
    PaymentPriceList('Hamburger', '10.00'),
]

buy_button = BuyButton(
    'Buy',
    'PAYLOAD_HERE',
    PaymentSummary(
        'USD',
        'FIXED_AMOUNT',
        'Merchant',
        ['shipping_address', 'contact_email'],
        price_list
    )
)

client = MessengerClient(os.environ.get('FACEBOOK_PAGE_TOKEN'))
client.send('recipient_id', ButtonTemplate('Title', buy_button))
```

## Development

Run tests:

```bash
tox
```

See details about the development and releasing process on [DEVELOPMENT.md](https://github.com/magrathealabs/mlabs-messenger/blob/master/DEVELOPMENT.md).

## Documentation

* [Facebook Messenger Documentation](https://developers.facebook.com/docs/messenger-platform)

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## About Magrathea Labs

mlabs-messenger is maintained by Magrathea Labs. The names and logos for Magrathea Labs are trademarks of Magrathea Labs.

Magrathea Labs is a team of specialists in Software Engineering, Distributed Systems, Artificial Intelligence and
Data Science. We love to solve challenging problems and build amazing things. Want to do something amazing with us?
We are available for [hire](mailto:contact@magrathealabs.com).
