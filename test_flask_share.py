import unittest

from flask import Flask, render_template_string, current_app

from flask_share import Share

class ShareTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.testing = True
        self.share = Share(app)

        @app.route('/')
        def index():
            return render_template_string('{{ share.load() }}\n{{ share.create()}}')

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()

    def tearDown(self):
        self.context.pop()

