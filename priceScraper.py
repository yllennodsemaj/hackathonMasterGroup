from appJar import gui
from urllib.request import urlopen

app = gui()

foodType = {
    "Dairy": ["white eggs L", "delicious milk", "nature megumi", "Hokkaido pure fresh cream 35",
              "Hokkaido sour cream", "organic soy milk, unsweetened", "almond effect",
             "Tropicana Whole Fruit 100% Orange", "Hokkaido butter", "Hotel margarine", "Cream cheese"],
    "Meat": ["chicken", "pork", "beef"],
    "Fish": ["sashimi trout", "fish fillet mackerel", "white shrimp", "squid fillet cut", "seafood mix",
             "shelled clams", "salted sockeye salmon", "red fish pickled in sake lees", "boiled whitebait", "tarako", "shiokara",
            "wakame seaweed from Naruto waters", "fatty mackerel teriyaki", "fragrant genuine wasabi"],
    "Fruits": [ "banana", "muscat", "kiwi", "gold kiwi", "persimmon", "avocado", "orange"],
    "Vegetables": ["onion", "carrot", "cherry tomato", "green onion", "cucumber",
            "potato", "broccoli", "eggplant", "lettuce", "cabbage", "green pepper",
            "shimeji mushroom", "enoki mushroom", "japanese mustard spinach",
            "half white radish", "chinese cabbage"]
}

dictTranslate = {"white eggs L" : "白たまご L",
             "delicious milk" : "おいしい牛乳",
             "nature megumi" : "ナチュレ 恵 megumi",
             "Hokkaido pure fresh cream 35" : "北海道純生クリーム３５",
             "Hokkaido sour cream" : "北海道サワークリーム",
             "organic soy milk, unsweetened" : "有機豆乳 無調整",
             "almond effect" : "アーモンド効果",
             "Tropicana Whole Fruit 100% Orange" : "トロピカーナ まるごと果実感 100％ オレンジ",
             "Hokkaido butter" : "北海道バター",
             "Hotel margarine" : "ホテルマーガリン",
            "Cream cheese" : "クリームチーズ",
            "sashimi trout" : "サーモントラウト",
            "fish fillet mackerel" : "お魚切り身 さば",
            "white shrimp" : "ホワイトえび",
            "squid fillet cut" : "いか切身カット",
            "seafood mix" : "シーフードミックス",
            "shelled clams" : "あさりむき身",
            "salted sockeye salmon" : "お魚切り身 塩紅鮭",
            "red fish pickled in sake lees" : "漬魚",
            "boiled whitebait" : "釜揚げしらす",
            "tarako" : "たらこ", "shiokara" : "いか塩辛",
            "wakame seaweed from Naruto waters" : "鳴門水域産わかめ",
            "fatty mackerel teriyaki" : "九州産うなぎ蒲焼",
            "fragrant genuine wasabi" : "香る本わさび",
            "banana": "バナナ",
            "muscat": "ぶどう(シャインマスカット)",
            "kiwi": "キウイフルーツ(グリーン)",
            "gold kiwi": "サンゴールドキウイ",
            "persimmon": "かき(種なし柿)",
            "avocado": "アボカド",
            "orange": "オレンジ",
            "chicken": "若どりもも肉 2枚",
            "pork": "豚肉こまぎれ 大",
            "beef": "牛切落し(交雑種)",
            "onion": "玉ねぎ",
            "carrot": "にんじん",
            "cherry tomato": "チェリートマト",
            "green onion": "長ねぎ",
            "cucumber": "きゅうり",
            "potato": "じゃがいも",
            "broccoli": "ブロッコリー(国産)",
            "eggplant": "なす",
            "lettuce": "レタス",
            "cabbage": "キャベツ",
            "green pepper": "ピーマン",
            "shimeji mushroom": "ぶなしめじ",
            "enoki mushroom": "えのき茸",
            "japanese mustard spinach": "小松菜",
            "half white radish": "大根(1/2カット)",
            "chinese cabbage": "白菜(はくさい)"}

