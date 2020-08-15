from flask import Blueprint, jsonify
from random import *

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
  response = {'msg': "Hello {}".format(name)}
  return jsonify(response)

@app.route("/api/product", methods=["GET"])
# select * from products    
def getProductList():
  product_list = db.session.query(Product).all()

  if product_list == None:
    return[]
  else:
    return product_list