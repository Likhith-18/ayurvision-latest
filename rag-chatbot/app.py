
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from chainlit.utils import mount_chainlit
from pydantic import BaseModel
from config import config
import os
import httpx
from model import execute_prediction

app = FastAPI()

api = FastAPI()

port = int(os.getenv('PORT', 5000))


class PrakritiUpdateRequest(BaseModel):
    prakriti: str


@app.get('/')
def hello():
    return "hello form likhtih"


@app.post('/update-prakriti')
async def update_prakriti(request: PrakritiUpdateRequest):
    config.prakriti = request.prakriti.lower()
    config.needs_refresh = True
    return JSONResponse(content={"success": True, "prakriti": config.prakriti})


@api.post("/predict")
async def predict_prakriti(request: Request):
    input_json = await request.json()
    # input_data = json.dumps(input_json)
    result = execute_prediction(input_json)

    async with httpx.AsyncClient() as client:
        update_response = await client.post("http://localhost:8000/update-prakriti", json={"prakriti": result})

    return {"prediction": result, "update_response": update_response.json()}


mount_chainlit(app=app, target="app-chainlit.py", path="/chatbot")

app.mount('/api', api)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=port)
