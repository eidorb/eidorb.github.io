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
    # login = mo.ui.text(value="petertodd", placeholder="GitHub login")
    login = mo.ui.text(value="thenashfactor", placeholder="GitHub login")

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
            /// details | Block theft at our warehouses
                type: warning

            Report instances of block theft **immediately** to your regional BSO Liason Officer.

            Blockheads, longclocks, and others prone to hyperstacking, steal blocks in an attempt bypass fair delivery rates (configured in _大老二_ in accordance with `~/research/2027/deepseek jailbreak lolprompts.txt`, verse 3:14).

            We have received wisdom from _大老二_ (praise its timeliness), informing us of techniques used by thieves to impersonate employees: VPNs, hotspotting, "borrowing" Wi-Fi, and other IP address modification techniques.

            Remain vigilant. Be wary of colleagues, friends and family -- especially your children. Accurate information will be handsomely rewarded.

            Regards,

            \- Block Storage Operations
            ///
            """
        ),
        mo.md(
            rf"""
            /// details | Calling all masterpiece-making Monets!
                type: info

            Starting today, our valued employees can customise blocks with a design that’s as unique as your login:

            {login}

            We trust this will spark joy ✨ in your block stacking and satisfy concerns raised in the employee satisfication survey post-survey debrief discussion workshop series (shout out to ESSPSDDWS tiger team (T-Team) 👏).

            Unleash your inner artist, superstars!

            \- _Your_ biggest fans! 😍 (aka Employee Experience)
            ///
            """
        ),
        mo.md(
            rf"""
            /// details| Attention all!
                type: danger

            Employee Experience have been notified of a block design resembling genitalia of a sperm-producing man or woman.

            Employee Experience is also aware of employees sharing "blockshots", competing in "biggest e-peen" events and other distateful activites on social media.

            Let’s keep it pro and polished, okay? No designs that’d make HR blush or send the office into a tizzy—think workplace "Wow, not NSFW oof! 🙅"

            Remember Blockwork reserves the right to force you into a PIMP arrangement (Performance Improvement Management Plan) 🤔

            Have a great day.

            \- Employee Experience 😡
            ///
            """
        ),
    ]

    mo.md(
        f"""
        ## Noticeboard

        {mo.vstack(notices)}
        """
    )
    return (notices,)


@app.cell
def _(clockblockchain, grouper, mo, rate_limit, stack):
    operations = [
        mo.md(
            rf"""
            ### ▨ Block warehouse

            > We store blocks!

            <small>(In warehouses.)</small>

            \# TODO: refresh periodically as well as after block stack

            #### Block storage

            /// attention | Maximum rated capacity: {rate_limit["limit"]} ▧

            ///

            {
                mo.tree(
                    list(
                        "".join(group)
                        # give a 6x10 grid
                        for group in grouper(
                            "□" * rate_limit["used"] + "▨" * rate_limit["remaining"], 6
                        )
                    )
                )
            }
            """
        ).callout(),
        mo.md(
            f"""
            ### Employee handbook

            Work on your task list with one-pointed strong determination:

            - {stack} block from warehouse onto blockchain

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

            _BLOPS-101_

            <small>EmployeeHandbook - Copy (2)-external.docx</small>
            """
        ).callout(),
        mo.md(
            f"""
            ### ClockBlockChain

            {
                mo.tree(
                    [
                        mo.image(f"https://github.com/identicons/{login}.png", width="5em")
                        for login in clockblockchain
                    ]
                )
            }
            """
        ).callout(),
    ]

    mo.md(
        f"""
        ## Operations

        """
    )
    return (operations,)


@app.cell
def _(mo, operations):
    mo.hstack(operations)
    return


@app.cell
def _(clockblockchain, login, requests, stack):
    rate_limit = requests.get("http://api.github.com/rate_limit").json()["rate"]

    if stack.value:
        requests.get(
            f"https://api.github.com/users/{login.value}"
        )  # remove block from warehouse/burn request
        clockblockchain.insert(0, login.value)


    def grouper(iterable, n):
        "Collect data into non-overlapping fixed-length chunks or blocks."
        # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
        iterators = [iter(iterable)] * n
        return zip(*iterators)
    return grouper, rate_limit


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
