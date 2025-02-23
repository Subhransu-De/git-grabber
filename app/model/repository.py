from pydantic import BaseModel


class Repository(BaseModel):
    name: str
    url: str
    default_branch: str
