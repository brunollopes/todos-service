# generated by datamodel-codegen:
#   filename:  userDeletedSchema.json
#   timestamp: 2023-01-23T17:11:54+00:00

from __future__ import annotations

from pydantic import BaseModel


class Data(BaseModel):
    user: str


class UserDeleted(BaseModel):
    time: str
    data: Data
