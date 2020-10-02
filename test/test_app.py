from src import app as api
import requests


class TestClass:
    def test_default_route(self):
        app = api.test_client()
        response = app.get('/')
        assert 200 == response.status_code

    def test_default_route(self):
        app = api.test_client()
        response = app.get('/daniel')
        assert 200 == response.status_code

    def test_health_route(self):
        app = api.test_client()
        response = app.get('/health')
        assert 200 == response.status_code
