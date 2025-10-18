from urllib.request import urlopen

def getPrice(food):
    if(html.find(food) != -1)
        foodNameIndex = html.find(food)
        taxIndex = html.find("税込", foodNameIndex)
        yenIndex = html.find("円", foodNameIndex)
        price = html[taxIndex + 3 : yenIndex]
        return price
    return -1

def whichWebpage(userInputCategory):
    #selects webpage based on user input
    url = dictFoods(userInputCategory)
    food = userInputFood

    #opens webpage and pulls html to string
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    dictFoods = {"vegetables" : "https://netsuper.rakuten.co.jp/seiyu/search/110001/?l-id=_leftnavi_110001&sort=1",
                 "fruits" : "https://netsuper.rakuten.co.jp/seiyu/search/110002/?l-id=_leftnavi_110002&sort=1",
                 "meats" : "https://netsuper.rakuten.co.jp/seiyu/search/110003/?l-id=_leftnavi_110003&sort=1",
                 "fish" : "https://netsuper.rakuten.co.jp/seiyu/search/110004/?l-id=_leftnavi_110004&sort=1",
                 "dairy" : "https://netsuper.rakuten.co.jp/seiyu/search/110007/?l-id=_leftnavi_110007&sort=1",
                 "rice" : "https://netsuper.rakuten.co.jp/seiyu/search/110010/?l-id=_leftnavi_110010&sort=1"}
