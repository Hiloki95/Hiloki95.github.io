import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests
    return mo, requests


@app.cell
def _(mo):
    mo.md(
        r"""
    # Indice
    - [Scomposizione di polinomi](#scomposizione-di-polinomi)
    - [Equazioni di primo e secondo grado](#equazioni-di-primo-e-secondo-grado)
        * [Equazioni di primo grado](#equazioni-di-primo-grado)
        * [Equazioni di secondo grado](#equazioni-di-secondo-grado)
        * [Equazioni parametriche](#equazioni-parametriche)
    - [Equazioni riconducibili al secondo grado](#equazioni-riconducibili-al-secondo-grado)
        * [Equazioni binomie](#equazioni-binomie)
        * [Equazioni trinomie](#equazioni-trinomie)
        * [Equazioni scomponibili](#equazioni-scomponibili)
    ---
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Scomposizione di polinomi""")
    return


@app.cell
def _(exercise, response0, switch0):
    # ESERCIZIO 1 --> INDICE 0
    exercise(text=r'$1)$ Scomponi: $\quad x^3 + 3x^2 + x + 3$', results='$R: (x+3)\:(x^2+1)$', svol_img_path=response0, switch=switch0)
    return


@app.cell
def _(exercise, switch1, url1):
    # ESERCIZIO 2 --> INDICE 1
    exercise(text=r'$2)$ Scomponi: $\quad -x^2 + 4x - 4$', results='$R: -(x-2)^2$', svol_img_path=url1, switch=switch1)
    return


@app.cell
def _(exercise, switch2, url2):
    # ESERCIZIO 3 --> INDICE 2
    exercise(text=r'$3)$ Calcolare il valore di:  $\:\frac{127^2 - 73^2}{2}\:$', results='$R: 5400$', svol_img_path=url2, switch=switch2)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Equazioni di primo e secondo grado
    ### Equazioni di primo grado
    """
    )
    return


@app.cell
def _(exercise, switch3, url3):
    # ESERCIZIO 4 --> INDICE 3
    exercise(text=r"$4)$ Risolvere l'equazione: $2(3x - 3) + 1 = 0$", results=r'$R: x = \frac{5}{6}$', svol_img_path=url3, switch=switch3)
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _(mo):
    mo.md(r"""### Equazioni di secondo grado""")
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _(mo):
    mo.md(r"""### Equazioni parametriche""")
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Equazioni riconducibili al secondo grado
    ### Equazioni binomie
    """
    )
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _(mo):
    mo.md(r"""### Equazioni trinomie""")
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _(mo):
    mo.md(r"""### Equazioni scomponibili""")
    return


@app.cell
def _(exercise, switch1):
    exercise(text='ciao', results='caaa', svol_img_path='cccc', switch=switch1)
    return


@app.cell
def _():
    url0 = "https://raw.githubusercontent.com/Hiloki95/Hiloki95.github.io/main/assets_imgs/exercises/es1/es1-1-2/1.png"
    url1 = "https://raw.githubusercontent.com/Hiloki95/Hiloki95.github.io/main/assets_imgs/exercises/es1/es1-1-2/2.png"
    url2 = "https://raw.githubusercontent.com/Hiloki95/Hiloki95.github.io/main/assets_imgs/exercises/es1/es1-1-2/3.png"
    url3 = "https://raw.githubusercontent.com/Hiloki95/Hiloki95.github.io/main/assets_imgs/exercises/es1/es1-1-2/4.png"
    return url0, url1, url2, url3


@app.cell
def _(requests, url0, url1, url2, url3):
    response0 = requests.get(url0).content
    response1 = requests.get(url1).content
    response2 = requests.get(url2).content
    response3 = requests.get(url3).content
    return (response0,)


