import configparser
import os
import xml.etree.ElementTree as ET
import requests

# 读取配置文件
# 构建配置文件的路径
config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')

config = configparser.ConfigParser()
config.read(config_file_path)

# 从配置文件获取GitHub API令牌和其他配置
token = config['GitHub']['TOKEN']
owner = config['GitHub']['OWNER']
repo = config['GitHub']['REPO']
path = 'docs'

url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    files = response.json()
    for file in files:
        filename = file['name']
        url = file['download_url']
        _, file_extension = os.path.splitext(filename)
        if filename == '36kr-ai.xml':
            # print(f"File Name: {file['name']} - Download URL: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                # 解析xml内容
                xml_content = response.content.decode('utf-8')
                root = ET.fromstring(xml_content)
                print(root)
            else:
                print(response.status_code)

    else:
        print("Failed to retrieve files")
else:
    print(response.json()['message'])
