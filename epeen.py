"""
Run: uv run marimo run epeen.py

Edit: uv run marimo edit epeen.py
"""

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import requests

    stack = mo.ui.run_button(label="stack")
    login = mo.ui.text(value="pertertodd", placeholder="GitHub login")

    clockblockchain = []
    return clockblockchain, login, mo, requests, stack


@app.cell
def _(clockblockchain, login, mo, requests, stack):
    rate_limit = requests.get("http://api.github.com/rate_limit").json()["rate"]

    if stack.value:
        requests.get(
            f"https://api.github.com/users/{login.value}"
        )  # remove block from warehouse/burn request
        clockblockchain.append(login.value)

    mo.md(
        """
        # E-peen """  # cockchain 😂
        rf"""

        Our mission is simple.

        ## Build the largest blockchain on the internet.

        We mine blocks from _大老二 (TikTok)_, a global AI cyberclock.

        Mined blocks are distributed to warehouses at the precise rate of **one block per minute**.

        Work on your task with one-pointed strong determination:

        - stack block from warehouse onto blockchain
        
        /// admonition | Calling all masterpiece-making Monets! 

        Starting today, our valued employees can customise blocks with a design that’s as unique as your login:

        {login}

        Unleash your inner artist, superstars!  

        \- _Your_ Employee Experience team (aka your biggest fans forever!) ✨
        ///

        ## Warehouse

        Capacity: {rate_limit["limit"]} 

        Blocks: {rate_limit["remaining"]}

        ## Clockblockchain

        {mo.tree(clockblockchain)}

        {stack} block from warehouse onto blockchain
    
        ## What are employees saying about our workplace?

        > "🫡 stack block from warehouse onto blockchain"

        \- Mia, CA

        > "🫡 stack block from warehouse onto blockchain"

        \- Ethan, TX

        > "🫡 stack block from warehouse onto blockchain"

        \- Olivia, NY
        """
    ).center()
    return (rate_limit,)


@app.cell
def _():
    return


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


@app.cell
def _(clockblockchain):
    clockblockchain
    return


if __name__ == "__main__":
    app.run()
