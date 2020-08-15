from flask import Blueprint, jsonify
from random import *

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
  response = {'msg': "Hello {}".format(name)}
  return jsonify(response)

# Product一覧取得
@api.route("/api/product", methods=["GET"])
# select * from products    
def getProductList():
  product_list = db.session.query(Product).all()

  if product_list == None:
    return[]
  else:
    return product_list
# ショッピングカート
@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
  item = json.loads(request.data.decode('utf-8'))