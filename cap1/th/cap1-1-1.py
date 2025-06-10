import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ##Capitolo 1.1.1 - Operazioni matematiche e loro proprietà
    Mi rifiuto di scrivere 'sto capitolo, sarebbe un insulto all'intelligenza di entrambi. Cià
    """
    )
    return


if __name__ == "__main__":
    app.run()
