from urllib.request import urlopen

dictWebpages = {"vegetables" : "https://netsuper.rakuten.co.jp/seiyu/search/110001/?l-id=_leftnavi_110001&sort=1",
                 "fruits" : "https://netsuper.rakuten.co.jp/seiyu/search/110002/?l-id=_leftnavi_110002&sort=1",
                 "meats" : "https://netsuper.rakuten.co.jp/seiyu/search/110003/?l-id=_leftnavi_110003&sort=1",
                 "fish" : "https://netsuper.rakuten.co.jp/seiyu/search/110004/?l-id=_leftnavi_110004&sort=1",
                 "dairy" : "https://netsuper.rakuten.co.jp/seiyu/search/110007/?l-id=_leftnavi_110007&sort=1",
                 "rice" : "https://netsuper.rakuten.co.jp/seiyu/search/110010/?l-id=_leftnavi_110010&sort=1"}

dictVegetables = {"にんじん" : "vegetables", "玉ねぎ" : "vegetables", "きゅうり" : "vegetables", "じゃがいも" : "vegetables"}



def webpageToString(category):
    #selects url based on category
    url = dictWebpages[category]

    #opens url and pulls html to string
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")
    
def getPrice(food):
    category = dictVegetables[food]
    html = webpageToString(category)
    foodIndex = html.find(food)
    taxIndex = html.find("税込", foodIndex)
    yenIndex = html.find("円", taxIndex)
    price = html[taxIndex + 3 : yenIndex]
    return int(price)

def addToCart:
    itemName = getName()
    itemPrice = getPrice(food)
    itemQuantity = getQuant()
    newItem = [itemName, itemQuantity, itemPrice]
    shoppingList.add(newItem)
    totalPrice()

def totalPrice():
    nTotal = 0
    for item in ShoppingList:
        nTotal += item[1] * item[2]
    return nTotal

def totalItems():
    nTotal = 0
    for item in shoppingList:
        nTotal += item[1]
    return nTotal
        
#test with carrots

print("Carrots cost: " + getPrice("にんじん"))
print("Onions cost: " + getPrice("玉ねぎ"))
print("Cucumbers cost: " + getPrice("きゅうり"))
print("Potatoes cost: " + getPrice("じゃがいも"))
