from fastapi import Fastapi
import pickle
import pandas as pd
from pydantic import BaseModel, Field, computed_field
from typing import Annotated , Literal


class Model(BaseModel):
    "age" : Annotated(str, Field(...,))