from flask import Blueprint, jsonify
from random import *
from backend import db
from backend.models import Product

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
  response = {'msg': "Hello {}".format(name)}
  return jsonify(response)

# Product一覧取得
@api.route("/product", methods=["GET"])
# select * from products
def getProductList():
  product_list = db.session.query(Product).all()
  task_dict = [product.to_dict() for product in product_list]
  return jsonify(task_dict)

  #if product_list == None:
  #  return[]
  #else:
  #  return product_list

# ショッピングカート
#@app.route('/api/add_to_cart', methods=['POST'])
#def add_to_cart():
  #item = json.loads(request.data.decode('utf-8'))
