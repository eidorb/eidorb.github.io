"""
Run: uv run marimo run epeen.py

Edit: uv run marimo edit epeen.py
"""

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    stack = mo.ui.run_button(label="stack")
    login = mo.ui.text(value="pertertodd", placeholder="GitHub login")

    mo.md(
        """
        # E-peen """  # cockchain 😂
        rf"""

        Our mission is simple.

        ## Build the largest blockchain on the internet.

        We mine blocks from _大老二 (TikTok)_, a global AI cyberclock.

        Mined blocks are distributed to warehouses at the precise rate of **one block per minute**.

        Work on your task with strong determination:

        - {stack} block from warehouse onto blockchain

        /// admonition | Calling all masterpiece-making Monets! 

        Starting today, our valued employees can customise blocks with a design that’s as unique as your login:
    
        {login}

        Unleash your inner artist, superstars!  

        \- _Your_ Employee Experience team (aka your biggest fans forever!) ✨
        ///

        #### What are employees saying about our workplace?

        > "🫡 stack block from warehouse onto blockchain"

        \- Mia, CA

        > "🫡 stack block from warehouse onto blockchain"

        \- Ethan, TX

        > "🫡 stack block from warehouse onto blockchain"

        \- Olivia, NY
        """
    )
    return login, mo, stack


@app.cell
def _(mo):
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
    return Github, consume, gh, refresh, resource_units


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
def _(mo):
    mo.md(
        """
        admonition ---


        it has come to our attention

        blah blah bla



        No designs that’d make HR blush or send the office into a tizzy—think workplace wow, not NSFW oof!
        """
    )
    return


if __name__ == "__main__":
    app.run()
