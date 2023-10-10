from pydantic import BaseModel
from utils.utils import FilterBy

class UserFilterRequest(BaseModel):
    filter_type: FilterBy
    filter_value: str