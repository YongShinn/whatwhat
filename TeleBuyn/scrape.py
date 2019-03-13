from lxml import html
import requests
from bs4 import BeautifulSoup

list_prod = ['as', 'sa']


def scraping(retailer, link, qty):
    if (retailer == """Colorpop: [$50]💄""" or retailer == "CP"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@class="prod-name"]/text()')
        prod_price = tree.xpath('//*[@id="mainprice"]/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[8:12]
        return list_prod

    elif (retailer == """Sephora: [$40]💄""" or retailer == """Sephora: [$110]💄""" or retailer == "SE"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@class="product-brand"]/a/text()')
        prod_price = tree.xpath(
            '//*[@class="product-price"]/a/text()')
        list_prod[0] = prod_name
        list_prod[1] = prod_price
        return list_prod

    elif (retailer == """Uniqlo: [$60]👚""" or retailer == "UQ"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="goodsNmArea"]/span/text()')
        prod_price = tree.xpath(
            '//*[@id="product-price-7"]/text()')
        list_prod[0] = (prod_name[0])[21:]
        list_prod[1] = (prod_price[0])[2:]
        return list_prod

    elif (retailer == """Zara: [$79]👚""" or retailer == "ZA"):
        page = requests.get(link)
        soup = BeautifulSoup(page.content)
        # tree = html.fromstring(page.content)
        # # This will create a list of buyers:
        # prod_name = tree.xpath(
        #     '//*[@id="product"]/div[1]/div/div[2]/header/h1/text()')
        # prod_price = tree.xpath('//*[@id="product"]/div[1]/div/div[2]/div[1]/span/text()')
        # list_prod[0] = prod_name[0]
        list_prod[1] = soup.select(
            "#product > div.product-info-container._product-info-container > div > div.info-section > div.price._product-price")
        return list_prod

    elif (retailer == """The Editor's Market: [$60]👚""" or retailer == "TE"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="node-product-right-inner"]/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="node-product-price"]/div[' + qty + ']/div[1]/span/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[1:]
        return list_prod

    elif (retailer == """The Tinsel Rack: [$100]👚""" or retailer == "TT"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="product-information"]/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="node-product-price"]/div[1]/span/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[4:]
        return list_prod

    elif (retailer == """Abercrombie & Fitch: [$160]👚""" or retailer == "AN"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        count = 33
        for x in link[33:]:
            if x == '/':
                break
            else:
                count = count + 1
        AFID = (link[count+5:count+11])
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@id="product-' + AFID + '"]/div[2]/div/div/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="product-' + AFID + '"]/div[2]/div/div/div[2]/div/div/div[1]/span[2]/text()')
        list_prod[0] = (prod_name[0])[6:]
        list_prod[1] = prod_price[0]
        return list_prod

    elif (retailer == """Gardenpicks: [$50]🥜""" or retailer == "GP"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="product-544"]/div[2]/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="product-544"]/div[2]/form/div/div[1]/span/span/span')
        list_prod[0] = prod_name
        list_prod[1] = prod_price

    elif (retailer == """MyProtein: [$100]💊""" or retailer == "MP"):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@id="mainContent"]/div[1]/div[5]/div[2]/div/div[1]/div[2]/div/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="mainContent"]/div[1]/div[5]/div[2]/div/div[1]/div[5]/div/p/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[2:]
        return list_prod


# print(scraping("""Sephora: [$40]💄""",
#                """https://www.sephora.sg/products/burts-bees-soap-bark-and-chamomile-deep-cleansing-cream/v/default""", "NA"))
# print(scraping(
#     """Zara: [$79]👚""", """https://www.zara.com/sg/en/check-shirt-p04284415.html?v1=9561638&v2=1181080""", "NA"))
# print(scraping(
#     """Gardenpicks: [$50]🥜""", """http://gardenpicks.com.sg/product/baked-almond-unsalted-top-seller/""", "NA"))
