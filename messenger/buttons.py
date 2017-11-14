import validators


class BaseButton(object):
    def __init__(self):
        pass


class ButtonGenerator(BaseButton):
    def __new__(self, buttons):
        if (isinstance(buttons, list)):
            if (not all(isinstance(button, BaseButton) for button in buttons)):
                raise ValueError('Invalid Buttons instances.')

            return [button.button_dict for button in buttons]

        return buttons.button_dict


class URLButton(BaseButton):
    def __init__(
        self,
        url,
        title=None,
        webview_height_ratio=None,
        messenger_extensions=None,
        fallback_url=None,
        webview_share_button=None
    ):
        if (not validators.url(url)):
            raise ValueError('Invalid URL.')

        self.button_dict = {
            'type': 'web_url',
            'url': url
        }

        if (title):
            self.button_dict['title'] = title

        if (webview_height_ratio):
            self.button_dict['webview_height_ratio'] = webview_height_ratio

        if (messenger_extensions):
            self.button_dict['messenger_extensions'] = messenger_extensions

        if (fallback_url):
            self.button_dict['fallback_url'] = fallback_url

        if (webview_share_button):
            self.button_dict['webview_share_button'] = webview_share_button


class PostbackButton(BaseButton):
    def __init__(self, title, payload):
        self.button_dict = {
            'type': 'postback',
            'title': title,
            'payload': payload
        }


class CallButton(BaseButton):
    def __init__(self, title, payload):
        self.button_dict = {
            'type': 'phone_number',
            'title': title,
            'payload': payload
        }


class ShareButton(BaseButton):
    def __init__(self, share_contents=None):
        self.button_dict = {
            'type': 'element_share'
        }

        if (share_contents):
            self.button_dict['share_contents'] = share_contents


class BuyButton(BaseButton):
    def __init__(self, title, payload, payment_summary):
        self.button_dict = {
            'type': 'payment',
            'title': title,
            'payload': payload,
            'payment_summary': payment_summary
        }


class LogInButton(BaseButton):
    def __init__(self, url):
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.button_dict = {
            'type': 'account_link',
            'url': url
        }


class LogOutButton(BaseButton):
    def __init__(self):
        self.button_dict = {
            'type': 'account_unlink'
        }
