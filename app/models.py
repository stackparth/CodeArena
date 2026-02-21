from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class SubmitRequest(BaseModel):
    user_id: str
    question_id: int
    code: str

class SkipRequest(BaseModel):
    user_id: str
    question_id: int
