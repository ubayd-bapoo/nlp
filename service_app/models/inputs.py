from pydantic import BaseModel


class TransactionID(BaseModel):
    transaction_id: str


class InputString(BaseModel):
    input_string: str

