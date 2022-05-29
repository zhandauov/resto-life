from fastapi import FastAPI
from pyndatic_basemodels import Item

api = FastAPI()

inventory = {}


@api.get('/')
def index():
    return 'index page'


@api.get('/get_item/{item_id}')
def get_whole_item(item_id: int):
    return inventory[item_id]


@api.get('/get_item/{item_id}/{name}')
def get_item(item_id: int, name: str):
    return inventory[item_id][name]
