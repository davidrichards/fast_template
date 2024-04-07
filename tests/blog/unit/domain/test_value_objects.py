import pytest

from fast_tutorial.blog.domain import value_objects as model


class TestBody:

    def test_body_is_not_empty(self):
        with pytest.raises(model.BodyInitializationError):
            model.Body("")

    def test_body_is_not_none(self):
        with pytest.raises(model.BodyInitializationError):
            model.Body(None)

    def test_body_is_not_whitespace(self):
        with pytest.raises(model.BodyInitializationError):
            model.Body(" ")

    def test_body_is_not_longer_than_1gb(self):
        too_long = "a" * 1024 * 1024 * 1024 + "a"
        with pytest.raises(model.BodyInitializationError):
            model.Body(too_long)

    def test_body_is_a_string(self):
        body = model.Body("test")
        assert body == "test"
        assert isinstance(body, str)
        assert isinstance(body, model.Body)


class TestTitle:

    def test_title_is_not_empty(self):
        with pytest.raises(model.TitleInitializationError):
            model.Title("")

    def test_title_is_not_none(self):
        with pytest.raises(model.TitleInitializationError):
            model.Title(None)

    def test_title_is_not_whitespace(self):
        with pytest.raises(model.TitleInitializationError):
            model.Title(" ")

    def test_title_is_not_longer_than_1kb(self):
        too_long = "a" * 1024 + "a"
        with pytest.raises(model.TitleInitializationError):
            model.Title(too_long)

    def test_title_is_a_string(self):
        title = model.Title("test")
        assert title == "test"
        assert isinstance(title, str)
        assert isinstance(title, model.Title)
