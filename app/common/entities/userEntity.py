from uuid import UUID
from pydantic import BaseModel

class UserEntity(BaseModel):
    id:UUID
    first_name: str
    last_name: str
    username: str
    password: str

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"