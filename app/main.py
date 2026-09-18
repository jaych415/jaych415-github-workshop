from fastapi import FastAPI
from nicegui import ui

app = FastAPI(title="CSE120 GitHub Workshop")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@ui.page("/")
def home() -> None:
    ui.label("CSE120 GitHub Workshop").classes("text-2xl font-bold")
    ui.label("Average Calculator").classes("text-lg text-gray-600")


ui.run_with(app)