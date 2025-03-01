import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="Derpware")


@app.cell
def _():
    import github  # just use PyGithub, it's easy, modify later if required
    import marimo as mo
    return github, mo


@app.cell
def _(mo):
    mo.md(
        """
        Welcome to 

        # Derpware.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        We make 

        ## Game.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ### Game Model 

        is the underlying data structure and logic representing the Game's state and rules. It's the abstraction developers use to define how Game operates, like a chess game's board state and move rules.
        """
    )
    return


@app.cell
def _(github):
    gh = github.Github()
    return (gh,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Game Resource Model 

        focuses on managing in-game resources, such as health, mana, currency, or ammunition. This model details how resources are acquired, used, and depleted, crucial for gameplay balance and progression.
        """
    )
    return


@app.cell
def _(gh, mo):
    rate_limit = gh.get_rate_limit()
    rate_limit

    mo.md(
        f"""
        GitHub's API provides a
    
        ## `/rate_limit` endpoint.

        Querying it gives resources statistics.

        {
            mo.hstack(
                [
                    mo.md(
                        f'''
                        Raw data:
                        {mo.tree(rate_limit.raw_data)}
                '''
                    ),
                    mo.md(
                        f'''
                        Raw response headers:
                        {mo.tree(rate_limit.raw_headers)}
                '''
                    ),
                ]
            )
        }

        """
    )
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
def _(go, mo, rate_limit):
    mo.hstack(
        [
            mo.ui.plotly(
                go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        gauge={
                            "axis": {"range": [None, rate_limit.core.limit]},
                        },
                        value=rate_limit.core.used,
                        number={"suffix": "/hour"},
                        title="core",
                    ),
                    layout={"width": 250, "height": 250},
                )
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
        # justify="start",
    )
    return


if __name__ == "__main__":
    app.run()
