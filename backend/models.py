from backend import db
from sqlalchemy.dialects.mysql import MEDIUMBLOB

def init():
    db.create_all()

class Product(db.Model):
    __tablename__ = 'products'
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
            imgName =product['imgName'],
            name = product['name'],
            cost = product['cost'],
            area = product['area'],
            stock = product['stock'],
            review = product['review']
        )

        db.session.add(record)
        db.session.commit()

        return product

#class UserSchema(ma.ModelSchema):
    #class Meta:
      #model = Product
      #fields = ('id','imgName', 'name', 'cost', 'area', 'stock','review')
