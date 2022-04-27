from flask_restx import Api

from .post import api as postApi

api = Api()

api.add_namespace(postApi, path="/post")
