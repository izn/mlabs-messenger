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


class QuickReply(object):
    """Send plain quick replies using the
    [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
    """

    def __init__(self, text, *hash_list):
        self.text = text
        for dictionary in hash_list:
            self.dictionary = dictionary
        """
        Key parameters
        ----------
        content_type : str
            required
            supported formats are "location" and "text"
        title : str
            required if content_type is text
            must be UTF-8 and has a 20 character limit.
        payload : str or int
            required if content_type is text
            must be UTF-8 and has a 1000 character limit.
        image_url : str
            not required, however, should be set to None in the dictionary
            image should be at least 24x24
        """
    def message(self):
        quick_replies = []
        for key in self.dictionary:
            print(key['content_type'])
            if key['content_type'] == 'location':
                quick_replies.append({'content_type': 'location'})
            elif key['content_type'] == 'text':
                quick_replies.append({
                    'content_type': 'text',
                    'title': key['title'],
                    'payload': key['payload'],
                    'image_url': key['image_url']
            })
        return {'text': self.text, 'quick_replies': quick_replies}


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
