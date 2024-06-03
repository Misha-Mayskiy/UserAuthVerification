from pydantic import BaseModel, EmailStr


class RegisterUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class VerifyUserRequest(BaseModel):
    token: str
    email: EmailStr


class EmailRequest(BaseModel):
    email: EmailStr


class ResetRequest(BaseModel):
    token: str
    email: EmailStr
    password: str


class FiltersForGenerationExampleRequest(BaseModel):
    token: str
    example_type: str
    difficulty: str


class AnswerToExample(BaseModel):
    token: str
    user_answer: str
    correct_answer: str
