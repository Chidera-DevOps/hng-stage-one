from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health():
    return {"message": "healthy"}

@app.get("/me")
async def me():
    return {
        "name": "0xdera_24", 
        "email": "deradev24@gmail.com",
        "github": "https://github.com/Chidera-DevOps"
    }