dictURL = {"白たまご L" : "https://netsuper.rakuten.co.jp/seiyu/item/4901995100309/",
                "おいしい牛乳" : "https://netsuper.rakuten.co.jp/seiyu/item/4902705126558/",
                "ナチュレ 恵 megumi" : "https://netsuper.rakuten.co.jp/seiyu/item/49212877/",
                "北海道純生クリーム３５" : "https://netsuper.rakuten.co.jp/seiyu/item/49854282/",
                "北海道サワークリーム" : "https://netsuper.rakuten.co.jp/seiyu/item/49853971/",
                "有機豆乳 無調整" : "https://netsuper.rakuten.co.jp/seiyu/item/4902188122290/",
                "アーモンド効果" : "https://netsuper.rakuten.co.jp/seiyu/item/4971666410174/",
                "トロピカーナ まるごと果実感 100％ オレンジ" : "https://netsuper.rakuten.co.jp/seiyu/item/4909411091279/",
                "北海道バター" : "https://netsuper.rakuten.co.jp/seiyu/item/4903050155989/",
                "ホテルマーガリン" : "https://netsuper.rakuten.co.jp/seiyu/item/4970208030238/",
                "クリームチーズ" : "https://netsuper.rakuten.co.jp/seiyu/item/4903050506378/", "サーモントラウト" : "https://netsuper.rakuten.co.jp/seiyu/item/13269915000000/?l-id=category_ranking_item_03",
               "お魚切り身 さば" : "https://netsuper.rakuten.co.jp/seiyu/item/134582404040562/?l-id=category_ranking_item_02",
               "ホワイトえび" : "https://netsuper.rakuten.co.jp/seiyu/item/134969832214039/",
               "いか切身カット" : "https://netsuper.rakuten.co.jp/seiyu/item/134589791876989/",
               "シーフードミックス" : "https://netsuper.rakuten.co.jp/seiyu/item/134940785147285/",
               "あさりむき身" : "https://netsuper.rakuten.co.jp/seiyu/item/134570078000098/",
               "お魚切り身 塩紅鮭" : "https://netsuper.rakuten.co.jp/seiyu/item/134582404040661/",
               "漬魚" : "https://netsuper.rakuten.co.jp/seiyu/item/134978496001367/",
               "釜揚げしらす" : "https://netsuper.rakuten.co.jp/seiyu/item/134984320710145/",
               "いか塩辛" : "https://netsuper.rakuten.co.jp/seiyu/item/134957971807045/",
               "いか塩辛" : "https://netsuper.rakuten.co.jp/seiyu/item/134902584812771/",
               "鳴門水域産わかめ" : "https://netsuper.rakuten.co.jp/seiyu/item/134975041860851/",
               "九州産うなぎ蒲焼" : "https://netsuper.rakuten.co.jp/seiyu/item/134589849071502/",
               "香る本わさび" : "https://netsuper.rakuten.co.jp/seiyu/item/134967825190711/",
               "バナナ": "https://netsuper.rakuten.co.jp/seiyu/item/131098754/",
                "ぶどう(シャインマスカット)": "https://netsuper.rakuten.co.jp/seiyu/item/139394438/",
                "キウイフルーツ(グリーン)": "https://netsuper.rakuten.co.jp/seiyu/item/1394185454/",
                "サンゴールドキウイ": "https://netsuper.rakuten.co.jp/seiyu/item/1394001129/",
                "かき(種なし柿)": "https://netsuper.rakuten.co.jp/seiyu/item/131201390/",
                "アボカド": "https://netsuper.rakuten.co.jp/seiyu/item/131103434/",
                "オレンジ": "https://netsuper.rakuten.co.jp/seiyu/item/131106282/",
               "若どりもも肉 2枚": "https://netsuper.rakuten.co.jp/seiyu/item/130251393000003/",
                "豚肉こまぎれ 大": "https://netsuper.rakuten.co.jp/seiyu/item/130250846000003/",
                "牛切落し(交雑種)": "https://netsuper.rakuten.co.jp/seiyu/item/130217954000004/",
                "玉ねぎ": "https://netsuper.rakuten.co.jp/seiyu/item/131042108/",
                "にんじん": "https://netsuper.rakuten.co.jp/seiyu/item/131029406/",
               "チェリートマト": "https://netsuper.rakuten.co.jp/seiyu/item/131034448/",
               "長ねぎ": "https://netsuper.rakuten.co.jp/seiyu/item/131052930/",
               "きゅうり": "https://netsuper.rakuten.co.jp/seiyu/item/131000368/",
               "じゃがいも": "https://netsuper.rakuten.co.jp/seiyu/item/131038972/",
               "ブロッコリー(国産)": "https://netsuper.rakuten.co.jp/seiyu/item/131006964/",
               "なす": "https://netsuper.rakuten.co.jp/seiyu/item/131011456/",
               "レタス": "https://netsuper.rakuten.co.jp/seiyu/item/131005448/",
               "キャベツ": "https://netsuper.rakuten.co.jp/seiyu/item/131013658/",
               "ピーマン": "https://netsuper.rakuten.co.jp/seiyu/item/131014594/",
               "ぶなしめじ": "https://netsuper.rakuten.co.jp/seiyu/item/131072464/",
               "えのき茸": "https://netsuper.rakuten.co.jp/seiyu/item/131070842/",
               "小松菜": "https://netsuper.rakuten.co.jp/seiyu/item/131046052/",
               "大根(1/2カット)": "https://netsuper.rakuten.co.jp/seiyu/item/131040326/",
               "白菜(はくさい)": "https://netsuper.rakuten.co.jp/seiyu/item/131052640/"}

