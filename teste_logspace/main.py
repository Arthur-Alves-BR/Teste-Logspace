import dotenv

from fastapi import FastAPI
from langchain.llms import OpenAI

from .models import SearchRequest, SearchResponse


dotenv.load_dotenv()

llm = OpenAI()
app = FastAPI()


@app.post('/search')
def search(data: SearchRequest) -> SearchResponse:
    return {'summary': llm(data.query)}
