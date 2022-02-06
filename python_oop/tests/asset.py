"""
asset methods
"""
import calculation as c


# def coupon(rate, face_value):
#     return c.polynomial(rate, face_value, c=0)
#
#
# def coupon_rate(coupon, face_value):
#     return c.division(coupon, face_value)


from python_oop.tests.calculation import Calculation


class Asset(Calculation):
    def __init__(self, name='VTI', inception='1900-01-01'):
        self.name = name
        self.inception = inception

    def coupon(self, rate=0.01, face_value=100):
        return self.polynomial(rate, face_value, c=0)

    def coupon_rate(self, coupon=1, face_value=100):
        return self.division(coupon, face_value)


class Bond(Asset):
    def __init__(self, interest_rate=0.01, principal=100, frequency=1, tenor=10):
        super().__init__()
        self.interest_rate = interest_rate
        self.principal = principal
        self.frequency = frequency
        self.tenor = tenor

    def interest(self):
        return self.coupon(self.interest_rate, self.principal)


class Stock(Asset):
    def __init__(self, dividend_rate=0.01, price=100, frequency=1):
        super().__init__()
        self.dividend_rate = dividend_rate
        self.price = price
        self.frequency = frequency

    def dividend(self):
        return self.coupon(self.dividend_rate, self.price)


class UserAsset(Asset):
    def __init__(self, end_date='2021-12-31'):
        super().__init__()
        self.end_date = end_date

    def import_user_asset(self, import_params):
        pass

    def export_user_asset(self, name, date):
        pass

