from fastapi import FastAPI # import the fastapi module

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
