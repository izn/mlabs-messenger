import json
import requests


class MessengerClient(object):
    """The MessengerClient is used to send messages to users.
    """

    API_URL = 'https://graph.facebook.com/v2.9/me/messages'

    def __init__(self, token):
        """
        Parameters
        ----------
        token : str
            the page access token.
        """
        self.token = token

    def send(self, recipient_id, content):
        """Makes a POST request with the JSON payload to Messenger Platform.

        Parameters
        ----------
        recipient_id : str
            the page access token.
        content : object
            any object that responds to the message method.
        """
        response = requests.post(
            self.API_URL,
            params={'access_token': self.token},
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'recipient': {'id': recipient_id},
                'message': content.message()
            })
        )

        return response
