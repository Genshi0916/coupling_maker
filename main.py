import random

idol = [
  '櫻木真乃','風野灯織','八宮めぐる',
  '月岡恋鐘','田中摩美々','白瀬咲耶','三峰結華','幽谷霧子',
  '小宮果穂','園田智代子','西城樹里','杜野凛世','有栖川夏葉',
  '桑山千雪','大崎甘奈','大崎甜花',
  '芹沢あさひ','黛冬優子','和泉愛依',
  '浅倉透','樋口円香','福丸小糸','市川雛菜',
  '七草はづき'
]

# print("\n\n\n" + idol[random.randint(0,len(idol)-1)] + " ✕  " + idol[random.randint(0,len(idol)-1)] + "\n\n\n")

seme = idol[random.randint(0,len(idol)-1)]
uke = idol[random.randint(0,len(idol)-1)]

if seme == "風野灯織" and uke == "田中摩美々":
  seme = "田中摩美々"
  uke ="風野灯織"

print("\n\n\n" + seme + " ✕  " + uke + "\n\n\n")
