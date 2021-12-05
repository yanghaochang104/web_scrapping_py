import requests
from bs4 import BeautifulSoup

# send request to target webpage
result = requests.get(
    'https://coinmarketcap.com/watchlist/60f8a3694dc006143c359066/')

# get whole html file content
soup = BeautifulSoup(result.text, 'lxml')

# TODO: 選取規則皆待優化
# 選取前半部標題


def get_former_title(dom):
    if dom != None and len(dom) != 0:
        for item in dom:
            return item

# 後半部標題的樣式和前半部不同，另外選取


def get_later_title(dom):
    newSoup = BeautifulSoup(f"""{dom}""", 'lxml')
    target = newSoup.find_all('span')
    for index, item in enumerate(target):
        if index == 1:
            return item.get_text()


# 判定數字是否為float，否則回傳 0
def get_price(dom):
    for item in dom:
        price = item.find('span').get_text()[1:]
        try:
            # can convert to float
            return float(price)
        except:
            return 0


# 取得各欄位
data = []
list = soup.table.find_all('tr')
for item in list:
    # select title
    former_title = get_former_title(
        item.find('p', {'class': 'sc-1eb5slv-0 iworPT'}))
    later_title = get_later_title(item.find('a', {'class': 'cmc-link'}))
    title = former_title if former_title != None else later_title

    # select price
    price = get_price(item.select('td:nth-of-type(4)'))

    # select trend of day
    # trend_per_day = item.select('td:nth-of-type(4)')
    # print(trend_per_day)

    # for dom in trend_per_day:
    #     target = dom.find('span').get_text()
    #     if target != '':
    #         print(target)
    #     else:
    #         print('0%')

    # select trend of week

    data.append((title, price))
    
for item in data:
    print(item)