def webpageToString(translation):
    #selects url based on category
    url = dictURL[translation]

    #opens url and pulls html to string
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")
    
def getPrice(food):
    translation = dictTranslate[food]
    html = webpageToString(translation)
    startIndex = html.find("product-detail-price-without-tax")
    taxIndex = html.find("税込", startIndex)
    yenIndex = html.find("円", taxIndex)
    price = html[taxIndex + 3 : yenIndex]
    price = price.replace(",", "")
    return price

def reset():
    for word in foodType[app.getOptionBox("type")]:
        app.stopSound()
        app.changeOptionBox("food", foodType[app.getOptionBox("type")], word)
        app.loopSound(app.getOptionBox("type") + ".wav")

def resetPrice():
    app.setLabel("JP", dictTranslate[app.getOptionBox("food")])
    price = getPrice(app.getOptionBox("food"))
    app.setLabel("price", price)

app.setSticky("nesw")
app.addLabel("title", "Food Type", 0, 0)
app.addLabel("title2", "Specific food", 0, 1)
app.addLabel("title3", "Price with tax", 2, 2)
app.addLabel("title4", "Written Japanese", 0, 2)
app.setLabelBg("title4", "green")
app.setLabelBg("title", "red")
app.setLabelBg("title2", "blue")
app.addOptionBox("type", foodType, 1, 0)
app.addOptionBox("food", foodType[app.getOptionBox("type")], 1, 1)
app.setOptionBoxChangeFunction("type", reset)
app.setOptionBoxChangeFunction("food", resetPrice)
app.addLabel("JP", app.getOptionBox("food"), 1, 2)
app.addLabel("price", None, 3, 2)
app.addTextArea("cartTxt", 5, 1)
app.addLabel("total", "0", 5, 2)
    

def cartBtn(btn):
    if(not (app.getLabel("total").isdigit())):
        nTotal = int(app.getLabel("price"))
    else:
        price = getPrice(app.getOptionBox("food"))
        nTotal = int(price) + int(app.getLabel("total"))
    app.setTextArea("cartTxt", app.getOptionBox("food") + "\n")
    app.setLabel("total", str(nTotal))
    app.stopSound()
    app.playSound("Money.wav")
    
def clearCartBtn(btn):
    app.setLabel("total", str(0))
    app.clearTextArea("cartTxt")
    
app.addButton("Clear cart", clearCartBtn, 4, 0)
app.addButton("Add to cart", cartBtn, 4, 2)

app.go()
