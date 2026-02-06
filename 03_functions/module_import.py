import math # built-in module
import myModule # Custom built module
import requests # external library... need to be installed first using `pip install request`

print(math.sqrt(16))

myModule.hello()

r = requests.get("https://google.com")
print(r.text)
