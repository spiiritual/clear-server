from pydantic import BaseModel, Field
from typing import Optional, Union, Literal

class EntryInternal(BaseModel):
    title : Optional[str]
    content : str
    timestamp : str
    visibility : Literal["public", "private", "unlisted"]
    owner_username : str
    owner_id : str
    anonymous : bool
    color : str

class EntryToSend(BaseModel):
    title : Optional[str]
    content : str
    timestamp : str
    visibility : Literal["public", "private", "unlisted"]
    owner_username : str

class SuccessfulResponse(BaseModel):
    status : str = Field(default="success")
    response : Union[str, EntryToSend]

class UnsuccessfulResponse(BaseModel):
    status : str = Field(default="failure")
    message : str