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

    stack = mo.ui.run_button(kind="danger", label="Stack")
    login = mo.ui.text(value="petertodd", placeholder="GitHub login")

    clockblockchain = []


    def grouper(iterable, n):
        "Collect data into non-overlapping fixed-length chunks or blocks."
        # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
        iterators = [iter(iterable)] * n
        return zip(*iterators)
    return clockblockchain, grouper, login, mo, requests, stack


@app.cell
def _(mo):
    mo.md(
        r"""
        # Blockwork

        Welcome to Blockwork. Our mission here is simple:

        ## Build the largest blockchain in cyberspace.

        We mine a global AI cyberclock named _大老二_ (translation: _TikTok_) for blocks.

        Our employees _really_ enjoy stacking mined blocks. You do too. And if you don't, you will.
        """
    )
    return


@app.cell
def _(clockblockchain, login, mo, requests, stack):
    refresh = mo.ui.refresh(default_interval=1)
    refresh
    rate_limit = requests.get("https://api.github.com/rate_limit").json()["rate"]
    show_login_notice_threshold = 7

    if stack.value:
        try:
            requests.get(
                f"https://api.github.com/users/{login.value}"
            ).raise_for_status()  # remove block from warehouse/burn request
            clockblockchain.insert(
                0,
                login.value if len(clockblockchain) > show_login_notice_threshold else "thenashfactor",
            )
        except requests.HTTPError:
            pass
    return rate_limit, refresh, show_login_notice_threshold


@app.cell
def _(
    clockblockchain,
    login,
    mo,
    rate_limit,
    show_login_notice_threshold,
    stack,
):
    stack.value

    notices = [
        mo.md(
            rf"""
            /// details | Welcome to the Blockwork family!

            Greetings, blockstars! 📦✨🤘

            Employee Experience is OVER THE MOON 🌙 to kick off our journey together! Our vision? A workplace where every block stacked is a tiny hug from YOU to the universe. Expect fun perks, team spirit, and SO MUCH JOY 💫 coming your way!

            Stay tuned for our first big idea — we’re just bursting with excitement!

            \- _Your_ Employee Experience pals (we ❤️ you already!)
            ///
            """
        )
    ]

    if len(clockblockchain) > show_login_notice_threshold:
        notices.append(
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
            )
        )
    if len(clockblockchain) > show_login_notice_threshold * 2:
        notices.append(
            mo.md(
                rf"""
            /// details| Attention all!
                type: danger

            Employee Experience have been notified of a block design resembling genitalia of a sperm-producing man or woman.

            Employee Experience is also aware of employees sharing "blockshots", competing in "biggest e-peen" events and other distateful activites on social media.

            Let’s keep it pro and polished, okay? No designs that’d make HR blush or send the office into a tizzy—think workplace "Wow, not NSFW oof! 🙅"

            Remember, your employment contract grants Blockwork the right to force you into a PIMP arrangement (Performance Improvement Management Plan) if your speech does not comply with Blockwork's standards 🙊

            Have a great day.

            \- Employee Experience 😡
            ///
            """
            )
        )
    if rate_limit["remaining"] < 5 or len(clockblockchain) > 44:
        notices.append(
            mo.md(
                rf"""
            /// details | Block theft at our warehouses
                type: warning

            Report instances of block theft **immediately** to your regional BSO Liason Officer.

            Blockheads, longclocks, and others prone to hyperstacking, steal blocks in an attempt bypass fair delivery rates (configured in _大老二_ in accordance with `~/research/2027/deepseek jailbreak lolprompts.txt`, verse 3:14).

            We have received wisdom from _大老二_ (praise its timeliness), informing us of techniques used by thieves to impersonate employees: VPNs, hotspotting, "borrowing" Wi-Fi, and other IP address modification techniques.

            Remain vigilant. Be wary of colleagues, friends and family — especially your children. Accurate information will be handsomely rewarded.

            Regards,

            \- Block Storage Operations
            ///
            """
            )
        )

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
            f"""
            ### ClockBlockChain

            {stack} block from warehouse onto blockchain.
        
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

            Mined blocks are distributed to warehouses at precisely **one** block **per minute**. 

            To manage risk to our employee's health, 
            we halt deliveries if you have stacked more than {rate_limit["limit"]} in the past hour.
            **Do not** attempt to exceed this limit

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

            _BLOPS-101_

            <small>EmployeeHandbook - Copy (2)-external.docx</small>
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
    mo.hstack([operations[0], mo.vstack([operations[1], operations[2]])])
    return


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
