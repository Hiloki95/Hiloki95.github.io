

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""**ciao** proviamo a fare un grafico stupidissimo""")
    return


@app.cell
def _(mo):
    slider_x2 = mo.ui.slider(-5, 5, label=f"Coefficiente x^2: ")
    slider_x = mo.ui.slider(-5, 5, label=f"Coefficiente x: ")
    slider_b = mo.ui.slider(-5, 5, label=f"Termine noto: ")
    return slider_b, slider_x, slider_x2


@app.cell
def _(slider_b, slider_x, slider_x2):
    slider_x2, slider_x, slider_b
    return


@app.cell
def _(mo, slider_b, slider_x, slider_x2):
    a = slider_x2.value
    b = slider_x.value
    c = slider_b.value
    mo.md(rf"""L'equazione mostrata nel grafico è la seguente:  
    {a}x<sup>2</sup> + {b}x + {c}""")
    return a, b, c


@app.cell
def _(a, b, c, np, plt):
    # x = range(-1, 1, 100)
    x = np.linspace(-10, 10, 1000)
    y = [a*x**2 + b*x + c for x in x]
    if a >= 0:
        lim_inf, lim_sup = -1*max(y), max(y)
    else:
        lim_inf, lim_sup = min(y), -1*min(y)
    asse_x  = np.zeros(len(x))
    asse_y  = np.zeros(len(x))
    asse_y2 = np.linspace(lim_inf, lim_sup, len(x))
    g = plt.plot(x,y)
    g = plt.plot(asse_y, asse_y2, 'k')
    g = plt.plot(x, asse_x, 'k')
    return (g,)


@app.cell
def _(g):
    g
    return


@app.cell
def _(mo, plt):
    plt.plot([1,2,3],[4,5,6])
    mo.mpl.interactive(plt.gcf())
    return


@app.cell
def _(mo):
    mo.Html('<div><a href="../index.html">Torna indietro</a></div>')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
