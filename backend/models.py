from backend import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text
        )

    def __repr__(self):
        return '<Task id={id} title={title!r}>'.format(
            id=self.id, title=self.title)

def init():
    db.create_all()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    imgName = db.Column(MEDIUMBLOB)
    name = db.Column(db.String(1000))
    cost = db.Column(db.Integer)
    area = db.Column(db.String(1000))
    stock = db.Column(db.Integer)
    review = db.Column(db.Integer)

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

class UserSchema(ma.ModelSchema):
    class Meta:
      model = Product
      fields = ('id','imgName', 'name', 'cost', 'area', 'stock','review')