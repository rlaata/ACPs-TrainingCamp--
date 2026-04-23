import requests
import time
import os
import webbrowser
from bs4 import BeautifulSoup

# 登录（请修改成你的账号密码）
session = requests.Session()
login_url = 'https://bbs.byr.cn/user/ajax_login.json'
headers = {'x-requested-with': 'XMLHttpRequest'}
login_data = {'id': '你的用户名', 'passwd': '你的密码'}  # ⚠️ 这里改成你自己的账号密码

login_resp = session.post(login_url, data=login_data, headers=headers)
print("登录状态:", login_resp.json()['ajax_msg'])

# 爬取美食版块第1页
page_url = "https://bbs.byr.cn/board/Food?p=1&_uid=你的用户名"  # ⚠️ 注意 _uid 也要改
response = session.get(page_url, headers=headers)

# 保存原始HTML（可选）
with open('byr_page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

# 解析并修复链接
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    old_href = link.get('href')
    if old_href and old_href.startswith('/'):
        new_href = f'https://bbs.byr.cn{old_href}?_uid=你的用户名'  # ⚠️ _uid 也要改
        link['href'] = new_href

# 保存修复后的版本
with open('byr_page_fixed.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('\n完成！已生成 byr_page_fixed.html')

# 自动打开 byr_page_fixed.html
file_path_fixed = os.path.abspath('byr_page_fixed.html')
webbrowser.open(f'file://{file_path_fixed}')
print(f"已自动打开：{file_path_fixed}")