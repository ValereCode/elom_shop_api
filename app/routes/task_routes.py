from fastapi import APIRouter
from app.models.task import Task

router = APIRouter(
    prefix='/task',
    tags=['It will be remove later']
)

@router.get("")
async def root():
    return {
        "key": "12345",
        "activity": "Hiking",
        "type": "recreational",
        "participants": 4,
        "price": 0.0
    }
    
@router.get("/tasks")
async def get_tasks():
    return await Task.find().to_list()

    # return {
    #     "id": "1",
    #     "title": "Acheter des courses",
    #     "description": "Acheter du lait, du pain et des œufs",
    #     "dueDate": "2024-10-22T12:00:00",
    #     "status": "en cours",
    #     "priority": 2,
    #     "createdDate": "2024-10-20T08:30:00",
    #     "updatedDate": "2024-10-20T09:00:00"
    # }

@router.post("/tasks", response_model=Task)
async def create_task(task: Task):
    await Task.insert_one(task)
    return task