from datetime import datetime
from pydantic import BaseModel, Field


class TodoModel(BaseModel):
    """Todo Model for storing todo related details."""

    slug: str = Field(...)
    title: str = Field(...)
    description: str = Field(max_length=1000)
    completed: bool = Field(False)
    image: list = Field([])
    date_created: datetime = Field(datetime.now())
    date_modified: datetime = Field(datetime.now())

    def dict(self, *args, **kwargs):
        return super().dict(*args, **kwargs)
