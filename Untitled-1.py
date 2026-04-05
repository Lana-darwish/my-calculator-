items=["bag","shoes"]
def addItems():
    qes=input("would you like to add item ")
    while qes=="yes":
      items.append(input('add item : '))
      qes=input("would you like to add item ")
      
    else:
      print( items)

addItems()


