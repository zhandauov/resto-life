from fastapi import FastAPI
import models
import database
api = FastAPI()

models.Base.metadata.create_all(database.engine)
# print(models.Base.metadata)


@api.get('/')
def index():
    return 'index page'


# @api.get('/get_item/{item_id}')
# def get_whole_item(item_id: int):
#     return inventory[item_id]


# @api.get('/get_item/{item_id}/{name}')
# def get_item(item_id: int, name: str):
#     return inventory[item_id][name]
