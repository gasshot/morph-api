from fastapi import FastAPI
from pydantic import BaseModel
from kiwipiepy import Kiwi

app = FastAPI()
kiwi = Kiwi()

class Text(BaseModel):
    sentence: str

@app.get("/")
def welcome():
    return {"message": "환영합니다! 형태소 분석 API입니다."}

@app.post("/analyze")
def analyze(text: Text):
    # 클라이언트로부터 받은 데이터를 형태소로 분석한 결과를 result 변수
    result = kiwi.analyze(text.sentence) 
    return {"tokens":[token.form for token in result[0][0]]}

# JSON형태로 반환처리리
