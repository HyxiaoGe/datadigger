import configparser
import os
from lxml import etree
import requests
from datetime import datetime, timedelta
import pytz

from datadigger.model.article import Article

config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')

config = configparser.ConfigParser()
config.read(config_file_path)

# 从配置文件获取GitHub API令牌和其他配置
token = config['GitHub']['TOKEN']
owner = config['GitHub']['OWNER']
repo = config['GitHub']['REPO']
path = 'docs'


def fetch_xml():
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url=url, headers=headers)

    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
    }

    if response.status_code == 200:
        files = response.json()
        articles = []
        for file in files:
            filename = file['name']
            url = file['download_url']
            _, file_extension = os.path.splitext(filename)
            # if file_extension == '.xml' and 'ai' in filename:
            if filename == '36kr-ai.xml':
                response = requests.get(url)
                if response.status_code == 200:
                    xml_content = response.content.decode('utf-8')
                    try:
                        root = etree.fromstring(xml_content.encode('utf-8'))
                        for item in root.xpath('//item', namespaces=namespaces):
                            title = item.find('title').text
                            link = item.find('link').text
                            content = item.find('content:encoded', namespaces=namespaces).text
                            pub_date = item.find('pubDate').text
                            pub_date = format_date(pub_date)
                            article = Article(title=title, link=link, content=content, publication_date=pub_date)
                            articles.append(article)
                    except etree.XMLSyntaxError as e:
                        print(f"Error parsing XML: {e}")
                else:
                    print(f"Failed to download {filename}: {response.status_code}")
        return articles
    else:
        print(response.json()['message'])


def format_date(date_str):
    dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
    dt = dt.replace(tzinfo=pytz.UTC)
    dt = dt + timedelta(hours=8)
    return dt.strftime("%Y-%m-%d %H:%M:%S")