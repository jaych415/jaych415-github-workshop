from statistics import mean

from fastapi import FastAPI
from nicegui import ui

app = FastAPI(title="CSE120 GitHub Workshop")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


def parse_and_average(raw: str | None) -> str:
    raw = raw or ""
    tokens = [t for part in raw.split(",") for t in part.strip().split()] if raw else []
    values = [float(t) for t in tokens if t]
    return f"Average: {mean(values):.4f}"


@ui.page("/")
def home() -> None:
    ui.label("CSE120 GitHub Workshop").classes("text-2xl font-bold")
    ui.label("Average Calculator").classes("text-lg text-gray-600 mb-4")

    numbers_input = ui.textarea(
        label="Numbers (comma or space separated)"
    ).classes("w-full h-32")
    result_label = ui.label(
        "Enter numbers and click Compute"
    ).classes("mt-4 text-lg")

    def compute() -> None:
        result_label.text = parse_and_average(numbers_input.value)

    ui.button("Compute Average", on_click=compute).classes("mt-2")
    ui.separator()

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