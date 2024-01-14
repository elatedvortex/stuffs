import requests
response = requests.get("https://blog.bi0s.in/assets/logo.png")
with open("logo2.png", 'wb') as file:
        file.write(response.content)

