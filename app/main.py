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

    numbers_input = ui.input("Numbers (comma-separated)")
    result = ui.label("")

    def calculate_average() -> None:
        try:
            values = [float(value.strip()) for value in numbers_input.value.split(",")]
            if not values:
                raise ValueError
        except ValueError:
            result.text = "Enter one or more valid numbers."
            return

        result.text = f"Average: {sum(values) / len(values):g}"

    def reset() -> None:
        numbers_input.value = ""
        result.text = ""

    with ui.row():
        ui.button("Calculate", on_click=calculate_average)
        ui.button("Reset", on_click=reset)


ui.run_with(app)