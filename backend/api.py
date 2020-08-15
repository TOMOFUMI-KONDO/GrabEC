from flask import Blueprint, jsonify
from random import *
from backend import db
from backend.models import Product, Menu

api = Blueprint('api', __name__)


# Product一覧取得
@api.route("/product", methods=["GET"])
def getProductList():
  product_list = db.session.query(Product).all()
  task_dict = [product.to_dict() for product in product_list]
  return jsonify(task_dict)


@api.route("/menu", methods=["GET"])
def getMenuList():
  menu_list = db.session.query(Menu).all()
  menu_dict = [menu.to_dict() for menu in menu_list]
  return menu_dict


# ショッピングカート
# @api.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
  # item = json.loads(request.data.decode('utf-8'))
