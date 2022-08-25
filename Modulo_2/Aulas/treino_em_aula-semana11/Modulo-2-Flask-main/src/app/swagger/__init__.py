from flasgger import Swagger
from flask import Flask

def create_swagger(app: Flask):
  app.config['SWAGGER'] = {
    "specs": [
      {
        "endpoint": 'apispec',
        'route': '/apispec.json',
        'rule_filter': lambda rule: True,
        'model_filter': lambda tag: True
      }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/flasgger',
    'openapi': '3.0.0',
    'title': 'Info Api',
    'description': "Aplicação de dados sobre desenvolvedores"
  }

  Swagger(app)