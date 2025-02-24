import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # 60

        The scarce resource game.

        60 requests per hour.

        ## Resource model

        lol, hackers have already been here: [Rate limits for /rate_limit REST API endpoint](https://github.blog/changelog/2023-10-18-rate-limits-for-rate_limit-rest-api-endpoint/)

        > the `/rate_limit` endpoint is now covered by rate limits

        Previously it was not covered by limits.

        > it was also a potential vector for abuse

        We'll have to test behaviour for unauthenticated requests.
        It says requests _do not_ count towards the primary limit for _authenticated_ users.

        It's interesting. 

        > Unauthenticated requests are associated with the originating IP address

        GitHub maintains a collection of rate limits, keyed by requestor.

        A requestor can be

        - ip address (unauthenticated requests)
        - credential identity (authenticated requests)

        > The primary rate limit for unauthenticated requests is 60 requests per hour.

        I'm visualising some feel where you're riding perilously close to hitting the rate limit.
        It's like your timeline and the limit's timeline converging? 
        The feeling of constriction.
        How close can you let it shrink.

        As the ... approaches _now_
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from github import Github

    gh = Github()
    get = mo.ui.run_button(kind="success", label="Get")

    mo.md(
        f"""
        {get} rate limit
        """
    )
    return Github, get, gh, mo


@app.cell
def _(get, gh, mo):
    import json
    from datetime import datetime, timezone

    if get.value:
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

        response received at
    
        {received}

        """
    ) if get.value else None
    return datetime, json, rate_limit, received, sent, timezone


@app.cell
def _(rate_limit):
    rate_limit.core.reset
    return


@app.cell
def _(received):
    received
    return


@app.cell
def _(mo, rate_limit, received, sent):
    mo.md(
        f"""
        delta: {received - sent}

        mm:ss.mmmm: {rate_limit.core.reset - received}
    
        {(rate_limit.core.reset - received).seconds} s
        """
    )
    return


@app.cell
def _():
    # poll rate limit endpoint?
    return


@app.cell
def _(rate_limit):
    rate_limit.raw_headers
    return


if __name__ == "__main__":
    app.run()
