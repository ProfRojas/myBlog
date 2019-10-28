from app import myFlaskObj
from flask import render_template

@myFlaskObj.route('/')
def hello():
    username = 'Carlos'
    someList = [1, 3, 2, 5]
    return render_template('index.html', indexUsr=username, indexLst=someList)