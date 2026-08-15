from pydantic import BaseModel, field_validator, Field, EmailStr, AnyUrl
from typing import List, Dict, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description="Name of the Patient")]
    age : int = Field(gt=0, lt=120)
    weight : float = Annotated[float, Field(gt=0)]
    email : EmailStr
    LinkedIn : AnyUrl
    allergy : List[str]