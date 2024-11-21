
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from chainlit.utils import mount_chainlit
from pydantic import BaseModel
from config import config
import os

app = FastAPI()

port = int(os.getenv('PORT', 5000))


class PrakritiUpdateRequest(BaseModel):
    prakriti: str


@app.get('/')
def hello():
    return "hello form likhtih"


@app.post('/update-prakriti')
async def update_prakriti(request: PrakritiUpdateRequest):
    global prakriti
    # data = await request.json
    # Update prakriti with the value from the request
    config.prakriti = request.prakriti.lower()
    config.needs_refresh = True
    return JSONResponse(content={"success": True, "prakriti": config.prakriti})


mount_chainlit(app=app, target="app-chainlit.py", path="/chatbot")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=port)
