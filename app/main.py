from fastapi import FastAPI
from nicegui import ui

app = FastAPI(title="CSE120 GitHub Workshop")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@ui.page("/")
def home() -> None:
    ui.label("CSE120 GitHub Workshop").classes("text-2xl font-bold")
    ui.label("Average Calculator").classes("text-lg text-gray-600 mb-4")

    numbers_input = ui.textarea(
        label="Numbers (comma or space separated)"
    ).classes("w-full h-32")
    result_label = ui.label(
        "Enter numbers..."
    ).classes("mt-4 text-lg")

    def reset() -> None:
        numbers_input.value = ""
        result_label.text = "Enter numbers..."

    ui.button(
        "Reset",
        on_click=reset,
    ).classes("mt-2 bg-red-500 text-white")
    ui.separator()


ui.run_with(app)