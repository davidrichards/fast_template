import pytest

from fast_tutorial.domain import model
from fast_tutorial.domain.value_objects import Body, Title


class TestComment:

    @pytest.fixture
    def body(self):
        return Body("body")

    @pytest.fixture
    def comment(self, body):
        return model.Comment(body)

    @pytest.fixture
    def another(self, body):
        return model.Comment(body)

    def test_comment_requires_body(self, body):
        with pytest.raises(TypeError):
            model.Comment()

        subject = model.Comment(body)
        assert subject.body == body

    def test_equality(self, body):
        comment1 = model.Comment(body)
        comment2 = model.Comment(body)
        assert comment1 == comment2

    def test_hash(self, comment, another):
        assert set([comment]) == set([comment, another])

    def test_serialize(self, comment):
        data = {"body": "body"}
        assert comment.serialize() == data
        subject = model.Comment.deserialize(data)
        assert subject == comment


class TestPost:

    @pytest.fixture
    def title(self):
        return Title("title")

    @pytest.fixture
    def body(self):
        return Body("body")

    @pytest.fixture
    def post(self, title, body):
        return model.Post(title, body)

    @pytest.fixture
    def another(self, title, body):
        return model.Post(title, body)

    def test_post_requires_title_and_body(self, title, body):
        with pytest.raises(TypeError):
            model.Post()

        subject = model.Post(title, body)
        assert subject.title == title
        assert subject.body == body

    def test_equality(self, title, body):
        post1 = model.Post(title, body)
        post2 = model.Post(title, body)
        assert post1 == post2

    def test_hash(self, post, another):
        assert set([post]) == set([post, another])

    def test_serialize(self, post):
        data = {"title": "title", "body": "body", "status": "draft", "comments": None}
        assert post.serialize() == data
        subject = model.Post.deserialize(data)
        assert subject == post

    def test_comments(self, post):
        assert post.comments is None
        post.comments = [model.Comment(Body("comment"))]
        assert isinstance(post.comments[0], model.Comment)
        assert post.comments[0].body == "comment"

    def test_status(self, post):
        assert post.status == "draft"
        post.status = "published"
        assert post.status == "published"


class TestAddComment:

    @pytest.fixture
    def post(self):
        return model.Post("title", "body")

    def test_can_add_comment(self, post):
        model.add_comment(post, "comment")
        assert post.comments[0] == "comment"

    def test_add_comment_is_also_a_post_method(self, post):
        post.comment("comment")
        assert post.comments[0] == "comment"


class TestStartPost:

    def test_start_post(self):
        post = model.Post("title", "body")
        assert post.status == "draft"


class TestPublishPost:

    @pytest.fixture
    def post(self):
        return model.Post("title", "body")

    def test_publish_post(self, post):
        assert post.status == "draft"
        model.publish_post(post)
        assert post.status == "published"
