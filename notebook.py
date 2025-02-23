import marimo

__generated_with = "0.11.8"
app = marimo.App(app_title="", css_file="")


@app.cell
def _():
    from itertools import cycle
    from urllib.parse import urlencode
    import marimo as mo
    return cycle, mo, urlencode


@app.cell
def _(mo):
    with mo.status.spinner("loading snakes on a browser..."):
        # import micropip
        # await micropip.install('requests')
        import requests
    return (requests,)


@app.cell
def _(mo):
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
    return login, query_params


@app.cell
def _(avatar_url, login, mo, query_params, urlencode):
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
    return


@app.cell
def _(cycle, login, mo, requests):
    # get avatar or placeholder if user not found :(
    try:
        with mo.status.spinner():
            response = requests.get(f"https://api.github.com/users/{login.value}")
            response.raise_for_status()
            user = response.json()
            repos = requests.get(user["repos_url"]).json()
            avatar_url = user["avatar_url"]
    except requests.HTTPError:
        user = None
        avatar_url = (
            "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
        )

    # filter my repos: not forks; have a homepage link
    if user:
        projects = [
            repo
            for repo in repos
            if not repo["fork"] and repo["homepage"] and repo["name"] != "eidorb.github.io"
        ]
    # no user has no repos
    else:
        projects = []

    # use differnt types of details to style with colour
    for repo, type in zip(projects, cycle(["info", "warn", "danger", "success"])):
        mo.output.append(
            mo.md(
                f"""
                /// details | [{repo["name"]}]({repo["homepage"]})
                    type: {type}

                {repo["description"]} [::line-md:github-loop::]({repo["html_url"]}) 
                ///
                """
            )
        )
    return avatar_url, projects, repo, repos, response, type, user


@app.cell
def _(mo):
    mo.md(r"""<small>Hack on your own copy of this notebook [here](https://marimo.app/https://eidorb.github.io/notebook.py).</small>""")
    return


if __name__ == "__main__":
    app.run()
