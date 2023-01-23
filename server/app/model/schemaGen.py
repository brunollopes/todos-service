# generated by datamodel-codegen:
#   filename:  boardschema.json
#   timestamp: 2023-01-21T19:49:35+00:00

from __future__ import annotations

from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, constr


class Task(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[UUID] = None
    name: str
    description: Optional[str] = str('')
    user: UUID
    status: Optional[constr(regex=r'(Created|Started|Completed)')] = None


class BoardSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[UUID] = None
    name: str
    description: Optional[str] = str('')
    tasks: Optional[List[Task]] = []
