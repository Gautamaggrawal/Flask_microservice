import json
from flask import request
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import create_app, database
from .models import KeyValue, User, db
from flask_login import login_required, current_user
app = create_app()


@app.route('/', methods=['GET'])
@login_required
def fetch():
    print(current_user.email)
    user=User.query.filter_by(email=current_user.email).first()
    # keyvalue = database.get_all(KeyValue)
    print(user.keyvalue)
    # return json.dumps(list(user.keyvalue))
    # kv = []
    # for i in keyvalue:
    #     k_v = {
    #         "key": i.key,
    #         "value": i.value,
    #     }

    #     kv.append(k_v)
    # return json.dumps(kv), 200


@app.route('/add', methods=['POST','GET'])
@login_required
def add():
    if request.form:
        request.form.get('key')
        key = request.form.get('key')
        value = request.form.get('value')
        user = User.query.filter_by(email=current_user.email).first()
        new_keyvalue = KeyValue(key=key,value=value,user_id=user.id)
        db.session.add(new_keyvalue)
        db.session.commit()
    user=User.query.filter_by(email=current_user.email).first()
    return render_template('timeline.html',kv=user.keyvalue)


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200
