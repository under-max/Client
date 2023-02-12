websites = (
    "https:\\google.com",
    "naver.com",
    "twitter.com",
    "https:\\facebook.com"
)

for website in websites:
    if not website.startswith("https:\\"): # && = and || =or ! =not
        website = f"https:\\{website}"
    print(website)
