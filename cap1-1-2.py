import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Indice
        - [Monomi e polinomi](#monomi-e-polinomi)
            * [Monomi](#monomi)
            * [Proprietà dei monomi](#proprieta-dei-monomi)
            * [Polinomi](#polinomi)
            * [Proprietà dei polinomi](#proprieta-dei-polinomi)
        - [Operazioni tra monomi e tra polinomi](#operazioni-tra-monomi-e-tra-polinomi)
            * [Operazioni tra monomi](#operazioni-tra-monomi)
            * [Operazioni tra polinomi](#operazioni-tra-polinomi)
        - [Scomposizione di polinomi](#scomposizione-di-polinomi)
        - [Equazioni di primo e secondo grado](#equazioni-di-primo-e-secondo-grado)
        - [Equazioni riconducibili al secondo grado](#equazioni-riconducibili-al-secondo-grado)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Monomi e polinomi
        ### Monomi
        I monomi sono l'elemento costituente dei polinomi e sono caratterizzati dal prodotto tra una _parte numerica_ e una _parte letterale_. La parte numerica è un numero qualsiasi e viene detto _coefficiente_, mentre la parte letterale è un prodotto di potenze con base letterale ed esponente intero (positivo o nullo).

        Ad esempio, $-4a^2bc^3$ è un monomio: la parte numerica è $-4$ mentre la parte letterale è $a^2bc^3$.

        Altri esempi di monomi: $\quad3x^2$, $\quad\sqrt{2}xy$, $\quad\frac{5}{7}ab^3$ 

        **NB:** la parte letterale di un monomio è costituito da un **prodotto** di potenze di esponente **positivo** o nullo. Pertanto, elementi come $2a+bc$ o $3xy^{-1}$ **non sono dei monomi**.

        ### Proprietà dei monomi
        #### Gradi di un monomio
        Introduciamo le definizioni di grado _complessivo_ di un monomio e di grado di un monomio _rispetto a una lettera_. Il grado di un monomio rispetto a una lettera corrisponde all'esponente che presenta la lettera stessa all'interno del monomio; il grado complessivo di un monomio, invece, è la somma degli esponenti presenti nella sua parte letterale.

        Ad esempio, prendendo in considerazione il monomio $4x^3yz^2$, si può dire che:

        - il monomio è di grado 3 rispetto alla lettera $x$;
        - il monomio è di grado 1 rispetto alla lettera $y$;
        - il monomio è di grado 2 rispetto alla lettera $z$;
        - 6 è il grado complessivo del monomio.

        #### Monomi simili
        Due monomi si dicono _simili_ se, ridotti in forma normale (cioè riconducendo la parte numerica ad un singolo numero e quella letterale ad un prodotto di lettere **non ripetute**), presentano la stessa parte letterale. Ad esempio:

        - $5xy^2$ e $2xy^2$ sono due monomi simili;
        - $ab$ e $ab^2$ **non** sono due monomi simili.

        #### Monomi uguali
        Due monomi si dicono _uguali_ se, ridotti in forma normale, presentano stessa parte letterale e stessa parte numerica.

        #### Monomi opposti
        Due monomi in forma normale sono monomi opposti se sono simili e se hanno i coefficienti numerici opposti, come ad esempio $3abc^2$ e $−3abc^2$.

        #### Monomio nullo
        Qualsiasi monomio che ha $0$ come parte numerica è detto _monomio nullo_, a prescindere dalla parte letterale. I monomi nulli per definizione non hanno un grado  

        ### Polinomi
        Per polinomio si intende una qualsiasi _somma algebrica_ tra due o più monomi. Per indicare un generico polinomio si utilizza una lettera maiuscola, seguita dalle lettere che lo costituiscono racchiuse tra parentesi tonde, come ad esempio:

        - $P(x) = -3x^3 + x^2 - x + 1$
        - $Q(a,b) = -a^2b^2 + 2a^2b + 3ab^2 - ab$
        - $R(p,q,s) = -p - \sqrt{2}q + \frac{1}{4}s$

        Ricordando la definizione di monomio, $\quad2\sqrt{x}y\quad$ e $\quad5\frac{xy}{z} + 4xy\quad$ **non** sono polinomi in quanto alcuni dei loro elementi **non** sono dei monomi.

        ### Proprietà dei polinomi
        #### Polinomi in forma normale
        Un polinomio è definito normale se è costituito da soli monomi in forma normale e [non simili](#monomi-simili) tra loro. Prendiamo in esempio questo polinomio:  
        $$7a − 9b + 4 − 12a + 15ab − 12 − a$$
        esso **non** è un polinomio in forma normale poiché sono presenti monomi simili tra loro:
        $$\underline{7a} − 9b + \underline{\underline{4}} − \underline{12a} + 15ab − \underline{\underline{12}} − \underline{a}$$
        sommando i monomi simili otterremo un polinomio in forma normale:
        $$(7−12−1)\:a − 9b + 15ab + (4−12) = −6a − 9b + 15ab − 8$$

        #### Nomi dei polinomi in base al numero di termini
        A seconda del numero di termini che costituiscono i polinomi in forma normale, si possono usare nomi specifici per classificarli. Possiamo distinguere tra:

        - binomi: polinomi costituiti da due monomi non simili;
        - trinomi: polinomi costituiti da tre monomi non simili;
        - quadrinomi: polinomi costituiti da quattro monomi non simili.
 
        In presenza di un maggior numero di monomi si usa l'espressione _polinomio con $n$ termini_.

        #### Grado di un polinomio
        Si definisce **grado di un polinomio** il più alto tra i gradi dei monomi che lo compongono. Si definisce, invece, grado del polinomio _rispetto a una lettera_ il massimo dei gradi dei suoi monomi rispetto alla lettera considerata.

        #### Polinomi nulli, uguali e opposti
        Vale la stessa definizione dei [monomi uguali](#monomi-uguali), [opposti](#monomi-opposti) e [monomio nullo](#monomio-nullo).
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Operazioni tra monomi e tra polinomi
        ### Operazioni tra monomi
        #### Somma e differenza di monomi
        Per poter sommare due monomi è necessario che siano entrambi [simili](#monomi-simili); il risultato della somma è un monomio che possiede la stessa parte letterale degli addendi e come parte numerica presenta la somma algebrica delle parti numeriche degli addendi. Ad esempio:

        $$3ab + 7ab = 10ab$$

        $$5xy^2 + 2xy^2 - 4xy^2 = 3xy^2$$

        $$2a + 3b = 2a + 3b$$

        #### Prodotto tra monomi
        Il prodotto tra due monomi è un monomio in cui la parte numerica e la parte letterale sono date dal prodotto delle parti numeriche e delle parti letterali dei due fattori, as simple as that. Ad esempio:

        $$4x \cdot 3y = 12xy$$

        $$-2ab^2 \cdot 4ac = -8a^2b^2c$$

        #### Potenza di un monomio
        Per elevare alla potenza $n$-esima un monomio, bisogna elevare a potenza $n$-esima la parte numerica e moltiplicare per $n$ tutti gli esponenti della parte letterale. Ad esempio:

        $$(-2x^2yz)^2 = 4x^4y^2z^2$$

        $$(3abc^2)^3 = 27a^3b^3c^6$$

        ### Operazioni tra polinomi
        #### Addizione e sottrazione tra polinomi
        L'addizione/sottrazione tra polinomi restituisce un polinomio chiamato _polinomio somma_ che è costituito dalla somma di tutti i monomi simili presenti all'interno dei due polinomi di partenza. Dati due polinomi $P, Q$ la loro somma sarà data dall'operazione $P + Q$; la loro differenza, invece, sarà data dall'operazione $P + (-Q)$. Ad esempio, se $P(x,y) = 3x+2y-xy+5$ e $Q(x,y,z) = 5x+y+2z+3xy-xyz+8$:

        $$P(x,y)+Q(x,y,z)=(3x+2y-xy+5)+(5x+y+2z+3xy-xyz+8)=8x+3y+2z+2xy-xyz+13$$

        $$P(x,y)-Q(x,y,z)=(3x+2y-xy+5)+(-5x-y-2z-3xy+xyz-8)=-2x+y-2z-4xy+xyz-3$$

        #### Prodotto tra monomi e polinomi
        Per calcolare il prodotto tra un monomio e un polinomio (somma algebrica di monomi), basta applicare la proprietà distributiva all'operazione. Ad esempio:

        $$4xy\cdot(3x+z+2xy) = 4xy\cdot3x + 4xy\cdot z+4xy\cdot2xy = 12x^2y + 4xyz + 8x^2y^2$$

        $$−2ax(1−x−a) = −2ax+2ax^2+2a^2x$$

        Si può notare come il polinomio risultante ha come grado la somma dei gradi di monomio e polinomio.

        #### Prodotto tra polinomi
        Per calcolare il prodotto tra due polinomi, bisogna moltiplicare ogni monomio del primo polinomio col secondo polinomio, sommando tutti i risultati. Ad esempio:

        $$(2a+b)(a−b+2) = 2a\cdot(a−b+2) + b\cdot(a−b+2) = $$

        $$= (2a^2 - 2ab + 4a) + (ab - b^2 + 2b) = 2a^2 - b^2 - ab + 4a + 2b$$

        Valgono le stesse considerazioni anche per quanto riguarda il grado del polinomio risultante.

        #### Divisione di un polinomio per un monomio
        _Non conosco anima viva che abbia mai utilizzato o trovato utile 'sta cosa_. Oltre ad essere inutile è pure complicata ed è facilissimo sbagliare. 

        > Non lo so Volibear, io non la scrivo.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Scomposizione di polinomi""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Equazioni di primo e secondo grado""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Equazioni riconducibili al secondo grado""")
    return


if __name__ == "__main__":
    app.run()
