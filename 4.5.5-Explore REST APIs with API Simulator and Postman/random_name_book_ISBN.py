import requests
import json
from faker import Faker
fake = Faker()
print('My name is {}.and I wrote "{}"(ISBN {})'.format(fake.name(),fake.catch_phrase(),fake.isbn13()))
for i in range(10):
    print(fake.name())