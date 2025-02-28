import marimo

__generated_with = "0.11.8"
app = marimo.App(width="full", app_title="", css_file="")


@app.cell
def _():
    """
    Export to WASM-powered HTML:
        uv run marimo export html-wasm notebook.py -o . --mode run

    Serve locally:
        uv run -m http.server --directory .
    """

    import marimo as mo

    with mo.status.spinner("loading snakes on a browser..."):
        # import micropip
        # await micropip.install('requests')
        import requests

    # get and set login name from query param
    # if _no_ login param, then login is eidorb
    # otherwise login is set to login param
    # if login param _present_ but empty,
    # app will be in an "uninitialised" state
    query_params = mo.query_params()
    login = mo.ui.text(
        value="eidorb"
        if query_params["login"] is None  #
        else query_params["login"],
        on_change=lambda value: query_params.set("login", value),
    )
    return login, mo, query_params, requests


@app.cell
def _(avatar_url, login, mo, query_params):
    from urllib.parse import urlencode

    mo.md(
        f"""
        /// details | {
            mo.image(
                avatar_url,
                width=123,
                rounded=True,
                caption=f"{login.value}'s projects" if login.value else None,
            ).center()
        }

        This webpage is interactive!

        Enter your GitHub login: {login}

          /// admonition | Come again

          Changing the login updates this page's URL.
          Use it to come back to the same state:

          {
            mo.ui.text(
                f"{str(mo.notebook_location())}?{urlencode(query_params.to_dict())}",
                full_width=True,
            )
        }
          ///
        ///
        """
    )
    return (urlencode,)


@app.cell
def _(login, mo, requests):
    import itertools

    # fall back to placeholder avatar and empty list of repos
    # if user can't be found
    user = None
    # brute search for interesting identicons... - https://github.com/kashav/identicon
    avatar_url = "https://github.com/identicons/jsime.png"
    repos = []

    # try to look up avatar and repos from user login
    try:
        with mo.status.spinner():
            response = requests.get(f"https://api.github.com/users/{login.value}")
            response.raise_for_status()
            user = response.json()
            repos = requests.get(user["repos_url"]).json()
            # avatar_url = f"https://github.com/identicons/{login.value}.png"
            avatar_url = user["avatar_url"]
    except requests.HTTPError:
        # api error :( fall back to defaults above
        # 404 user not found
        # 403 rate limited
        pass

    # style projects with cycling colours (details types)
    types = itertools.cycle(["info", "warn", "danger", "success"])
    for repo in repos:
        # filter out forks and repos without homepages
        if not repo["fork"] and repo["homepage"] and repo["name"] != "eidorb.github.io":
            mo.output.append(
                mo.md(
                    f"""
                    /// details | [{repo["name"]}]({repo["homepage"]})
                        type: {next(types)}

                    {repo["description"]} [::line-md:github-loop::]({repo["html_url"]}) 
                    ///
                    """
                )
            )
    return avatar_url, itertools, repo, repos, response, types, user


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Games

        >  The game is out there, and it's either play or get played.
        >
        > -- Omar Little

        These games are played by billions of simultaneous players.
        Not all players realise they are playing.

        _You right mate?_

        It's odd for sure, but kinda cool! 

        In-game resources 

        Game state is modelled with the API rate limit model. 

        umanage sing GitHub. 
        in-game player actions correspond
        player actions correspond to API requests,
        in-game resource is modelled with

        >  A man got to have a code.
        >
        > -- Omar Little


        So, if the game is using the API request rate limit model to manage gameplay, that might mean that the game's mechanics are designed such that  and the rate at which these requests can be made affects how the player can interact with the game.

        Game ideas are limited by imagination.

        - [Blockwork](https://eidorb.github.io/blockwork.html)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""<small>Hack on your own copy of this notebook [here](https://marimo.app/https://eidorb.github.io/notebook.py).</small>""")
    return


if __name__ == "__main__":
    app.run()
