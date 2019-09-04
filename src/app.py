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
    user=User.query.filter_by(email=current_user.email).first()
    return render_template('timeline.html',kv=user.keyvalue)


@app.route('/add', methods=['POST','GET'])
@login_required
def add():
    if request.form:
        key = request.form.get('key')
        value = request.form.get('value')
        user = User.query.filter_by(email=current_user.email).first()
        new_keyvalue = KeyValue(key=key,value=value,user_id=user.id)
        db.session.add(new_keyvalue)
        db.session.commit()
    user=User.query.filter_by(email=current_user.email).first()
    return render_template('timeline.html',kv=user.keyvalue)



@app.route('/get', methods=['POST'])
@login_required
def get_value():
    if request.form:
        key = request.form.get('key')
        print(key)
        x=KeyValue.query.filter_by(key=key,user_id=current_user.id)
        print(x)
        return render_template('timeline.html',kv=x)
