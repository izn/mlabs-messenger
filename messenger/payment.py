class PaymentSummary(object):
    def __new__(
        self,
        currency,
        payment_type,
        merchant_name,
        requested_user_info,
        price_list,
        is_test_payment=None
    ):
        if (not isinstance(requested_user_info, list)):
            raise ValueError('Invalid requested_user_info type.')

        if (not all(isinstance(price, PaymentPriceList) for price in price_list)):
            raise ValueError('Invalid PaymentPriceList instances.')

        payment_dict = dict({
            'currency': currency,
            'payment_type': payment_type,
            'merchant_name': merchant_name,
            'requested_user_info': requested_user_info,
            'price_list': [
                price.price_list_dict for price in price_list
            ]
        })

        if (is_test_payment):
            payment_dict['is_test_payment'] = is_test_payment

        return payment_dict


class PaymentPriceList(object):
    def __init__(self, label, amount):
        self.price_list_dict = dict({
            'label': label,
            'amount': amount
        })
