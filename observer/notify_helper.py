import requests
import json
import difflib
from .models import Notify, Version
from html2text import html2text
import os

def notify(version):
    for notify in Notify.objects.filter(site=version.site).all():
        eval(notify.key)(notify, version)

def slack(notify, version):
    v = Version.objects.filter(site=version.site, updated_at__lt=version.updated_at).order_by('-updated_at').first()
    text = "HPが更新されました\n"
    text += diff(html2text(v.html), html2text(version.html))
    text += "\n<{}/diff/{}/{}|差分を表示>".format(os.getenv("host", 'http://localhost'),v.id,version.id)
    text += "\n<{}/version/{}|全体を表示>".format(os.getenv("host", 'http://localhost'), version.id)
    requests.post(notify.url, data = json.dumps({
        'text': text,
        'username': u'HP-diff',
        'icon_emoji': u'chrome',
    }))


def diff(texta, textb):
    d = difflib.Differ()
    diff = d.compare(texta, textb)
    print(diff)
    s = ""
    now = " "
    for c in diff:
        s += check(c, now)
        now = c[0]
        if c[2] == "\n":
            s += addtext(now)
            s += "\n"
            s += addtext(now)
        else:
            s += c[2]
    s += check("   ", now)
    s = s.replace("` `", "").replace("~ ~", "")
    return "\n".join(filter(lambda x: "~" in x or "`" in x, s.split("\n")))

def check(c, now):
    s = ""
    if c[0] == "+" and now != "+":
        s += addtext(now)
        s += " `"
    elif c[0] == "-" and now != "-":
        s += addtext(now)
        s += " ~"
    elif c[0] == " " and now != " ":
        s += addtext(now)
    return s

def addtext(now):
    if now == "+":
        return "` "
    elif now == "-":
        return "~ "
    return ""