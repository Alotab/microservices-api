from pathlib import Path

import yaml
from apispec import APISpec
from flask import Flask
from flask_smorest import Api

from api.api import blueprint
from config import BaseConfig


app = Flask(__name__)

# pass the config to the flask app
app.config.from_object(BaseConfig)

# the smorest-api takes the flask instance -app
kitchen_api = Api(app)

# register the created blueprint(imported from the api) to our API object in the kitchen app.py
kitchen_api.register_blueprint(blueprint)

api_spec = yaml.safe_load((Path(__file__).parent / "oas.yaml").read_text())
spec = APISpec(
    title=api_spec["info"]["title"],
    version=api_spec["info"]["version"],
    openapi_version=api_spec["openapi"],
)
spec.to_dict = lambda: api_spec
kitchen_api.spec = spec