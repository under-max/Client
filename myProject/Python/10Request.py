#pypi 다른사람이 만든 project 나 module 을 모아둔곳 
from requests import get
websites = (
    "https:\\google.com",
    "naver.com",
    "twitter.com",
    "https:\\facebook.com"
)

for website in websites:
    if not website.startswith("https:\\"): # && = and || =or ! =not
        website = f"https:\\{website}"
        response = get(website)
        print(response.status_code)

list_of_number = [1,2,3]
first, second, third = list_of_number #리스트의 길이를 알고 있을 때 
print(first)
print(second)
print(third)
