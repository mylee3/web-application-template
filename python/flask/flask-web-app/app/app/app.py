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
    status_code = 200

    for id, person in persons.items():
        ret_json[id] = {}
        ret_json[id]["first_name"] = person.first_name
        ret_json[id]["last_name"] = person.last_name
        ret_json[id]["email_address"] = person.email_address

    return jsonify(ret_json), status_code


def create_person(request):
    ret_json = {}
    status_code = 400
    data = request.get_json()

    if data != None:
        status_code = 201
        f_name = data.get("first_name", "")
        l_name = data.get("last_name", "")
        e_address = data.get("email_address", "")

        new_person = Person(f_name, l_name, e_address)

        global ID
        ID = ID + 1
        persons[str(ID)] = new_person

        ret_json["first_name"] = new_person.first_name
        ret_json["last_name"] = new_person.last_name
        ret_json["email_address"] = new_person.email_address

    else:
        ret_json["message"] = "first_name, last_name, and email_address should be given."
    
    return jsonify(ret_json), status_code


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
    status_code = 404

    person = persons.get(person_id)
    
    if person != None:
        status_code = 200
        ret_json["first_name"] = person.first_name
        ret_json["last_name"] = person.last_name
        ret_json["email_address"] = person.email_address
    else:
        ret_json["message"] = "Person with id {id} not found.".format(id=person_id)

    return jsonify(ret_json), status_code


def update_person(request, person_id):
    ret_json = {}
    status_code = 404

    person = persons.get(person_id)

    if person != None:

        status_code = 400
        data = request.get_json()

        if data != None:

            status_code = 200

            if data.get("first_name"):
                person.first_name = data.get("first_name")
            
            if data.get("last_name"):
                person.last_name = data.get("last_name")

            if data.get("email_address"):
                person.email_address = data.get("email_address")

            ret_json["first_name"] = person.first_name
            ret_json["last_name"] = person.last_name
            ret_json["email_address"] = person.email_address

        else:
            ret_json["message"] = "first_name, last_name, or email_address should be given."

    else:
        ret_json["message"] = "Person with id {id} not found.".format(id=person_id)
    
    return jsonify(ret_json), status_code


def delete_person(person_id):

    ret_json = {}
    status_code = 404

    person = persons.get(person_id)

    if person != None:

        status_code = 204

        ret_json["first_name"] = person.first_name
        ret_json["last_name"] = person.last_name
        ret_json["email_address"] = person.email_address

        persons.pop(person_id, None)

    else:
        ret_json["message"] = "Person with id {id} not found.".format(id=person_id)

    return jsonify(ret_json), status_code


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
