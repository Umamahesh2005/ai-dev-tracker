from pydantic import BaseModel

class Developer(BaseModel):
    name: str
    github_username: str
    productivity: float
    support: float
    learning: float
