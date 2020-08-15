from backend import db
from backend.models import Product, Menu


def seeding():
  # テーブルのデータを消去
  db.session.query(Product).delete()
  db.session.query(Menu).delete()

  # 初期データを追加
  product_list = [
      Product(
          imgName='milk.jpg',
          name='みなさまのお墨付き牛乳　成分無調整　1000ml',
          cost=175,
          area='北海道_国産',
          stock=9,
          review=4),
      Product(
          imgName='うどん.jpg',
          name='きほんのき　讃岐うどん　(冷凍)　5食入り',
          cost=185,
          area='香川_国産',
          stock=15,
          review=5),
      Product(
          imgName='ベーコン.jpg',
          name='みなさまのお墨付きベーコン　標準5枚入り4パック',
          cost=258,
          area='東京_国産',
          stock=10,
          review=3),
      Product(
          imgName='納豆.jpg',
          name='極小粒納豆　3パック',
          cost=105,
          area='茨木_国産',
          stock=100,
          review=1),
      Product(
          imgName='絹豆腐.jpg',
          name='みなさまのお墨付き絹豆腐　150g×3',
          cost=75,
          area='仙台_国産',
          stock=50,
          review=2),
  ]

  menu_list = [
      Menu(imgName='卵焼き.jpg', displayName='卵焼き', description="出汁のきいた和風の卵焼きです。"),
      Menu(imgName='オムライス.jpg',displayName='オムライス', description="ふわトロの絶品オムライスです。"),
      Menu(imgName='餃子.jpg',displayName='餃子', description="ジューシーな肉汁があふれ出す餃子です。"),
  ]

  db.session.add_all(product_list)
  db.session.add_all(menu_list)

  db.session.commit()
