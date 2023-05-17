import os
from dotenv import load_dotenv

from fastapi import FastAPI, Depends
from fastapi import HTTPException

from teste_logspace.models import SearchRequest, SearchResponse


load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
app = FastAPI()


@app.post("/search")
async def search(query: SearchRequest) -> SearchResponse:
    # summary = await process_with_langchain(query.query)
    
    print(query)
    # print(os.getenv('OPENAI_API_KEY'))
    # if not summary:
    #     raise HTTPException(status_code=404, detail="No results found.")
    
    return {"summary": 'summary'}
