import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.function
def exercise(text, results, svol_img_path, switch):    
    txt = mo.md(rf"""{text}

    {results}
    """)

    style_css = {"filter": "blur(7px)"} if switch.value == False else {}

    im = mo.image(svol_img_path, style=style_css)
    im_none = None if switch.value == False else im

    dim = [2, 3]
    txt_stack = mo.vstack([txt, switch], justify="center", align="center", gap=2)

    ##########################  USAGE  ##########################
    # switch1 = mo.ui.switch(label="Mostra procedimento") [***IN UN'ALTRA CELLA***]
    # text = "$$ 1)\quad x^2 + 5x -3 = 0 $$"
    # res = "$$ [x_1 = 4 \quad\lor\quad x_2 = 3] $$"
    # svol_img = "C:\\Users\\enric\\Desktop\\marimo_notebooks\\cacca.png"
    # exercise(text=text, res=res, svol_img=svol_img, switch=switch1)

    return mo.hstack([txt_stack, im], widths=dim, align="center")


@app.cell
def _():
    switch1 = mo.ui.switch(label="Mostra procedimento")
    switch2 = mo.ui.switch(label="Mostra procedimento")
    return switch1, switch2


@app.cell
def _(switch1):
    text = "$$ 1)\quad x^2 + 5x -3 = 0 $$"
    res = "$$ [x_1 = 4 \quad\lor\quad x_2 = 3] $$"
    svol_img = "C:\\Users\\enric\\Desktop\\marimo_notebooks\\cacca.png"

    exercise(text=text, results=res, svol_img_path=svol_img, switch=switch1)

    return (svol_img,)


@app.cell
def _(svol_img, switch2):
    text2 = "$$ 2)\quad x^{2222} + 5x -3 = 0 $$"
    res2 = "$$ [x_{1222} = 4 \quad\lor\quad x_2 = 3] $$"

    exercise(text=text2, results=res2, svol_img_path=svol_img, switch=switch2)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
