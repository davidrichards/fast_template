from dataclasses import dataclass
from typing import List

from .serialize import serialize, deserialize
from .value_objects import Body, Title


@dataclass
class Comment:
    body: Body

    def __post_init__(self):
        self.body = Body(self.body)

    def __eq__(self, other):
        if not isinstance(other, Comment):
            try:
                if isinstance(other, str):
                    other = {"body": other}
                other = Comment.deserialize(other)
            except:
                return False
        return self.body == other.body

    def __hash__(self):
        return hash(self.body)

    def serialize(self):
        return serialize(self)

    @classmethod
    def deserialize(cls, o):
        if isinstance(o, str):
            o = {"body": o}
        return deserialize(o, cls)


@dataclass
class Post:

    title: Title
    body: Body
    status: str = "draft"
    comments: List[Comment] = None

    def __post_init__(self):
        self.title = Title(self.title)
        self.body = Body(self.body)

    def __eq__(self, other):
        if not isinstance(other, Post):
            try:
                other = Post.deserialize(other)
            except:
                return False
        return self.title == other.title and self.body == other.body

    def __hash__(self):
        return hash((self.title, self.body))

    def serialize(self):
        return serialize(self)

    @classmethod
    def deserialize(cls, o):
        return deserialize(o, cls)

    def comment(self, comment):
        return add_comment(self, comment)


def add_comment(post, comment):
    post = Post.deserialize(post)
    comment = Comment.deserialize(comment)
    if post.comments is None:
        post.comments = []
    if not comment in post.comments:
        post.comments.append(comment)
    return post


def publish_post(post):
    post.status = "published"
    return post


def start_post(title, body):
    return Post(title, body, status="draft")


class Article:
    def __init__(self, post):
        self.post = Post.deserialize(post)

    def publish(self):
        self.post = publish_post(self.post)
        return self
