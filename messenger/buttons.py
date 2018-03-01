import validators
from typing import Dict, List, Union, Optional


class BaseButton(object):
    def __init__(self) -> None:
        self.button_dict: Dict[str, str]


class ButtonGenerator(BaseButton):
    def __new__(self, buttons: Union[List[BaseButton], BaseButton]) -> Union[List[Dict[str, str]], Dict[str, str]]:
        if (isinstance(buttons, list)):
            if (not all(isinstance(button, BaseButton) for button in buttons)):
                raise ValueError('Invalid Buttons instances.')

            return [button.button_dict for button in buttons]

        return buttons.button_dict


class URLButton(BaseButton):
    """The URL Button opens a webpage in the Messenger webview.
    This button can be used with the Button and Generic Templates.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url)
    """

    def __init__(
        self,
        url: str,
        title: Optional[str] = None,
        webview_height_ratio: Optional[str] = None,
        messenger_extensions: Optional[str] = None,
        fallback_url: Optional[str] = None,
        webview_share_button: Optional[str] = None
    ) -> None:
        """
        Parameters
        ----------
        url : str
            Must use HTTPS protocol if messenger_extensions is true.
        title : str, optional
            Must be UTF-8 and has a 20 character limit.
        webview_height_ratio : str, optional
            compact, tall or full. defaults to full.
        messenger_extensions : bool, optional
            Must be true if using Messenger Extensions.
        fallback_url : str, optional
            It may only be specified if messenger_extensions is true.
        webview_share_button : str, optional
            Set to 'hide' to disable the share button in the Webview.
        """
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
    """When the postback button is tapped, the Messenger Platform sends an event
    to your postback webhook. This is useful when you want to invoke an action
    in your bot.
    This button can be used with the Button Template and Generic Template.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)
    """

    def __init__(self, title: str, payload: str) -> None:
        """
        Parameters
        ----------
        title : str
            20 character limit.
        payload : str
            1000 character limit.
        """
        self.button_dict = {
            'type': 'postback',
            'title': title,
            'payload': payload
        }


class CallButton(BaseButton):
    """The Call Button can be used to initiate a phone call.
    This button can be used with the Button and Generic Templates.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/call)
    """

    def __init__(self, title: str, payload: str) -> None:
        """
        Parameters
        ----------
        title : str
            20 character limit.
        payload : str
            Must have "+" prefix followed by the country code, area code and
            local number (i.e: +16505551234).
        """
        self.button_dict = {
            'type': 'phone_number',
            'title': title,
            'payload': payload
        }


class ShareButton(BaseButton):
    """The Share Button enables people to share your content in Messenger.
    Messages shared this way show an attribution to your bot that recipients can
    tap to learn more about your bot.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/share)
    """

    def __init__(self, share_contents: str = None) -> None:
        """
        Parameters
        ----------
        share_contents : str, optional
            Only supports the following:
            - Template used must be generic template.
            - Maximum of one URL button on the template.
        """
        self.button_dict = {
            'type': 'element_share'
        }

        if (share_contents):
            self.button_dict['share_contents'] = share_contents


class BuyButton(BaseButton):
    """ The buy button enables you to build a checkout experience in Messenger.
    This button opens a native checkout dialog that enables people to make
    payments using their information stored in Messenger.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/buy)
    """

    def __init__(self, title: str, payload: str, payment_summary: str) -> None:
        """
        Parameters
        ----------
        title : str
            Must be "Buy".
        payload : str
        payment_summary : dict
            Must be a PaymentSummary dict
        """
        self.button_dict = {
            'type': 'payment',
            'title': title,
            'payload': payload,
            'payment_summary': payment_summary
        }


class LogInButton(BaseButton):
    """The log in button triggers the account linking authentication flow.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/login)
    """

    def __init__(self, url: str) -> None:
        """
        Parameters
        ----------
        url : str
            Must use HTTPS protocol.
        """
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.button_dict = {
            'type': 'account_link',
            'url': url
        }


class LogOutButton(BaseButton):
    """The log out button triggers the account unlinking flow.
    [Send API](https://developers.facebook.com/docs/messenger-platform/reference/buttons/logout)
    """

    def __init__(self) -> None:
        self.button_dict = {
            'type': 'account_unlink'
        }
