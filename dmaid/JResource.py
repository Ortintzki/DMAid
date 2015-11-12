import flask_restful as restful
from flask import render_template, make_response


class JResource(restful.Resource):

    def render_response(self, template, **context):
        """
        A helper to render a response with a page template.
        :param template: the template to render
        :param context: the context args of the template
        :return:
        """
        return make_response(render_template(template, **context))

