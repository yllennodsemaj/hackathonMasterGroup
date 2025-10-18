from urllib.request import urlopen

dictWebpages = {"vegetables" : "https://netsuper.rakuten.co.jp/seiyu/search/110001/?l-id=_leftnavi_110001&sort=1",
                 "fruits" : "https://netsuper.rakuten.co.jp/seiyu/search/110002/?l-id=_leftnavi_110002&sort=1",
                 "meats" : "https://netsuper.rakuten.co.jp/seiyu/search/110003/?l-id=_leftnavi_110003&sort=1",
                 "fish" : "https://netsuper.rakuten.co.jp/seiyu/search/110004/?l-id=_leftnavi_110004&sort=1",
                 "dairy" : "https://netsuper.rakuten.co.jp/seiyu/search/110007/?l-id=_leftnavi_110007&sort=1",
                 "rice" : "https://netsuper.rakuten.co.jp/seiyu/search/110010/?l-id=_leftnavi_110010&sort=1"}

dictVegetables = {"にんじん" : "vegetables"}

def getCategory(food):
    return dictVegetables[food]

def whichWebpage(category):
    #selects webpage based on user input
    url = dictWebpages[category]

    #opens webpage and pulls html to string
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")
    
def getPrice(food):
    category = getCategory(food)
    html = whichWebpage(category)
    foodIndex = html.find(food)
    taxIndex = html.find("税込", foodIndex)
    yenIndex = html.find("円", taxIndex)
    price = html[taxIndex + 3 : yenIndex]
    return price

#test with carrots

print("Carrots cost: " + getPrice("にんじん") + "円")



    
