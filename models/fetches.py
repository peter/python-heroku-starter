from model_api import make_model_api
from model_routes import get_model_routes

name = 'fetches'

json_schema = {
  'type': 'object',
  'properties': {
    'id': {'type': 'integer', 'minimum': 1, 'x-meta': {'writable': False}},
    'url_id': {'type': 'integer'},
    'data': {'type': 'string'},
    'created_at': {'type': 'string', 'x-meta': {'writable': False}}
  },
  'additionalProperties': False,
  'required': ['id', 'url_id', 'data', 'created_at']
}

db_schema = f'''
  CREATE TABLE {name} (
    id serial PRIMARY KEY,
    url_id integer not null references urls(id),
    data text NOT NULL,
    created_at TIMESTAMP NOT NULL
  )
'''

db_migrations = []

api = make_model_api(name, json_schema)

routes = get_model_routes(name, json_schema, api)
