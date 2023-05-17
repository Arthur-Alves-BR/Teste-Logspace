from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    summary: str
