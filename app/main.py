from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def get_user():
    return {"hello": "Hello"}

