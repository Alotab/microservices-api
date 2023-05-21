from pathlib import Path

import yaml
from fastapi import FastAPI

app = FastAPI(debug=True, openapi_url="/openapi/orders.json", docs_url="/docs/orders")
# app = FastAPI(debug=True)

# overrides the FastAPI openai property. It returns our API specification
oas_doc = yaml.safe_load((Path(__file__).parent / "../oas.yaml").read_text())

app.openapi = lambda: oas_doc

from orders.api import api