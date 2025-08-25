from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello, FastAPI & GitLab CI/CD!"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
