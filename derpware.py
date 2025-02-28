import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="Derpware")


@app.cell
def _():
    import github
    import marimo as mo
    import requests
    return github, mo, requests


@app.cell
def _(mo):
    mo.md(
        """
        Welcome to 

        # Derpware.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        We make 

        ## Game.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ### Game Model 

        is the underlying data structure and logic representing the game's state and rules. It's the abstraction developers use to define how the game operates, like a chess game's board state and move rules.
        """
    )
    return


@app.cell
def _(github):
    gh = github.Github()
    return (gh,)


@app.cell
def _(mo):
    mo.md(
        """
        # Game Resource Model 

        Game Resource Model focuses on managing in-game resources, such as health, mana, currency, or ammunition. This model details how resources are acquired, used, and depleted, crucial for gameplay balance and progression.
        """
    )
    return


@app.cell
def _():
    return


@app.cell
def _(gh):
    gh.rate_limiting_resettime
    return


@app.cell
def _(gh):
    gh.get_emojis()
    return


if __name__ == "__main__":
    app.run()
