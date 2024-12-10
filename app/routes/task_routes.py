from fastapi import APIRouter


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
    return {
        "id": "1",
        "title": "Acheter des courses",
        "description": "Acheter du lait, du pain et des œufs",
        "dueDate": "2024-10-22T12:00:00",
        "status": "en cours",
        "priority": 2,
        "createdDate": "2024-10-20T08:30:00",
        "updatedDate": "2024-10-20T09:00:00"
    }

@router.post("/tasks")
async def create_task():
  pass