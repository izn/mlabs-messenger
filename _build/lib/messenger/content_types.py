"""Types of raw (unstructured) content that can be sent to the users.
"""


class TextMessage(object):
    """Send plain text messages using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
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


class AudioAttachment(object):
    """Send sounds by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
    """

    def __init__(self):
        pass


class ImageAttachment(object):
    """Send images by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
    Supported formats are `jpg`, `png` and `gif`.
    """
    def __init__(self):
        pass


class VideoAttachment(object):
    """Send videos by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
    """
    def __init__(self):
        pass


class FileAttachment(object):
    """Send files by uploading them or sharing a URL using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
    """
    def __init__(self):
        pass
