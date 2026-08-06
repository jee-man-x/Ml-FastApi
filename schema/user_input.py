from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
import pandas as pd
import pickle

#pydentic opject for incomimg
class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=100,description='age of user')]
    sex:Annotated[str,Field(...,description='Sex of user')]
    bmi:Annotated[float,Field(...,gt=0,description='Bmi of user')]
    smoker:Annotated[str,Field(...,description='is user smoke')]
    region:Annotated[str,Field(...,description='region of user')]
    expenses:Annotated[float,Field(...,description='age of user')]
    