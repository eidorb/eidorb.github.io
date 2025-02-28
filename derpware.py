import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="Derpware")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Welcome to Derpware""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
