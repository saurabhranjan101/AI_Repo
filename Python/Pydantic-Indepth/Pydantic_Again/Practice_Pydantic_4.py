from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Dict, List, Annotated

class Employee(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    age: Annotated[int, Field(gt=18, lt=60)]
    mail: Annotated[EmailStr, Field(max_length=50)]
    LinkedIn: Annotated[AnyUrl, Field(max_length=50)]
    skillset: Annotated[List[str], Field(max_length=50)]
    contact: Annotated[Dict[str, str], Field(max_length=100)]

    @field_validator('skillset')
    @classmethod
    def skillvalidator(cls, value):
        banking_skills = {'Python', 'Equities', 'Unix', 'SQL', 'RAG'}
        
        # Calculate intersection
        matching_skills = set(value) & banking_skills
        percentage = (len(matching_skills) / len(banking_skills)) * 100
        
        print(f"\n--- Skill Assessment ---")
        print(f"Matched Skills: {list(matching_skills)}")
        print(f"Match Score: {percentage:.0f}%")
        
        # Apply validation logic based on percentage threshold
        if percentage < 40:
            raise ValueError(f"Profile rejected: Skill match is only {percentage:.0f}%. Minimum required is 40%.")
            
        return value


# Example 1: Passing 3 matching skills (60%)
Employee_Profile_1 = {
    'name': 'Saurabh',
    'age': 33,
    'mail': 'Saurabh.Ranjan@gs.com',
    'LinkedIn': 'https://linkedin.com/2322',
    'skillset': ['Python', 'SQL', 'Unix', 'AWS', 'RAG'], # 3 matching banking skills
    'contact': {'phone': '231456', 'address': 'begur'}
}

emp1 = Employee(**Employee_Profile_1)