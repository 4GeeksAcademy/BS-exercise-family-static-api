"""
This module takes care of starting the API Server, Loading the DB, and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors as a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET ALL MEMBERS
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# GET SINGLE MEMBER BY ID
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

# ADD NEW MEMBER
@app.route('/member', methods=['POST'])
def add_member():
    member = request.get_json()
    
    if not member or 'first_name' not in member or 'age' not in member or 'lucky_numbers' not in member:
        return jsonify({"error": "Invalid member data"}), 400
    
    jackson_family.add_member(member)
    return jsonify({"message": "Member added successfully"}), 200

# DELETE MEMBER
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    if jackson_family.get_member(id):
        jackson_family.delete_member(id)
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

# Run the app if this script is executed directly
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
