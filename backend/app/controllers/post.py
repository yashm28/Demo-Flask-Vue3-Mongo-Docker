import sys
sys.path.insert(1, '../controllers')

from flask import request, abort
from flask_restx import Namespace, Resource, fields
from models.post import Post
import json

api = Namespace('post')

post = api.model('Post',{
    'id': fields.String(readonly=True),
    'title': fields.String(required=True),
    'count': fields.Integer(required=True),
    'url': fields.String(),
})

@api.route('/create')
class CreatePost(Resource):

    @api.marshal_with(post, envelope='post')
    def post(self):
        data = request.get_json()
        title = data.get('title')
        count = data.get('count')
        url = data.get('url')
        post = Post(title=title, count=count, url=url)
        post.save()
        return post

@api.route('/createall')
class CreatePost(Resource):

    @api.marshal_list_with(post, envelope='posts')
    def post(self):
        data = request.get_json()
        print(data)
        posts = []
        for record in data.get('posts'):
            title = record.get('title')
            count = record.get('count')
            url = record.get('url')
            post = Post(title=title, count=count, url=url)
            posts.append(post)
        res = Post.objects.insert(posts)
        return res

@api.route('/getall')
class CreatePost(Resource):

    @api.marshal_with(post, envelope='posts')
    def get(self):
        return list(Post.objects())

@api.route('/increment')
class IncrementCount(Resource):

    @api.marshal_with(post, envelope='post')
    def post(self):
        try:
            data = request.get_json()
            id = data.get('id')
            post = list(Post.objects(id=id))
            if len(post) > 0:
                post = post[0]
                post.count = post.count + 1
                post.save()
            else:
                abort(400)
            return post
        except:
            abort(400, 'Something Went Wrong. Please Check If Id or Data is correct.')

@api.route('/decrement')
class DecrementCount(Resource):

    @api.marshal_with(post, envelope='post')
    def post(self):
        try:
            data = request.get_json()
            id = data.get('id')
            post = list(Post.objects(id=id))
            if len(post) > 0:
                post = post[0]
                post.count = post.count - 1
                post.save()
            else:
                abort(400)
            return post
        except:
            abort(400, 'Something Went Wrong. Please Check If Id or Data is correct.')
