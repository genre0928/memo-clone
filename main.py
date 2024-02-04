from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel) :
    id : str
    content : str

memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo) :
    memos.append(memo)
    return '메모 추가 성공'

@app.get("/memos")
def read_memo() :
    return memos

app.mount("/", StaticFiles(directory="memo-clone/static", html=True), name="static")