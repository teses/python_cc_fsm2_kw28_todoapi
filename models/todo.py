
from pydantic import BaseModel, Field

class ToDoCreate(BaseModel):
    todo_title : str = Field(
        ...,
        min_length=1,
        max_length=100
    )
    todo_description : str = Field(
        min_length=1,
        max_length=500
    )



#ToDoUpdate


#ToDoResponse