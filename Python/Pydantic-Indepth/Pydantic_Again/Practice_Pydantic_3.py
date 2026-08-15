from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Dict, List, Annotated

class Employee(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Enter name of employee')]
    age: Annotated[int, Field(gt=18, lt=60)]
    mail: Annotated[EmailStr, Field(max_length=50)]
    LinkedIn: Annotated[AnyUrl, Field(max_length=50)]
    skillset: Annotated[List[str], Field(max_length=50)]
    contact: Annotated[Dict[str, str], Field(max_length=100)]


    ##@field_validator('age', mode= 'before') ##This will throw an error.
    @field_validator('age', mode= 'after') ##this will pass
    @classmethod
    def age_validator(cls, value):
        if value > 18:
            print('Eligible to vote')
        else:
            print('Not eligible to vote')

    @field_validator('mail')
    @classmethod
    def mail_validator(cls, value):  # Removed type hints here
        print('I am inside mail Validator')
        domain = ['hshc.com', 'gs.com']
        mail_domain = value.split('@')[-1]
        
        if mail_domain not in domain:
            raise ValueError('Domain is not valid')
            
        return value  # Fix: Return the actual value, not a message string

    @field_validator('skillset')
    @classmethod
    def skillvalidator(cls, value):  # Removed type hints here
        print('I am inside skill Validator')
        skills = {'Python', 'Equities', 'Unix', 'SQL', 'RAG'}
        
        # Fix: Iterate over list elements rather than checking if list is in set
        for skill in value:
            if skill not in skills:
                raise ValueError(f'Invalid skill: {skill}')
                
        return value  # Fix: Return the list back to Pydantic


# Sample Execution
Employee_Profile = {
    'name': 'Saurabh',
    'age': '33',
    'mail': 'Saurabh.Ranjan@gs.com',
    'LinkedIn': 'https://linkedin.com/2322',
    'skillset': ['Python', 'SQL', 'Unix', 'Equities', 'RAG'],
    'contact': {
        'phone': '231456',
        'address': 'begur'
    }
}

emp1 = Employee(**Employee_Profile)
print(emp1)