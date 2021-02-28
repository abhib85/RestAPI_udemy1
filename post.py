from flask import Flask,jsonify
from flask_restful import Resource,Api
app=Flask(__name__)
api =Api(app)

items=[]

class Items(Resource):
    def get(self,name):
        for item in items:
            if item["name"]==name:
                return item
            #else:
            return {"item":None}

    def post(self,name):
        item={"name":name,"price":124}
        items.append(item)
        return item


api.add_resource(Items,"/item/<string:name>")

app.run()