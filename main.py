from flask import Flask,jsonify
from flask_restful import Resource,Api

app=Flask(__name__)
api =Api(app)


class Student(Resource):
    def get(self,name):
        return jsonify({"student_key":name})


api.add_resource(Student,"/student/<string:name>")

app.run(port=4000)