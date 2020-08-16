from backend import db
from backend.models import Product, Menu, Material


def seeding():
  # テーブルのデータを消去
  db.session.query(Product).delete()
  db.session.query(Menu).delete()
  db.session.query()

  # 初期データを追加
  product_list = [
      Product(
          id=1,
          imgName='milk.jpg',
          name='みなさまのお墨付き牛乳　成分無調整　1000ml',
          cost=175,
          area='北海道_国産',
          stock=9,
          review=4),
      Product(
          id=2,
          imgName='うどん.jpg',
          name='きほんのき　讃岐うどん　(冷凍)　5食入り',
          cost=185,
          area='香川_国産',
          stock=15,
          review=5),
      Product(
          id=3,
          imgName='ベーコン.jpg',
          name='みなさまのお墨付きベーコン　標準5枚入り4パック',
          cost=258,
          area='東京_国産',
          stock=10,
          review=3),
      Product(
          id=4,
          imgName='納豆.jpg',
          name='極小粒納豆　3パック',
          cost=105,
          area='茨木_国産',
          stock=100,
          review=1),
      Product(
          id=5,
          imgName='絹豆腐.jpg',
          name='みなさまのお墨付き絹豆腐　150g×3',
          cost=75,
          area='仙台_国産',
          stock=50,
          review=2),
      Product(
          id=6,
          imgName='みりん.jpg',
          name='みなさまのお墨付き 本みりん　1000ml',
          cost=245,
          area='東京_国産',
          stock=256,
          review=3),
      Product(
          id=7,
          imgName='egg.jpg',
          name='白玉ミックスたまご　10個入り',
          cost=168,
          area='東京_国産',
          stock=84,
          review=2),
      Product(
          id=8,
          imgName='醤油.jpg',
          name='いつでも新鮮 しぼりたて生しょうゆ　450ml',
          cost=255,
          area='東京_国産',
          stock=64,
          review=4),
      Product(
          id=9,
          imgName='ほんだし.jpg',
          name='ほんだし　450g',
          cost=648,
          area='東京_国産',
          stock=21,
          review=5),
      Product(
          id=10,
          imgName='ケチャップ.jpg',
          name='みなさまのお墨付き トマトケチャップ　500g',
          cost=138,
          area='仙台_国産',
          stock=654,
          review=4),
      Product(
          id=11,
          imgName='ピーマン.jpg',
          name='ピーマン　1袋',
          cost=157,
          area='栃木_国産',
          stock=84,
          review=1),
      Product(
          id=12,
          imgName='chiken.jpg',
          name='若どりもも肉2枚',
          cost=504,
          area='東京_国産',
          stock=45,
          review=5),
      Product(
          id=13,
          imgName='餃子の皮.jpg',
          name='うすめ大判餃子の皮　20枚入り',
          cost=130,
          area='東京_国産',
          stock=7,
          review=4),
      Product(
          id=14,
          imgName='豚ひき肉.jpg',
          name='豚ひき肉(解凍) 大　372g',
          cost=398,
          area='鹿児島_国産',
          stock=35,
          review=5),
      Product(
          id=15,
          imgName='にら.jpg',
          name='にら　1束',
          cost=178,
          area='高知_国産',
          stock=12,
          review=2),
  ]

  menu_list = [
      Menu(
          id=1,
          imgName='卵焼き.jpg',
          displayName='卵焼き',
          description="出汁のきいた和風の卵焼きです。"),
      Menu(
          id=2,
          imgName='オムライス.jpg',
          displayName='オムライス',
          description="ふわトロの絶品オムライスです。"),
      Menu(
          id=3,
          imgName='餃子.jpg',
          displayName='餃子',
          description="ジューシーな肉汁があふれ出す餃子です。"),
  ]

  material_list = [
      Material(menuId=1, productId=6),
      Material(menuId=1, productId=7),
      Material(menuId=1, productId=8),
      Material(menuId=1, productId=9),
      Material(menuId=2, productId=7),
      Material(menuId=2, productId=10),
      Material(menuId=2, productId=11),
      Material(menuId=2, productId=12),
      Material(menuId=3, productId=8),
      Material(menuId=3, productId=13),
      Material(menuId=3, productId=14),
      Material(menuId=3, productId=15),
  ]

  db.session.add_all(product_list)
  db.session.add_all(menu_list)
  db.session.add_all(material_list)

  db.session.commit()
