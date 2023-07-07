from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = []

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    contact = {
        'name': request.json['name'],
        'email': request.json['email'],
        'phone': request.json['phone']
    }
    contacts.append(contact)
    return jsonify({'message': 'Contact added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
