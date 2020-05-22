from flask_restful import Resource, Api
from flask import Flask

application = Flask(__name__)
api = Api(application)

class index(Resource):
  def get(self):
    return 'Hello World'

api.add_resource(index, '/')

if __name__ == '__main__':
  application.run(debug=True)