@app.cell
def _(mo):
    # Ci vuole l'elenco di tutti gli switch necessari

    switch0 = mo.ui.switch(label='Mostra procedimento')
    switch1 = mo.ui.switch(label='Mostra procedimento')
    switch2 = mo.ui.switch(label='Mostra procedimento')
    switch3 = mo.ui.switch(label='Mostra procedimento')
    switch4 = mo.ui.switch(label='Mostra procedimento')
    switch5 = mo.ui.switch(label='Mostra procedimento')
    switch6 = mo.ui.switch(label='Mostra procedimento')
    switch7 = mo.ui.switch(label='Mostra procedimento')
    switch8 = mo.ui.switch(label='Mostra procedimento')
    switch9 = mo.ui.switch(label='Mostra procedimento')
    switch10 = mo.ui.switch(label='Mostra procedimento')
    switch11 = mo.ui.switch(label='Mostra procedimento')
    switch12 = mo.ui.switch(label='Mostra procedimento')
    switch13 = mo.ui.switch(label='Mostra procedimento')
    switch14 = mo.ui.switch(label='Mostra procedimento')
    switch15 = mo.ui.switch(label='Mostra procedimento')
    switch16 = mo.ui.switch(label='Mostra procedimento')
    switch17 = mo.ui.switch(label='Mostra procedimento')
    switch18 = mo.ui.switch(label='Mostra procedimento')
    switch19 = mo.ui.switch(label='Mostra procedimento')
    switch20 = mo.ui.switch(label='Mostra procedimento')
    switch21 = mo.ui.switch(label='Mostra procedimento')
    switch22 = mo.ui.switch(label='Mostra procedimento')
    switch23 = mo.ui.switch(label='Mostra procedimento')
    switch24 = mo.ui.switch(label='Mostra procedimento')
    switch25 = mo.ui.switch(label='Mostra procedimento')
    switch26 = mo.ui.switch(label='Mostra procedimento')
    switch27 = mo.ui.switch(label='Mostra procedimento')
    switch28 = mo.ui.switch(label='Mostra procedimento')
    switch29 = mo.ui.switch(label='Mostra procedimento')
    switch30 = mo.ui.switch(label='Mostra procedimento')
    switch31 = mo.ui.switch(label='Mostra procedimento')
    switch32 = mo.ui.switch(label='Mostra procedimento')
    switch33 = mo.ui.switch(label='Mostra procedimento')
    switch34 = mo.ui.switch(label='Mostra procedimento')
    switch35 = mo.ui.switch(label='Mostra procedimento')
    switch36 = mo.ui.switch(label='Mostra procedimento')
    switch37 = mo.ui.switch(label='Mostra procedimento')
    switch38 = mo.ui.switch(label='Mostra procedimento')
    switch39 = mo.ui.switch(label='Mostra procedimento')
    switch40 = mo.ui.switch(label='Mostra procedimento')
    switch41 = mo.ui.switch(label='Mostra procedimento')
    switch42 = mo.ui.switch(label='Mostra procedimento')
    switch43 = mo.ui.switch(label='Mostra procedimento')
    switch44 = mo.ui.switch(label='Mostra procedimento')
    switch45 = mo.ui.switch(label='Mostra procedimento')
    switch46 = mo.ui.switch(label='Mostra procedimento')
    switch47 = mo.ui.switch(label='Mostra procedimento')
    switch48 = mo.ui.switch(label='Mostra procedimento')
    switch49 = mo.ui.switch(label='Mostra procedimento')
    switch50 = mo.ui.switch(label='Mostra procedimento')
    switch51 = mo.ui.switch(label='Mostra procedimento')
    switch52 = mo.ui.switch(label='Mostra procedimento')
    switch53 = mo.ui.switch(label='Mostra procedimento')
    switch54 = mo.ui.switch(label='Mostra procedimento')
    switch55 = mo.ui.switch(label='Mostra procedimento')
    switch56 = mo.ui.switch(label='Mostra procedimento')
    switch57 = mo.ui.switch(label='Mostra procedimento')
    switch58 = mo.ui.switch(label='Mostra procedimento')
    switch59 = mo.ui.switch(label='Mostra procedimento')
    switch60 = mo.ui.switch(label='Mostra procedimento')
    switch61 = mo.ui.switch(label='Mostra procedimento')
    switch62 = mo.ui.switch(label='Mostra procedimento')
    switch63 = mo.ui.switch(label='Mostra procedimento')
    switch64 = mo.ui.switch(label='Mostra procedimento')
    switch65 = mo.ui.switch(label='Mostra procedimento')
    switch66 = mo.ui.switch(label='Mostra procedimento')
    switch67 = mo.ui.switch(label='Mostra procedimento')
    switch68 = mo.ui.switch(label='Mostra procedimento')
    switch69 = mo.ui.switch(label='Mostra procedimento')
    switch70 = mo.ui.switch(label='Mostra procedimento')
    switch71 = mo.ui.switch(label='Mostra procedimento')
    switch72 = mo.ui.switch(label='Mostra procedimento')
    switch73 = mo.ui.switch(label='Mostra procedimento')
    switch74 = mo.ui.switch(label='Mostra procedimento')
    switch75 = mo.ui.switch(label='Mostra procedimento')
    switch76 = mo.ui.switch(label='Mostra procedimento')
    switch77 = mo.ui.switch(label='Mostra procedimento')
    switch78 = mo.ui.switch(label='Mostra procedimento')
    switch79 = mo.ui.switch(label='Mostra procedimento')
    switch80 = mo.ui.switch(label='Mostra procedimento')
    switch81 = mo.ui.switch(label='Mostra procedimento')
    switch82 = mo.ui.switch(label='Mostra procedimento')
    switch83 = mo.ui.switch(label='Mostra procedimento')
    switch84 = mo.ui.switch(label='Mostra procedimento')
    switch85 = mo.ui.switch(label='Mostra procedimento')
    switch86 = mo.ui.switch(label='Mostra procedimento')
    switch87 = mo.ui.switch(label='Mostra procedimento')
    switch88 = mo.ui.switch(label='Mostra procedimento')
    switch89 = mo.ui.switch(label='Mostra procedimento')
    switch90 = mo.ui.switch(label='Mostra procedimento')
    switch91 = mo.ui.switch(label='Mostra procedimento')
    switch92 = mo.ui.switch(label='Mostra procedimento')
    switch93 = mo.ui.switch(label='Mostra procedimento')
    switch94 = mo.ui.switch(label='Mostra procedimento')
    switch95 = mo.ui.switch(label='Mostra procedimento')
    switch96 = mo.ui.switch(label='Mostra procedimento')
    switch97 = mo.ui.switch(label='Mostra procedimento')
    switch98 = mo.ui.switch(label='Mostra procedimento')
    switch99 = mo.ui.switch(label='Mostra procedimento')
    switch100 = mo.ui.switch(label='Mostra procedimento')
    return switch0, switch1, switch2, switch3


@app.cell
def _():
    # for indice in range(100):
    #     print(f"switch{indice} = mo.ui.switch(label='Mostra procedimento')")
    return


@app.cell
def _(mo):
    def exercise(text, results, svol_img_path, switch):    
        txt = mo.md(rf"""{text}

        {results}
        """)

        style_css = {"filter": "blur(7px)"} if switch.value == False else {}

        im = mo.image(svol_img_path, style=style_css)
        im_none = None if switch.value == False else im

        dim = [2, 3]
        txt_stack = mo.vstack([txt, switch], justify="center", align="center", gap=2)

        return mo.hstack([txt_stack, im], widths=dim, align="center")
    return (exercise,)


if __name__ == "__main__":
    app.run()
