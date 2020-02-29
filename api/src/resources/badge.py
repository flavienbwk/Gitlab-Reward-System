from flask import Flask
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.badge import badge

app, api = server.app, server.api

# Let's just keep them in memory 
badges_db = [
    {"id": 0, "name": "War and Peace"},
    {"id": 1, "name": "Python for Dummies"},
]

# This class will handle GET and POST to /badges
@api.route('/badges')
class BadgeList(Resource):
    @api.marshal_list_with(badge)
    def get(self):
        return badges_db

    # Ask flask_restplus to validate the incoming payload
    @api.expect(badge, validate=True)
    @api.marshal_with(badge)
    def post(self):
        # Generate new Id
        api.payload["id"] = badges_db[-1]["id"] + 1 if len(badges_db) > 0 else 0
        badges_db.append(api.payload)
        return api.payload

# Handles GET and PUT to /badges/:id
# The path parameter will be supplied as a parameter to every method
@api.route('/badges/<int:id>')
class Badge(Resource):
    # Utility method
    def find_one(self, id):
        return next((b for b in badges_db if b["id"] == id), None)

    @api.marshal_with(badge)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(badge)
    def delete(self, id):
        global badges_db 
        match = self.find_one(id)
        badges_db = list(filter(lambda b: b["id"] != id, badges_db))
        return match

    # Ask flask_restplus to validate the incoming payload
    @api.expect(badge, validate=True)
    @api.marshal_with(badge)
    def put(self, id):
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match