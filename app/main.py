import uvicorn
from fastapi import FastAPI, Query
from typing import Annotated, Literal
from pydantic import Field


from app.users.routes import router as user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    return {"task_id": task_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/giner")
async def get_giner(number: int = 0, changer: str = "finger"):
    return {"number": number, "changer": changer}

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.post("/items/")
async def create_item(item: Item):
    ...
    # return item.name.

app.include_router(user_router)

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)