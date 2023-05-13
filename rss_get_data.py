import requests
from lxml import etree


def api_push(data, url="https://fc-mp-707de15b-2c71-4154-ac95-a6a1785a77d4.next.bspapp.com/news/push"):
    response = requests.get(url=url, params=data)
    print(response)


def rss_get_data():
    response = requests.get(url='http://www.people.com.cn/rss/politics.xml')
    response.encoding = "UTF-8"
    html = etree.XML(response.content)

    items = html.xpath("//item")
    for item in items:
        data = {}
        data["title"] = item.xpath("./title/text()")[0]
        data["url"] = item.xpath("./link/text()")[0]
        data["time"] = item.xpath("./pubDate/text()")[0]
        data["author"] = item.xpath("./author/text()")[0]
        api_push(data=data)
        print(data)


# rss_get_data()
