"""
Run: uv run marimo run epeen.py

Edit: uv run marimo edit epeen.py

Export: uv run marimo export html-wasm blockwork.py -o blockwork.html
"""

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="Blockwork")


@app.cell
def _():
    import marimo as mo
    import requests

    stack = mo.ui.run_button(label="stack")
    login = mo.ui.text(value="petertodd", placeholder="GitHub login")

    clockblockchain = []
    return clockblockchain, login, mo, requests, stack


@app.cell
def _(mo):
    mo.md(
        r"""
        # Blockwork

        Welcome to Blockwork. Our mission here is simple:

        ## Build the largest blockchain in cyberspace.

        We mine blocks from _大老二_ (_TikTok_), a global AI cyberclock.

        Mined blocks are distributed to warehouses at precisely **one** block **per minute**.
        """
    )
    return


@app.cell
def _(login, mo):
    notices = [
        mo.md(
            rf"""
            /// admonition | Calling all masterpiece-making Monets! 

            Starting today, our valued employees can customise blocks with a design that’s as unique as your login:

            {login}

            We trust this will spark joy ✨ in your block stacking and satisfy concerns raised in the employee satisfication survey post-survey debrief discussion workshop series (shout out to ESSPSDDWS tiger team (T-Team) 👏).

            Unleash your inner artist, superstars!

            \- _Your_ biggest fans! (aka Employee Experience) 
            ///
            """
        ),
        mo.md(
            rf"""
            /// warning | Block theft at our warehouses

            Please report any instances of block theft to your regional BSO Liason Officer.

            We praise _大老二_, oh chronotastic one, for informing us of techniques used by thieves to steal blocks from employee warehouses:

            - VPNs
            - hotspotting
            - "borrowing" Wi-Fi

            Be wary of your friends and family.

            Regards,

            \- Block Storage Operations
            ///
            """
        ),
        mo.md(
            rf"""
            /// danger | Attention all!

            Employee Experience have been informed of a block design resembling genitalia of a sperm-producing man or woman.

            Block designs NOT suitable for work will NOT be tolerated.

            Additonally, it has come to the attention of Employee Experience that employees are sharing their "blockshots", asking others to "get ya block out!", competing in "biggest e-peen" events and other distateful activites on social media.

            Employee Experience is aware of your activities. You have been warned.

            Have a great day.

            \- Employee Experience 😡
            ///
            """
        ),
    ]

    mo.md(
        r"""
        ## Noticeboard
        """
    )
    return (notices,)


@app.cell
def _(mo, notices):
    mo.hstack(notices)
    return


@app.cell
def _(mo):
    mo.md(r"""## Operations""")
    return


@app.cell
def _(mo, operations):
    mo.hstack(operations)
    return


@app.cell
def _(clockblockchain, login, mo, requests, stack):
    rate_limit = requests.get("http://api.github.com/rate_limit").json()["rate"]

    if stack.value:
        requests.get(
            f"https://api.github.com/users/{login.value}"
        )  # remove block from warehouse/burn request
        clockblockchain.append(login.value)


    def grouper(iterable, n):
        "Collect data into non-overlapping fixed-length chunks or blocks."
        # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
        iterators = [iter(iterable)] * n
        return zip(*iterators)


    operations = [
        mo.md(
            f"""
            ### Employee handbook

            Work on your task list with one-pointed strong determination:

            - stack block from warehouse onto blockchain

            #### Block stacking workflow

            {
                mo.mermaid(
                    '''
                    stateDiagram-v2
                        s : stack block from warehouse onto blockchain
                        [*] --> s
                        s --> s
                    '''
                )
            }

            <small>EmployeeHandbook - Copy (2)-external.docx</small>
            """
        ).callout(),
        mo.md(
            rf"""
            ### ▢ Block Warehouse

            \# TODO: think about refreshing this

            > We store blocks!

            <small>(In warehouses.)</small>

            #### Block storage

            /// attention | Maximum rated capacity

            {rate_limit["limit"]} ▧
            ///

            ```
            {
                "".join(
                    "".join(group)
                    for group in grouper(
                        "▨" * rate_limit["remaining"] + "□" * rate_limit["used"], 6
                    )
                )
            }
            ```
            """
        ).callout(),
        mo.md(
            f"""

            ### $CBC: ClockBlockChain

            {
                mo.tree(
                    [
                        mo.image(f"https://github.com/identicons/{login}.png")
                        for login in clockblockchain
                    ]
                )
            }

            {stack} block from warehouse onto blockchain
            """
        ).callout(),
    ]
    mo.vstack([])
    return grouper, operations, rate_limit


@app.cell
def _(mo):
    mo.md(
        """
        ## What are employees saying about our workplace?

        -   > "🫡 stack block from warehouse onto blockchain"

            \\- Mia, CA

            -   > "🫡 stack block from warehouse onto blockchain"

                \\- Ethan, TX

                -   > "🫡 stack block from warehouse onto blockchain"

                    \\- Olivia, NY
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""<small>Powered by [GIGES](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28), GitHub's internet game engine service.</small>""")
    return


if __name__ == "__main__":
    app.run()
