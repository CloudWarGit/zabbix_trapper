#! /usr/bin/env python3
from flask import Flask
from flask import request
from zbx_trapper import get_data
from werkzeug.exceptions import BadRequest

app=Flask(__name__)
app.debug=True

@app.route('/', methods=['POST'])
def recevice_data():
    json_data=None
    result=""
    if request.method == 'POST':
        try:
            json_data=request.get_json()
            print(json_data)
        except BadRequest as e:
            return "the monitor data should be json format, please check it! \n"

    if json_data:
        result=get_data(json_data)
    else:
        result="please provid monitor data! \n"

    return result

@app.errorhandler(404)
def not_found(error):
    return "error"


if __name__=="__main__":
    app.run()
