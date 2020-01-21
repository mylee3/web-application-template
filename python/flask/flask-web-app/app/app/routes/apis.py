from flask import request, jsonify
from ../app import app

@app.route("/api/v1/persons", methods=['GET', 'POST'])
def persons_api():
    
    if request.method == 'GET':
        return list_person()

    else:
        return create_person(request)

def list_person()
    ret_json = {}
    return jsonify(ret_json)

def create_person(request)
    ret_json = {}
    data = request.data
    f_name = data.get("first_name")
    l_name = data.get("last_name")
    e_address = data.get("email_address")

    ret_json["first_name"] = f_name
    ret_json["last_name"] = l_name
    ret_json["email_address"] = e_address

    return jsonify(ret_json)

