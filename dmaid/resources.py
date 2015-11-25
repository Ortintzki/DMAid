import json
import flask_restful as restful

from flask import abort, render_template, make_response
from flask_restful import reqparse
from dmaid import api, mongo


# TODO: Kill this
class ReadingList(restful.Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('reading', type=str)
        super(ReadingList, self).__init__()

    def get(self):
        return [x for x in mongo.db.readings.find()]

    def post(self):
        args = self.parser.parse_args()
        if not args['reading']:
            abort(400)

        jo = json.loads(args['reading'])
        reading_id = mongo.db.readings.insert(jo)
        return mongo.db.readings.find_one({"_id": reading_id})


# TODO: Kill this
class Reading(restful.Resource):
    def get(self, reading_id):
        return mongo.db.readings.find_one_or_404({"_id": reading_id})

    def delete(self, reading_id):
        mongo.db.readings.find_one_or_404({"_id": reading_id})
        mongo.db.readings.remove({"_id": reading_id})
        return '', 204


# TODO: Kill this
class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }


class Home(restful.Resource):
    def get(self):
        return render_response('home.html')



api.add_resource(Home, '/')
api.add_resource(Root, '/root/')
api.add_resource(ReadingList, '/readings/')
api.add_resource(Reading, '/readings/<ObjectId:reading_id>')


def render_response(template, **context):
    """
    A helper to render a response with a page template.
    :param template: the template to render
    :param context: the context args of the template
    :return: a response object with the template already rendered
    """
    return make_response(render_template(template, **context))
