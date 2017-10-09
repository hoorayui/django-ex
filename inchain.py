# f141319 222333 230193 888666
# http://cmhyperdrive.com/usercenter/MoneyTransfer2.php
# http://influencechain.org/#/inc
import requests,re

cookies = {
    'PHPSESSID': '9sc28pl8mmqk1m7713kbnsb741',
}

headers = {
    'Host': 'cmhyperdrive.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'http://cmhyperdrive.com/usercenter/MoneyTransfer2.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
}

params = (
    ('act', 'usersave'),
)

data = [
  ('INCPrice', '0.07'),
  ('atebi', '48351.65'),
  ('JYPrice', '1.1'),
  ('JYMoney', '2000'),
  ('BTCPrice', '0.150'),
  ('BTCNum', '7897.44'),
  ('wallet', '230193'),
  ('oHyPassword2', '888666'),
  ('submit', '\u7ACB\u5373\u4E70\u5165'),
]

def post():
    result = requests.post('http://cmhyperdrive.com/usercenter/MoneyTransfer2.php', headers=headers, params=params,cookies=cookies, data=data)
    content = result.content.decode('utf-8')
    while check(content) is False:
        result = requests.post('http://cmhyperdrive.com/usercenter/MoneyTransfer2.php', headers=headers, params=params,
                               cookies=cookies, data=data)
        content = result.content.decode('utf-8')
        print(content)

def check(content):
    # content = r'''<script>alert('denglu！');history.back();</script>'''
    if content.find('申购数量不足')>0:
        return False
    else:
        with open('log.txt','a',encoding='utf-8') as f:
            f.write(content+'\n')
        ret = re.search(r'alert\(\'(.*)\'\)',content)
        if ret:
            print(ret.group(1))
            exit()
        print(content)
        exit()
post()
