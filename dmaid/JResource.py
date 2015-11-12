from flask import render_template, make_response


def render_response(template, **context):
    """
    A helper to render a response with a page template.
    :param template: the template to render
    :param context: the context args of the template
    :return:
    """
    return make_response(render_template(template, **context))