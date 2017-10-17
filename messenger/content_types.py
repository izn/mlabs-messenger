import validators


class TextMessage(object):
    """
    Send plain text messages using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
    """

    def __init__(self, text):
        """
        Parameters
        ----------
        text : str
            must be UTF-8 and has a 640 character limit.
        """
        self.text = text

    def message(self):
        return {'text': self.text}


class Attachment(object):
    def __init__(self, type, url, is_reusable):
        """
        Parameters
        ----------
        type : str
        url : str
            must be a valid URL
        is_reusable : bool
            saves the asset and return an attachment_id
        """
        if (not validators.url(url)):
            raise ValueError('Invalid url.')

        self.type = type
        self.url = url
        self.is_reusable = is_reusable

    def message(self):
        return {
            'attachment': {
                'type': self.type,
                'payload': {
                    'url': self.url,
                    'is_reusable': self.is_reusable
                }
            }
        }


class AudioAttachment(Attachment):
    """Send sounds by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
    """
    def __init__(self, url, is_reusable=False):
        super().__init__('audio', url, is_reusable)


class ImageAttachment(Attachment):
    """Send images by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
    Supported formats are `jpg`, `png` and `gif`.
    """
    def __init__(self, url, is_reusable=False):
        super().__init__('image', url, is_reusable)


class VideoAttachment(Attachment):
    """Send videos by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
    """
    def __init__(self, url, is_reusable=False):
        super().__init__('video', url, is_reusable)


class FileAttachment(Attachment):
    """Send files by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
    """
    def __init__(self, url, is_reusable=False):
        super().__init__('file', url, is_reusable)
