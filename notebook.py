import marimo

__generated_with = "0.11.8"
app = marimo.App(app_title="", css_file="")


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
    # brute search look for interesting identicons... - https://github.com/kashav/identicon
    avatar_url = "https://github.com/identicons/msqui.png"
    # no user has no repos
    repos = []

    # try to look up avatar and repos from user login
    try:
        with mo.status.spinner():
            response = requests.get(f"https://api.github.com/users/{login.value}")
            response.raise_for_status()
            user = response.json()
            repos = requests.get(user["repos_url"]).json()
            avatar_url = user["avatar_url"]
    except requests.HTTPError:
        # 404 user not found :(
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
    mo.md(r"""<small>Hack on your own copy of this notebook [here](https://marimo.app/https://eidorb.github.io/notebook.py).</small>""")
    return


@app.cell
def _(mo):
    # hmm perhaps lil switch, towards bottow of page, with lab icon (beaker thing)
    switch = mo.ui.switch(label="do not disturb")

    # actually, nah...
    # it's a toggle button
    # https://docs.marimo.io/recipes/?h=toggle#create-a-toggle-button

    mo.hstack([switch, mo.md(f"Has value: {switch.value}")])
    mo.ui.tabs(
        {
            " ": "bar",
            "💻 LAB hehe!": mo.ui.text(placeholder="Key"),
        }
    )
    return (switch,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
