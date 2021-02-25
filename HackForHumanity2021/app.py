import os
from typing import Text
import urllib.parse
import json
import models
from flask import Flask, render_template, request
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine, Table, Integer, String, Column
from dotenv import load_dotenv
#from models import User, Business
from random import randint

load_dotenv()

#configure Database URI:
params = urllib.parse.quote_plus(
    f"{os.getenv('DRIVER')}"
    f"{os.getenv('SERVER')}"
    f"{os.getenv('DATABASE')}"
    f"{os.getenv('UID')}"
    f"{os.getenv('PWD')}"
    r'Encrypt=yes;'
    r'TrustServerCertificate=no;'
    r'Connection Timeout=30;'
)
    
conn_str = f'mssql+pyodbc:///?odbc_connect={params}'


#initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/restaurants.html/")
def restaurants():
    restaurants = models.Business.query.filter_by(busn_type="Restaurant").all()
    output = {"Restaurants" : []}
    print(restaurants)
    for r in restaurants:
        output["Restaurants"].append(
            {
                "Name" : r.busn_name,
                "Description" : r.busn_des,
                "Address" : r.busn_add,
            
            }
        )
    response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
    )
    #return render_template("restaurants.html", message=output)
    return response

@app.route("/users/")
def usr_search():

    users = models.User.query.all()
    print(type(users))
    print(users[0].usr_id)
    output = {
        users[0].usr_id : users[0].usr_email,
        users[1].usr_id : users[1].usr_email
    }

    response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
    )
        
    return response
'''
@app.route("/affiliate/")
def affiliate():
    if request.method == "POST":
        username = request.form['username']
        user = models.User.query.filter_by(usr_name=username). '''

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        user = models.User(
            usr_id=randint(0, 10),
            #usr_name=None,
            usr_email=email,
            #usr_pwd=None,
        )
        '''username = request.form['Username']
        user = User.query.filter_by(username=username).first()
        if(not user):
            user = User(
                #usr_id
                usr_name=request.form['Username'],
                usr_email
            )'''
        db.session.add(user)
        db.session.commit()
        print(f'User {user.usr_id}, {user.usr_email} added to database')
        output = {'msg' : 'posted'}
        response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
        )
        
        return response
    return render_template("user.html")

if __name__ == "__main__":
    if(os.getenv("DEBUG")):
        db.drop_all()
    db.create_all()
    app.run()