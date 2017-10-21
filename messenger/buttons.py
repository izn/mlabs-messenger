import validators


class Button(object):
    def __init__(self):
        pass

    def invoke(self):
        return self.button_dict


class URLButton(Button):
    def __init__(
        self,
        title,
        url,
        webview_height_ratio=None,
        messenger_extensions=None,
        fallback_url=None,
        webview_share_button=None
    ):
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.button_dict = {
            'type': 'web_url',
            'title': title,
            'url': url
        }

        if (webview_height_ratio):
            self.button_dict['webview_height_ratio'] = webview_height_ratio

        if (messenger_extensions):
            self.button_dict['messenger_extensions'] = messenger_extensions

        if (fallback_url):
            self.button_dict['fallback_url'] = fallback_url

        if (webview_share_button):
            self.button_dict['webview_share_button'] = webview_share_button


class PostbackButton(Button):
    def __init__(self, title, payload):
        self.button_dict = {
            'type': 'postback',
            'title': title,
            'payload': payload
        }


class CallButton(Button):
    def __init__(self, title, payload):
        self.button_dict = {
            'type': 'phone_number',
            'title': title,
            'payload': payload
        }


class ShareButton(Button):
    def __init__(self, title, share_contents=None):
        self.button_dict = {
            'type': 'share', 'title': title
        }

        if (share_contents):
            self.button_dict['share_contents'] = share_contents


class BuyButton(Button):
    def __init__(self, title, payload, payment_summary):
        self.button_dict = {
            'type': 'payment',
            'title': title,
            'payload': payload,
            'payment_summary': payment_summary
        }


class LogInButton(Button):
    def __init__(self, url):
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.button_dict = {
            'type': 'account_link',
            'url': url
        }


class LogOutButton(Button):
    def __init__(self):
        self.button_dict = {
            'type': 'account_unlink'
        }
