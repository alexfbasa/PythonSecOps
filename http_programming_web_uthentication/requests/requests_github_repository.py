#!/usr/bin/env python
import requests

response = requests.get('https://api.github.com/users/alexfbasa')
print(response.url)
print(response.text)
