import requests

res = requests.get('https://api.github.com/users/codewithharry')

print(res.json())

# check doc for post, delete and other http methods

