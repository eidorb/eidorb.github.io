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
