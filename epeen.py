"""
Run: uv run marimo run epeen.py

Edit: uv run marimo edit epeen.py
"""

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
        # E-peen """  # cockchain 😂
        r"""

        You mission is simple: 
    
        ## Build the largest blockchain on the internet.

        We mine blocks from a secret AI cyberclock. 
    
        We'll deliver new blocks to your warehouse at the rate of **one block per minute**.
    
        mined from an ancient AI cyber timechain cybermine
        We 
        we snip fresh blocks
        we cut fresh blocks

        the interweb blockchain

        The objective is simple
        laser focused goal
        one objective
        a single

        deliver one block per minute

        Block Warehouse

        We store blocks
        (in warehouses).

        1. Get ya block out!
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from github import Github

    gh = Github()
    refresh = mo.ui.refresh(label="Refresh", options=["1s", "5s", "10s", "30s"])
    consume = mo.ui.run_button(kind="danger", label="Consume")
    resource_units = mo.ui.number(value=1)

    mo.md(
        f"""
        {refresh} resource status

        {consume} {resource_units} resource units
        """
    )
    return Github, consume, gh, mo, refresh, resource_units


@app.cell
def _(gh, mo, refresh):
    import json
    from datetime import datetime, timezone

    if refresh.value:
        sent = datetime.now(tz=timezone.utc)
        rate_limit = gh.get_rate_limit()
        received = datetime.utcnow().replace(tzinfo=timezone.utc)

    mo.md(
        f"""
        request sent at

        {sent}

        rate limit status

        limit: {rate_limit.core.limit}

        remaining: {rate_limit.core.remaining}

        used: {rate_limit.core.used}

        reset: {str(rate_limit.core.reset.astimezone().replace(tzinfo=None))}

        time until reset: {rate_limit.core.reset - received}

        response received at

        {received}

        {type(rate_limit)}ack

        {rate_limit.raw_headers}


        """
    ) if refresh.value else None
    return datetime, json, rate_limit, received, sent, timezone


@app.cell
def _(mo, rate_limit, received):
    mo.md(
        f"""
        time until reset: {rate_limit.core.reset - received}
        """
    )
    return


@app.cell
def _(rate_limit):
    rate_limit.raw_headers
    return


@app.cell
def _():
    _
    return


@app.cell
def _(mo, rate_limit):
    mo.ui.dictionary(rate_limit.raw_headers)
    return


@app.cell
def _(mo, rate_limit):
    mo.Html(rate_limit.raw_headers)
    return


@app.cell
def _(rate_limit):
    [f'{k=},{type(v)=} vs {type("blah")=}' for k, v in rate_limit.raw_headers.items()]
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## another idea - treasure hunter!

        mine for things in req ids:

        `"x-github-request-id":"DCEE:1E06D0:F94125:14A6D74:67BCFEC0"`

        it's a hex id

        maybe you could search for...

        letters, words numbers etc

        use as seed to guess numbers, cards, suits, red/black

        "DCE9:718E9:151D541:1BEE077:67BCFE8E"
        """
    )
    return


if __name__ == "__main__":
    app.run()
