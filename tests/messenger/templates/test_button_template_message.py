from messenger.templates import (
    ButtonTemplate,
    URLButton,
    PostbackButton,
    CallButton,
    ShareButton,
    BuyButton,
    LogInButton,
    LogOutButton,
    PaymentSummary,
    PaymentPriceList)


class TestButtonTemplateMessage(object):
    def test_message(self):
        PriceList = [
            PaymentPriceList('Test Item 1', '13.00'),
            PaymentPriceList('Test Item 2', '18.50'),
        ]

        ButtonList = [
            URLButton('Title', 'http://example.com'),
            PostbackButton('Title', 'PAYLOAD_HERE'),
            CallButton('Title', '+0000000000'),
            ShareButton('Share'),
            BuyButton(
                'Buy',
                'PAYLOAD_HERE',
                PaymentSummary(
                    'USD',
                    'FIXED_AMOUNT',
                    'Merchant',
                    ['shipping_address', 'contact_email'],
                    PriceList
                )
            ),
            LogInButton('http://example.com'),
            LogOutButton()
        ]

        assert ButtonTemplate('Title', ButtonList).message() == {
            'attachment': {
                'payload': {
                    'buttons': [{
                        'title': 'Title',
                        'type': 'web_url',
                        'url': 'http://example.com'
                    }, {
                        'payload': 'PAYLOAD_HERE',
                        'title': 'Title',
                        'type': 'postback'
                    }, {
                        'payload': '+0000000000',
                        'title': 'Title',
                        'type': 'phone_number'
                    }, {
                        'title': 'Share',
                        'type': 'share'
                    }, {
                        'payload': 'PAYLOAD_HERE',
                        'payment_summary': {
                            'currency': 'USD',
                            'merchant_name': 'Merchant',
                            'payment_type': 'FIXED_AMOUNT',
                            'price_list': [{
                                'amount': '13.00',
                                'label': 'Test Item 1'
                            }, {
                                'amount': '18.50',
                                'label': 'Test Item 2'
                            }],
                            'requested_user_info': [
                                'shipping_address',
                                'contact_email'
                            ]
                        },
                        'title': 'Buy',
                        'type': 'payment'
                    }, {
                        'type': 'account_link',
                        'url': 'http://example.com'
                    }, {
                        'type': 'account_unlink'
                    }],
                    'template_type': 'button',
                    'title': 'Title'
                },
                'type': 'template'
            }
        }