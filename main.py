# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from api.default import default_chain
from api.recommend import recommend_chain, format_change

app = FastAPI()

@app.get('/')
def load_root():
  return {'hi': "server is running💭"}

# 사용자 입력값(데이터 모델) 정의
class UserInput(BaseModel):
  input_text: str

# userid integer | string 나중에 변경
# 일반대화 체인 (default chain)
@app.post('/api/{userid}/default')
def load_default(userid: str, user_input: UserInput):
  response = default_chain.invoke({"classification_result": "default",
                                   "user_input": user_input.input_text})
  return {'user_id': userid, "response": response}

# 추천요청 체인
@app.post('/api/{userid}/recommend')
def load_recommend(userid: str, user_input: UserInput):
  formatted_input = format_change({"type": "추천요청"}, user_input.input_text)
  response = recommend_chain.invoke(formatted_input)
  return response