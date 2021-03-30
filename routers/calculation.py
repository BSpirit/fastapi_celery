from fastapi import APIRouter, status
from typing import Optional
from pydantic import BaseModel
from services import calculation as service
from tasks import calculation as tasks

router = APIRouter(
    prefix="/calculation",
    tags=["Calculation service"]
)


class AddIn(BaseModel):
    a: int
    b: int

    class Config:
        schema_extra = {
            "example": {
                "a": 42,
                "b": 24
            }
        }


class AddOut(BaseModel):
    status: str
    result: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "status": "SUCCESS",
                "result": 42
            }
        }


class TaskId(BaseModel):
    task_id: str

    class Config:
        schema_extra = {
            "example": {
                "task_id": "b1d316af-8de8-4235-8fa1-353fe9eb5d70"
            }
        }


@router.post(
    "/add",
    summary="Add two numbers.",
    response_model=AddOut
)
def add(add_in: AddIn):
    response = {"status": "SUCCESS"}
    response["result"] = service.add(add_in.a, add_in.b)
    return response


@router.post(
    "/long_add",
    summary="Run a background task to add two numbers.",
    response_model=TaskId,
    status_code=status.HTTP_202_ACCEPTED
)
def run_long_add(add_in: AddIn):
    task = tasks.long_add.delay(add_in.a, add_in.b)
    response = {"task_id": task.id}
    return response


@router.get(
    "/long_add/{task_id}/result",
    summary="Retrieve the result of a background task.",
    response_model=AddOut
)
def get_long_add_result(task_id: str):
    result = tasks.long_add.AsyncResult(task_id)

    response = {"status": result.state}
    if result.ready():
        response["result"] = result.get()

    return response
