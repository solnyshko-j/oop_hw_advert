import keyword
import random
import json


class ColorizeMixin:
    """
    print colored title and price
    """

    def __repr__(self):
        color = f"\033[1;{self.repr_color_code};10m"
        white_color = "\033[0;0;8m"
        return f"{color} {self.title} | {self.price} ₽{white_color} "


class Advert(ColorizeMixin):
    """
    make advert structure
    check that price > 0 or set price = 0 if there are no price

    """

    def __init__(self, params):
        if isinstance(params, dict):
            self.params = params
        else:
            json.loads(params)
        self.repr_color_code = random.choice([32, 33, 34, 35])

        price = 0
        if "price" in self.params:
            price = int(self.params["price"])
            if price < 0:
                raise ValueError("price must be<0, but {price=}")
        self.price = price

    def __getattr__(self, item):
        if keyword.iskeyword(item[:-1]):
            return self.params[item[:-1]]
        # if locations:
        if type(self.params[item]) == dict:
            return Advert(self.params[item])
        return self.params[item]


try:
    print('LESSON ADVERT:title": "Python", "price": -1')
    lesson = {"title": "Python", "price": -1}
    lesson_ad = Advert(lesson)
    print(f"{lesson_ad= }")
    print(f"{lesson_ad.title= }")
    print(f"{lesson_ad.price= }")
    print()

except ValueError as e:
    print(e, "trying another price =0:")
    print('LESSON ADVERT:title": "Python", "price": 0')
    lesson = {
        "title": "Python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"],
        },
    }

    lesson_ad = Advert(lesson)
    print(f"{lesson_ad= }")
    print(f"{lesson_ad.title= }")
    print(f"{lesson_ad.price= }")
    print()


print("CORGI ADVERT:")
corgi = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское,
                    поселок санатория Тишково, 25"
      }
    }"""
corgi_ad = Advert(corgi)
print(f"{corgi_ad= }")
print(f"{corgi_ad.title= }")
print(f"{corgi_ad.price= }")
print(f"{corgi_ad.location.address= }")
print()
