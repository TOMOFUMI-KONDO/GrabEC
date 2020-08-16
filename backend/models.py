from backend import db

def init():
    db.create_all()

# 商品
class Product(db.Model):
  __tablename__ = 'products'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  imgName = db.Column(db.String(1000))
  name = db.Column(db.String(1000))
  cost = db.Column(db.Integer)
  area = db.Column(db.String(1000))
  stock = db.Column(db.Integer)
  review = db.Column(db.Integer)

  def to_dict(self):
    return dict(
        id=self.id,
        imgName=self.imgName,
        name=self.name,
        cost=self.cost,
        area=self.area,
        stock=self.stock,
        review=self.review
    )

  def __repr__(self):
    return '<Product %r>' % self.name

  def registProduct(product):
    record = Product(
        imgName=product['imgName'],
        name=product['name'],
        cost=product['cost'],
        area=product['area'],
        stock=product['stock'],
        review=product['review']
    )

    db.session.add(record)
    db.session.commit()

    return product


# オススメする献立
class Menu(db.Model):
  __tablename__ = 'menus'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  imgName = db.Column(db.String(1000))
  displayName = db.Column(db.String(1000))
  description = db.Column(db.String(1000))

  def to_dict(self):
    return dict(
        id=self.id,
        imgName=self.imgName,
        displayName=self.displayName,
        description=self.description
    )

  def __repr__(self):
    return '<Menu %r>' % self.displayName


# 献立に必要な商品
class Material(db.Model):
  __tablename__ = 'materials'
  __table_args__ = {'extend_existing': True}
  menuId = db.Column(
      db.Integer,
      db.ForeignKey(
          'menus.id',
          onupdate='CASCADE',
          ondelete='CASCADE'),
      primary_key=True)
  productId = db.Column(
      db.Integer,
      db.ForeignKey(
          'products.id',
          onupdate='CASCADE',
          ondelete='CASCADE'),
      primary_key=True)

  def to_dict(self):
    return dict(
        menuId=self.menuId,
        productId=self.productId
    )

  def __repr__(self):
    return '<Material %r %r>' % self.menuId, self.productId


# ショッピングカート
class Cart(db.Model):
    __tablename__ = 'cart'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        db.ForeignKey(
          'products.id',
          onupdate='CASCADE',
          ondelete='CASCADE'),
        primary_key=True)
    stock = db.Column(db.Integer)
    
    def to_dict(self):
        return dict(
            id = self.id,
            stock = self.stock
    )

    def __repr__(self):
        return '<Cart %r>' % self.id,self.stock