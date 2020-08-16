from flask import Blueprint, jsonify
from random import *
from backend import db
from backend.models import Product, Menu, Material

api = Blueprint('api', __name__)


# Product一覧取得
@api.route("/products", methods=["GET"])
def getProductList():
  product_list = db.session.query(Product).all()
  product_dict = [product.to_dict() for product in product_list]
  return jsonify(product_dict)


# nameで指定したProductを取得
@api.route("/products/<string:name>")
def getProdctFromName(name):
  product_list = db.session.query(Product).filter(
      Product.name.like('%' + name + '%')).all()
  product_dict = [product.to_dict() for product in product_list]
  return jsonify(product_dict)


# idで指定したProductを取得
@api.route("/product/<int:id>")
def getProdct(id):
  product = db.session.query(Product).filter(Product.id == id).first()
  product_dict = product.to_dict()
  return jsonify(product_dict)


# Menu一覧取得
@api.route("/menus", methods=["GET"])
def getMenuList():
  menu_list = db.session.query(Menu).all()
  menu_dict = [menu.to_dict() for menu in menu_list]
  return jsonify(menu_dict)


# idで指定したMenuを取得
@api.route("/menu/<int:id>")
def getMenu(id):
  menu = db.session.query(Menu).filter(Menu.id == id).first()
  menu_dict = menu.to_dict()
  return jsonify(menu_dict)


# menuIdで指定した献立の材料idリストを取得
@api.route("/materials/<int:menuId>")
def getMaterials(menuId):
  product_id_list = db.session.query(
      Material.productId).filter(
      Material.menuId == menuId).all()
  material_dict = [product_id[0] for product_id in product_id_list]
  return jsonify(material_dict)


# ショッピングカート
# @api.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
  # item = json.loads(request.data.decode('utf-8'))
