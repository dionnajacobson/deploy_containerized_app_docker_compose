from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/
app = FastAPI(title='Face-Bokeh and Face-Emotion', root_path='./')#root_path='/Prod/')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    return {requests.get(url='http://face-bokeh:8001'), requests.get(url='http://face-emotion:8002')}



