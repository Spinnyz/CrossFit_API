from fastapi import FastAPI

app = FastAPI(title="Meu App")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="