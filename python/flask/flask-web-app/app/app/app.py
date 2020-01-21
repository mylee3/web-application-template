from flask import Flask, request, jsonify
from app.models.person import Person
from app.core.database import persons

app = Flask(__name__)
ID = len(persons)

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/api/v1/persons", methods=['GET', 'POST'])
def persons_api():
    
    if request.method == 'GET':
        return list_person()

    else:
        return create_person(request)


def list_person():
    ret_json = {}
    for id, person in persons.items():
        ret_json[id] = {}
        ret_json[id]["first_name"] = person.first_name
        ret_json[id]["last_name"] = person.last_name
        ret_json[id]["email_address"] = person.email_address
    return jsonify(ret_json)


def create_person(request):
    ret_json = {}
    data = request.get_json()
    f_name = data.get("first_name")
    l_name = data.get("last_name")
    e_address = data.get("email_address")

    new_person = Person(f_name, l_name, e_address)

    global ID
    ID = ID + 1
    persons[str(ID)] = new_person

    ret_json["first_name"] = new_person.first_name
    ret_json["last_name"] = new_person.last_name
    ret_json["email_address"] = new_person.email_address

    return jsonify(ret_json)


@app.route("/api/v1/persons/<person_id>", methods=['GET', 'PUT', 'DELETE'])
def person_api(person_id):
    if request.method == 'GET':
        return get_person(person_id)
    
    elif request.method == 'PUT':
        return update_person(request, person_id)
    
    else:
        return delete_person(person_id)


def get_person(person_id):
    ret_json = {}

    person = persons.get(person_id)
    ret_json["first_name"] = person.first_name
    ret_json["last_name"] = person.last_name
    ret_json["email_address"] = person.email_address

    return jsonify(ret_json)


def update_person(request, person_id):
    ret_json = {}
    person = persons.get(person_id)

    data = request.get_json()

    if data.get("first_name"):
        person.first_name = data.get("first_name")
    
    if data.get("last_name"):
        person.last_name = data.get("last_name")

    if data.get("email_address"):
        person.email_address = data.get("email_address")

    ret_json["first_name"] = person.first_name
    ret_json["last_name"] = person.last_name
    ret_json["email_address"] = person.email_address
    
    return jsonify(ret_json)


def delete_person(person_id):

    ret_json = {}
    person = persons.get(person_id)

    ret_json["first_name"] = person.first_name
    ret_json["last_name"] = person.last_name
    ret_json["email_address"] = person.email_address

    persons[person_id] = None

    return jsonify(ret_json)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
