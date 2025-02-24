import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Stonk Trader

        - 60 trades/hour
        - stonk market closed if exceeded
        The scarce resource game.

        Stonk market reopens at...
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from github import Github

    gh = Github()
    refresh = mo.ui.refresh(label="Refresh", options=["1s", "5s"], default_interval="5s")
    consume = mo.ui.run_button(kind="danger", label="Consume")
    resource_units = mo.ui.number(value=1)
    return Github, consume, gh, mo, refresh, resource_units


@app.cell
def _(consume, gh, mo, refresh, resource_units):
    import json
    from datetime import datetime, timezone

    limit = gh.get_rate_limit().core

    mo.md(
        f"""
        Stonk market: {'open' if limit.remaining else 'closed'}

        will re open at...

        {refresh} resource status

        {consume} {resource_units} resource units

        rate limit status

        limit: {limit.limit}

        remaining: {limit.remaining}

        used: {limit.used}

        reset: {str(limit.reset.astimezone().replace(tzinfo=None))}

        """
    )
    return datetime, json, limit, timezone


@app.cell
def _(mo):
    mo.md(r"""<small>This runs on GGGE, GitHub's [global game engine]().</small>""")
    return


if __name__ == "__main__":
    app.run()
