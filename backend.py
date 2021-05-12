#Coco book trader app
from models.scraper import Scraper
import time


url = ['https://www.webuybooks.co.uk/', 'https://www.zapper.co.uk/', 'https://www.sellitback.com/', 'https://www.ziffit.com/en-gb/', 'https://www.musicmagpie.co.uk/start-selling']
search_bar = ['//*[@id="isbn"]', '//*[@id="form-field-name"]', '*//div[2]/div/input', '//*[@id="barcode"]', '*//div[3]/div/form/div/div[1]/div[1]/input']
get_value_button = ['//*[@id="submit_isbn"]', '*//div[1]/div[2]/button', '*//div[2]/div/div/button', '*//div[3]/button', 
                    '*//div[3]/div/form/div/div[1]/div[2]/input']
get_price_label = ['//*[@id="basketPriceUpdatable"]', '*//div[5]/div/div/div/div/div/p', '*//div[2]/div[1]/span', '*//div[3]/div[1]/label', '*//div[2]/div/span/strong/span']
tabs = ['0','0','0','0', '//*[@id="pills-media-tab"]/div[2]' ]
basket = ['0','0','0','0', '*//div[3]/a/em/strong']
isbn = ["9780241988350", "9781912047734", "9781786574718", "9789683802415", "9197373044", "9780993181443"]

sleepy = 1
bt = Scraper()
prices = []
trade = {}
best_price = 0.0
cart =[]


for item in range(0,4):
    print (url[item])
    bt.scrap_web(url[item]) 
    time.sleep(sleepy)

    bt.change_tab(tabs[item])
    time.sleep(sleepy)

    bt.send_isbn(isbn[0],search_bar[item])
    time.sleep(sleepy)


    bt.get_value(get_value_button[item])
    time.sleep(sleepy)
    
    
    bt.click_basket(basket[item])
    time.sleep(sleepy)
 
    # Error handling for isbn not in url
    try:
        price = bt.get_price(get_price_label[item])
    except Exception:
        price = 0.0
        print('Sorry, this book is not accepted by %s' %url[item])
    
    prices.append(price)

    if price > best_price:
        print('deal')
        best_price = prices[item]
        print(best_price)
        trade = {"price": best_price, "url": url[item], "isbn": isbn[0]}
    
    
 

    bt.driver_close()
    
cart.append(trade)
print(prices)
print (cart)

 
