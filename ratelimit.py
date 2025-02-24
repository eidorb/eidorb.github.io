import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
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


        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from github import Github

    gh = Github()
    return Github, gh, mo


@app.cell
def _(gh):
    rate_limit = gh.get_rate_limit()
    rate_limit
    return (rate_limit,)


@app.cell
def _(mo):
    mo.md(
        f"""
    
        """
    )
    return


@app.cell
def _(rate_limit):
    rate_limit.raw_headers
    return


if __name__ == "__main__":
    app.run()
