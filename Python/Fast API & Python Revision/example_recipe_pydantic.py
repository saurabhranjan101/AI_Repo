from pydantic import BaseModel
class Recipe(BaseModel):
    title: str  ##datatype hint -- string
    caleries: int
dal = Recipe(title = "Yellow Dal", caleries = 250 )
print(dal.title)
print(dal.caleries)