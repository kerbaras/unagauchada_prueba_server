from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView


db = SQLAlchemy()


def create_app():

    from app.schema import schema, default_query
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    db.init_app(app)

    return app
