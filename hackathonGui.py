from appJar import gui

app = gui()


hai = {"1": 199, "2": 100}
English = {"yes": hai, "no": "iie"}

app.setSticky("nesw")
app.addLabel("title", "English", 0, 0)
app.addLabel("title2", "Japanese", 0, 1)
app.addLabel("title3", "Average Price", 0, 2)
app.setLabelBg("title", "red")
app.setLabelBg("title2", "blue")
app.addOptionBox("type", English, 1, 0)
app.addOptionBox("food", English[app.getOptionBox("type")], 1, 1)
app.setOptionBox("food", English[app.getOptionsBox("type")])
app.addTextArea("price", 1, 2)
#app.addTextArea("japanese", , 2)

2,0

def cartBtn(btn):
    app.clearTextArea("food")
    app.setTextArea("price", app.getOptionBox("food"))

app.addButton("cart", cartBtn, 2, 2)

app.go()