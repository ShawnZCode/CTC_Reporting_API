"""Local pydantic base model(s) for the APICore module."""

from pydantic import BaseModel


# Base Model(s)
class LocalBaseModel(BaseModel):
    def update(self, **kwargs):
        for field, value in kwargs.items():
            if hasattr(self, field):
                setattr(self, field, value)
