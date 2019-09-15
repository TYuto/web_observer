import requests

def passwordAuth(site):
    payload = {"password": site.password }
    result = requests.post(site.url,data=payload)
    return getBody(result.text)

def default(site):
    result = requests.get(site.url)
    return getBody(result.text)

def getBody(text):
    start = text.find("<body")
    end = text.find("</body")
    text = text[start:end]
    text = text[text.find(">") + 1:]
    return text