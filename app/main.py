from fastapi import FastAPI

app = FastAPI(title="CSE120 GitHub Workshop")


@app.get("/health")
def health():
    return {"status": "ok"}