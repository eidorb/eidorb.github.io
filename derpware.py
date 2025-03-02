import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="Derpware")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        We are 

        # Derpware.

        We make 

        ## Game.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        Game has a

        ## Game Model.

        It's the underlying data structure and logic representing the Game's state and rules. It's the abstraction developers use to define how Game operates, like a chess game's board state and move rules.
        """
    )
    return


@app.cell
def _():
    import github  # game model based on PyGithub


    class Game(github.Github):
        def __init__(self):
            # raise exceptions instead of retry
            super().__init__(retry=None)

        def consume_core(self) -> None:
            """Consumes 1 core resource.

            Raises RateLimitExceededException if core limit reached.
            """
            # request to /get_hooks returns 404, but counts towards rate limit
            try:
                self.get_hooks()
            except github.UnknownObjectException as e:
                return e

        def consume_search(self) -> None:
            """Consumes 1 search resource.

            Raises RateLimitExceededException if search limit reached.
            """
            # search request without query returns 422 validation error, but counts towards rate limit
            try:
                self.requester.requestJsonAndCheck("GET", "/search/users")
            except github.GithubException as e:
                if e._GithubException__status != 422:
                    raise
                return e

        def consume_integration_manifest(self) -> None:
            """Consumes 1 integration_manifest resource.

            Raises RateLimitExceededException if core limit reached.
            """
            # request with bullshit code returns 404, but counts towards rate limit
            try:
                self.requester.requestJsonAndCheck(
                    "POST", "/app-manifests/{code}/conversions"
                )
            except github.UnknownObjectException as e:
                return e
    return Game, github


@app.cell
def _(mo, rate_limit):
    mo.md(
        f"""
        Game has

        ## Resource Models.

        A resource model manages in-game resources, such as health, mana, currency, or ammunition. It details how resources are acquired, used, and depleted, crucial for gameplay balance and progression.

        Game's resource models _are_ [GitHub's REST API rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28).
    
        Calling the rate limit endpoint gives current rate limit status:

        /// details | `GET /rate_limit`

        {
            mo.hstack(
                [
                    mo.md(f"Response: {mo.tree(rate_limit.raw_data)}"),
                    mo.md(f"Headers: {mo.tree(rate_limit.raw_headers)}"),
                ]
            )
        }
        ///
        """
    )
    return


@app.cell
def _(Game, mo):
    game = Game()

    consume_search = mo.ui.run_button(kind="danger", label="Consume")
    consume_core = mo.ui.run_button(kind="danger", label="Consume")
    consume_integration_manifest = mo.ui.run_button(kind="danger", label="Consume")
    return consume_core, consume_integration_manifest, consume_search, game


@app.cell
def _(consume_core, consume_integration_manifest, consume_search, game):
    # handle button clicks
    if consume_search.value:
        assert game.consume_search()
    if consume_core.value:
        assert game.consume_core()
    if consume_integration_manifest.value:
        assert game.consume_integration_manifest()

    rate_limit = game.get_rate_limit()
    return (rate_limit,)


@app.cell
def _(mo, rate_limit):
    import itertools

    import plotly.graph_objects as go

    resources = {
        resource_name: getattr(rate_limit, resource_name)
        for resource_name in rate_limit.raw_data
        # forget about graphql for now
        if rate_limit.raw_data[resource_name]["limit"]
    }

    fig = go.Figure()
    count = itertools.count()
    for resource, rate in resources.items():
        fig.add_indicator(
            mode="gauge+number",
            gauge={
                "shape": "bullet",
                "axis": {"range": [None, rate.limit]},
            },
            value=rate.remaining,
            # domain={"x": [0.2, 0.9], "y": [next(count) * 0.1, next(count) * 0.1 - 0.02]},
            domain={
                "x": [0.2, 0.9],
                "y": [
                    next(count) / 5,
                    next(count) / 5,
                ],
            },
            title={"text": resource},
        )

    round_gauge_fig = go.Figure(layout={"grid": {"rows": 1, "columns": len(resources)}})
    count = itertools.count()
    for resource, rate in resources.items():
        round_gauge_fig.add_indicator(
            mode="gauge+number",
            gauge={
                # "shape": "bullet",
                "axis": {"range": [None, rate.limit]},
            },
            value=rate.remaining,
            # domain={"x": [0.2, 0.9], "y": [next(count) * 0.1, next(count) * 0.1 - 0.02]},
            domain={"row": 0, "column": next(count), "x": [0.1, 0.9], "y": [0, 1]},
            title={"text": resource},
        )

        # {mo.ui.plotly(fig)}

        # {mo.ui.plotly(round_gauge_fig)}
    mo.md(
        f"""
        Game has two resources. 

        Consumption of resources is governed by a rate limit model.

        Each Game client IP address is limited to the amount of each resource it can consume per hour.

        Game has {len(resources)} (unlimited!)

        ## Resources:

        Game Resource Model.
        Game manages the rate of resource consumption using

        Game's resource models are implemented using GitHub's REST API rate limits.

        Game manages allocation and consumption of resources.
        """
    )
    return (
        count,
        fig,
        go,
        itertools,
        rate,
        resource,
        resources,
        round_gauge_fig,
    )


@app.cell
def _(consume_core, go, mo, rate_limit):
    def make_usage(rate):
        """Returns usage Figure for rate."""
        return go.Figure(
            go.Indicator(
                mode="number+gauge",
                gauge={
                    "shape": "bullet",
                    "axis": {"visible": False, "range": [0, rate.limit]},
                },
                value=rate.used,
                number={"suffix": f"/{rate.limit}"},
                title="Used",
            ),
            # layout={
            #     "width": 250,
            #     "height": 210,
            # },
        )


    mo.md(
        f"""
        `core` {consume_core}

        {mo.as_html(make_usage(rate_limit.core))}
        """
    )
    return (make_usage,)


@app.cell
def _(consume_search, game, make_usage, mo, rate_limit):
    if consume_search.value:
        assert game.consume_integration_manifest()

    mo.md(
        f"""
        `search` {consume_search}
    
        {mo.as_html(make_usage(rate_limit.search))}
        """
    )
    return


@app.cell
def _(consume_integration_manifest, make_usage, mo, rate_limit):
    mo.md(
        f"""
        `integration_manifest` {consume_integration_manifest}

        {mo.as_html(make_usage(rate_limit.integration_manifest))}
        """
    )
    return


@app.cell
def _(consume_core, go, mo, rate_limit):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.ui.plotly(
                        go.Figure(
                            go.Indicator(
                                mode="gauge+number",
                                gauge={
                                    "axis": {"range": [0, rate_limit.core.limit]},
                                },
                                value=rate_limit.core.used,
                                number={"suffix": "/hour"},
                                title="core",
                            ),
                            # layout={"width": 250, "height": 250},
                        )
                    ),
                    mo.md(f"{consume_core}"),
                ]
            ),
            mo.ui.plotly(
                go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        gauge={
                            "axis": {
                                "range": [
                                    None,
                                    rate_limit.integration_manifest.limit,
                                ]
                            },
                        },
                        value=rate_limit.integration_manifest.used,
                        number={"suffix": "/hour"},
                        title="integration_manifest",
                    ),
                    layout={"width": 250, "height": 250},
                )
            ),
            mo.ui.plotly(
                go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        gauge={
                            "axis": {"range": [None, rate_limit.search.limit]},
                        },
                        value=rate_limit.search.used,
                        number={"suffix": "/hour"},
                        title="search",
                    ),
                    layout={"width": 250, "height": 250},
                )
            ),
        ],
    )
    return


if __name__ == "__main__":
    app.run()
