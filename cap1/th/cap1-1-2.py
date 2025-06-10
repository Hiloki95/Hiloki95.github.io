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
        * [Raccoglimento totale](#raccoglimento-totale)
        * [Raccoglimento parziale](#raccoglimento-parziale)
        * [Quadrato di binomio](#quadrato-di-binomio)
        * [Cubo di binomio](#cubo-di-binomio)
        * [Quadrato di trinomio](#quadrato-di-trinomio)
        * [Differenza di quadrati](#differenza-di-quadrati)
        * [Somma di cubi](#somma-di-cubi)
        * [Triangolo di Tartaglia](#triangolo-di-tartaglia)
        * [Trinomio notevole](#trinomio-notevole-con-somma-e-prodotto)
        * [Regola di Ruffini](#regola-di-ruffini)
        * [Divisione tra polinomi](#divisione-tra-polinomi)
    - [Equazioni di primo e secondo grado](#equazioni-di-primo-e-secondo-grado)
        * [Principi di equivalenza](#principi-di-equivalenza)
        * [Equazioni di primo grado](#equazioni-di-primo-grado)
        * [Equazioni di secondo grado](#equazioni-di-secondo-grado)
        * [Equazioni fratte](#equazioni-fratte)
        * [Equazioni parametriche](#equazioni-parametriche)
    - [Equazioni riconducibili al secondo grado](#equazioni-riconducibili-al-secondo-grado)
        * [Equazioni binomie](#equazioni-binomie)
        * [Equazioni trinomie](#equazioni-trinomie)
        * [Equazioni scomponibili](#equazioni-scomponibili)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Monomi e polinomi
    ## Monomi
    I monomi sono l'elemento costituente dei polinomi e sono caratterizzati dal prodotto tra una _parte numerica_ e una _parte letterale_. La parte numerica è un numero qualsiasi e viene detto _coefficiente_, mentre la parte letterale è un prodotto di potenze con base letterale ed esponente intero (positivo o nullo).

    Ad esempio, $-4a^2bc^3$ è un monomio: la parte numerica è $-4$ mentre la parte letterale è $a^2bc^3$.

    Altri esempi di monomi: $\quad3x^2$, $\quad\sqrt{2}xy$, $\quad\frac{5}{7}ab^3$ 

    **NB:** la parte letterale di un monomio è costituito da un **prodotto** di potenze di esponente **positivo** o nullo. Pertanto, elementi come $2a+bc$ o $3xy^{-1}$ **non sono dei monomi**.

    ## Proprietà dei monomi
    ### Gradi di un monomio
    Introduciamo le definizioni di grado _complessivo_ di un monomio e di grado di un monomio _rispetto a una lettera_. Il grado di un monomio rispetto a una lettera corrisponde all'esponente che presenta la lettera stessa all'interno del monomio; il grado complessivo di un monomio, invece, è la somma degli esponenti presenti nella sua parte letterale.

    Ad esempio, prendendo in considerazione il monomio $4x^3yz^2$, si può dire che:

    - il monomio è di grado 3 rispetto alla lettera $x$;
    - il monomio è di grado 1 rispetto alla lettera $y$;
    - il monomio è di grado 2 rispetto alla lettera $z$;
    - 6 è il grado complessivo del monomio.

    ### Monomi simili
    Due monomi si dicono _simili_ se, ridotti in forma normale (cioè riconducendo la parte numerica ad un singolo numero e quella letterale ad un prodotto di lettere **non ripetute**), presentano la stessa parte letterale. Ad esempio:

    - $5xy^2$ e $2xy^2$ sono due monomi simili;
    - $ab$ e $ab^2$ **non** sono due monomi simili.

    ### Monomi uguali
    Due monomi si dicono _uguali_ se, ridotti in forma normale, presentano stessa parte letterale e stessa parte numerica.

    ### Monomi opposti
    Due monomi in forma normale sono monomi opposti se sono simili e se hanno i coefficienti numerici opposti, come ad esempio $3abc^2$ e $−3abc^2$.

    ### Monomio nullo
    Qualsiasi monomio che ha $0$ come parte numerica è detto _monomio nullo_, a prescindere dalla parte letterale. I monomi nulli per definizione non hanno un grado  

    ## Polinomi
    Per polinomio si intende una qualsiasi _somma algebrica_ tra due o più monomi. Per indicare un generico polinomio si utilizza una lettera maiuscola, seguita dalle lettere che lo costituiscono racchiuse tra parentesi tonde, come ad esempio:

    - $P(x) = -3x^3 + x^2 - x + 1$
    - $Q(a,b) = -a^2b^2 + 2a^2b + 3ab^2 - ab$
    - $R(p,q,s) = -p - \sqrt{2}q + \frac{1}{4}s$

    Ricordando la definizione di monomio, $\quad2\sqrt{x}y\quad$ e $\quad5\frac{xy}{z} + 4xy\quad$ **non** sono polinomi in quanto alcuni dei loro elementi **non** sono dei monomi.

    ## Proprietà dei polinomi
    ### Polinomi in forma normale
    Un polinomio è definito normale se è costituito da soli monomi in forma normale e [non simili](#monomi-simili) tra loro. Prendiamo in esempio questo polinomio:  
    $$7a − 9b + 4 − 12a + 15ab − 12 − a$$
    esso **non** è un polinomio in forma normale poiché sono presenti monomi simili tra loro:
    $$\underline{7a} − 9b + \underline{\underline{4}} − \underline{12a} + 15ab − \underline{\underline{12}} − \underline{a}$$
    sommando i monomi simili otterremo un polinomio in forma normale:
    $$(7−12−1)\:a − 9b + 15ab + (4−12) = −6a − 9b + 15ab − 8$$

    ### Nomi dei polinomi in base al numero di termini
    A seconda del numero di termini che costituiscono i polinomi in forma normale, si possono usare nomi specifici per classificarli. Possiamo distinguere tra:

    - binomi: polinomi costituiti da due monomi non simili;
    - trinomi: polinomi costituiti da tre monomi non simili;
    - quadrinomi: polinomi costituiti da quattro monomi non simili.

    In presenza di un maggior numero di monomi si usa l'espressione _polinomio con $n$ termini_.

    ### Grado di un polinomio
    Si definisce **grado di un polinomio** il più alto tra i gradi dei monomi che lo compongono. Si definisce, invece, grado del polinomio _rispetto a una lettera_ il massimo dei gradi dei suoi monomi rispetto alla lettera considerata.

    ### Polinomi nulli, uguali e opposti
    Vale la stessa definizione dei [monomi uguali](#monomi-uguali), [opposti](#monomi-opposti) e [monomio nullo](#monomio-nullo).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Operazioni tra monomi e tra polinomi
    ## Operazioni tra monomi
    ### Somma e differenza di monomi
    Per poter sommare due monomi è necessario che siano entrambi [simili](#monomi-simili); il risultato della somma è un monomio che possiede la stessa parte letterale degli addendi e come parte numerica presenta la somma algebrica delle parti numeriche degli addendi. Ad esempio:

    $$3ab + 7ab = 10ab$$

    $$5xy^2 + 2xy^2 - 4xy^2 = 3xy^2$$

    $$2a + 3b = 2a + 3b$$

    ### Prodotto tra monomi
    Il prodotto tra due monomi è un monomio in cui la parte numerica e la parte letterale sono date dal prodotto delle parti numeriche e delle parti letterali dei due fattori, as simple as that. Ad esempio:

    $$4x \cdot 3y = 12xy$$

    $$-2ab^2 \cdot 4ac = -8a^2b^2c$$

    ### Potenza di un monomio
    Per elevare alla potenza $n$-esima un monomio, bisogna elevare a potenza $n$-esima la parte numerica e moltiplicare per $n$ tutti gli esponenti della parte letterale. Ad esempio:

    $$(-2x^2yz)^2 = 4x^4y^2z^2$$

    $$(3abc^2)^3 = 27a^3b^3c^6$$

    ## Operazioni tra polinomi
    ### Addizione e sottrazione tra polinomi
    L'addizione/sottrazione tra polinomi restituisce un polinomio chiamato _polinomio somma_ che è costituito dalla somma di tutti i monomi simili presenti all'interno dei due polinomi di partenza. Dati due polinomi $P, Q$ la loro somma sarà data dall'operazione $P + Q$; la loro differenza, invece, sarà data dall'operazione $P + (-Q)$. Ad esempio, se $P(x,y) = 3x+2y-xy+5$ e $Q(x,y,z) = 5x+y+2z+3xy-xyz+8$:

    $$P(x,y)+Q(x,y,z)=(3x+2y-xy+5)+(5x+y+2z+3xy-xyz+8)=8x+3y+2z+2xy-xyz+13$$

    $$P(x,y)-Q(x,y,z)=(3x+2y-xy+5)+(-5x-y-2z-3xy+xyz-8)=-2x+y-2z-4xy+xyz-3$$

    ### Prodotto tra monomi e polinomi
    Per calcolare il prodotto tra un monomio e un polinomio (somma algebrica di monomi), basta applicare la proprietà distributiva all'operazione. Ad esempio:

    $$4xy\cdot(3x+z+2xy) = 4xy\cdot3x + 4xy\cdot z+4xy\cdot2xy = 12x^2y + 4xyz + 8x^2y^2$$

    $$−2ax(1−x−a) = −2ax+2ax^2+2a^2x$$

    Si può notare come il polinomio risultante ha come grado la somma dei gradi di monomio e polinomio.

    ### Prodotto tra polinomi
    Per calcolare il prodotto tra due polinomi, bisogna moltiplicare ogni monomio del primo polinomio col secondo polinomio, sommando tutti i risultati. Ad esempio:

    $$(2a+b)(a−b+2) = 2a\cdot(a−b+2) + b\cdot(a−b+2) = $$

    $$= (2a^2 - 2ab + 4a) + (ab - b^2 + 2b) = 2a^2 - b^2 - ab + 4a + 2b$$

    Valgono le stesse considerazioni anche per quanto riguarda il grado del polinomio risultante.

    ### Divisione di un polinomio per un monomio
    _Non conosco anima viva che abbia mai utilizzato o trovato utile 'sta cosa_. Oltre ad essere inutile è pure complicata ed è facilissimo sbagliare. 

    > Non lo so Volibear, io non la scrivo.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Scomposizione di polinomi
    Qui ti mostro un po' le principali tecniche di scomposizione dei polinomi. Non le metto tutte perché alcune sono necessarie solo in casi stupidamente rari e richiedono la conoscenza della divisione tra polinomi (che non piace a nessuno)

    ## Raccoglimento totale
    Il raccoglimento totale (o a fattor comune) è il tipo di scomposizione più semplice di tutti: mette in evidenza il fattore comune tra tutti i termini di un polinomio. La scomposizione risultante è composta dal prodotto tra il termine comune e un polinomio. Prendiamo come esempio il seguente polinomio:

    $$ 12x^6 + 8x^3 + 16x^2y$$

    tutti e tre i nomoni che lo costituiscono sono divisibili per 4 e per $x^2$. Pertanto, il monomio $4x^2$ è un fattore comune del polinomio di partenza (in questo caso, è il più grande fattore comune e nel 99% è quello che si vuole cercare). Dividendo tutti i monomi per il fattore comune, otterremo il raccoglimento totale:

    $$ 12x^6 + 8x^3 + 16x^2y = 4x^2\:(3x^4 + 2x + 4y) $$

    Per verificare di aver raccolto correttamente, basta rimoltiplicare il fattore comune per vedere se si ottiene il polinomio di partenza.

    NB: il fattore comune **non necessariamente** è un monomio. In questo esempio raccogliamo un polinomio: 

    $$ 3(x-1)^4 + 6x(x-1)^2 - (x-1)^3 = (x-1)^2\:(3(x-1)^2 + 6x - (x-1)) $$

    ## Raccoglimento parziale
    Questa scomposizione è applicabile per polinomi composti da un numero pari di monomi e consiste in due raccoglimenti consecutivi: uno intermedio seguito da uno totale. Facciamo prima con un esempio, prendiamo in considerazione il seguente polinomio:

    $$ x^3 + x^2 + 3x + 3 $$

    non esiste un fattor comune a tutti e quattro i monomi del polinomio. Esistono però dei fattori comuni ad alcune coppie di monomi, ad esempio i primi due monomi sono divisibili per $x^2$ e gli ultimi sono divisibili per 3. Svolgendo questo raccoglimento intermedio per coppie:

    $$ x^3 + x^2 + 3x + 3 = x^2\:(x + 1) + 3\:(x + 1) $$

    si è arrivati alla somma di due termini che adesso hanno un fattore in comune, cioè $(x + 1)$. Pertanto, è possibile svolgere un secondo raccoglimento:

    $$ x^2\:(x + 1) + 3\:(x + 1) = (x + 1)\:(x^2 + 3) $$

    ultimando il raccoglimento parziale. Anche in questo caso si può verificare di aver svolto correttamente il raccoglimento rimoltiplicando i due polinomi ottenuti. Il raccoglimento risultante è dunque:

    $$ x^3 + x^2 + 3x + 3 = x^2\:(x + 1) + 3\:(x + 1) = (x + 1)\:(x^2 + 3) $$

    NB: nel raccoglimento parziale è come se vigesse una specie di *proprietà commutativa*, pertanto la scelta dei fattori comuni del raccoglimento intermedio **non è univoca**. Per esempio, posso raccogliere diversamente i monomi del polinomio di prima: posso dividere il primo e il terzo monomio per $x$ e il secondo e il quarto per %1%, ottenendo:

    $$ x^3 + x^2 + 3x + 3 = x\:(x^2 + 3) + (1)\:(x^2 + 3) = (x^2 + 3)\:(x + 1) $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Quadrato di binomio
    Su questi andiamo spediti, dai. Parliamo di *prodotti notevoli*, un insieme di formule che aiutano a sviluppare dei calcoli che, se si dovessero sempre fare a mano, risulterebbero lunghi e noiosi. Sul quadrato di binomio non c'è molto da dire, è una formula secca da ricordare e sicuramente te la ricordi. Dato un binomio $(x + y)$, il suo quadrato sarà dato dal trinomio:

    $$ (x+y)^2 = x^2 + 2xy + y^2 $$

    Bisogna solo stare attenti ai segni di $x$ e $y$. Nonostante la formula sia semplice da ricordare, molto spesso è importante saper svolgere il procedimento inverso, cioè vedere un trinomio e accorgersi che quello è il risultato di un quadrato di binomio.

    ## Cubo di binomio
    Anche qui si tratta di una formula e basta. Dato un binomio $(x + y)$, il suo cubo sarà dato dal quadrinomio:

    $$ (x+y)^3 = x^3 + 3x^2y + 3 xy^2 + y^3 $$

    Anche in questo caso bisogna stare molto attenti ai segni di $x$ e $y$ e anche in questo caso è più utile riconoscere il cubo dal quadrinomio che non il sapere la formula.

    ## Quadrato di trinomio
    Ennesima formula con le stesse premesse di prima. Dato un trinomio $(x+y+z)$, il suo quadrato sarà dato dal polinomio:

    $$ (x+y+z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2xz $$

    ## Differenza di quadrati
    Uno dei prodotti notevoli più utili in assoluto. Dati due quadrati $x^2$ e $y^2$, la loro differenza è sempre data dal prodotto:

    $$ x^2 - y^2 = (x + y)\:(x - y) $$

    ## Somma di cubi
    Dati due cubi $x^3$ e $y^3$, la loro somma è data dal prodotto:

    $$ x^3 + y^3 = (x + y)\:(x^2 - xy + y^2) $$

    mentre la loro differenza dal prodotto:

    $$ x^3 - y^3 = (x - y)\:(x^2 + xy + y^2) $$

    NB: può sembrarlo a prima vista, ma il secondo termine della scomposizione **non è mai** un quadrato di binomio a sua volta.

    ## Triangolo di Tartaglia
    Grazie a questa costruzione è possibile calcolare qualsiasi scomposizione della potenza $n$-esima di un binomio.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    im = mo.image("C:\\Users\\enric\\Desktop\\marimo_notebooks\\tartaglia.png")
    mo.hstack([im], align='center', justify='center')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Per costruire ogni riga è necessario che ogni termine sia dato dalla somma dei due termini che stanno sopra alla sua sinistra e sopra alla sua destra. Ogni riga rappresenta i coefficienti del polinomio risultante dalla potenza $n$-esima del binomio $(x+y)$. Le potenze di $x$ e $y$ vanno messe in ordine crescente per una variabile e decrescente per l'altra. Ad esempio, se volessimo calcolare la potenza $(x+y)^5$ prendiamo come riferimento la riga $n=5$ del triangolo di Tartaglia:

    $$ (x+y)^5 = x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5 $$

    ## Trinomio notevole con somma e prodotto
    Il trinomio notevole è una regola di scomposizione attuabile per i trinomi che si presentano nella seguente forma:

    $$ x^2 + sx + p $$

    il trinomio così formato è detto *trinomio particolare* o *trinomio caratteristico*. I coefficienti $s$ e $p$ rappresentano rispettivamente la somma e il prodotto di due opportuni numeri $a$ e $b$. Il trinomio notevole può essere dunque scomposto nel seguente prodotto:

    $$ x^2 + sx + p = (x + a)\:(x + b) $$

    In parole povere: se esistono due numeri $a$ e $b$ che sommati danno $s$ e moltiplicati danno $p$, allora è possibile applicare la scomposizione mostrata sopra. Prendiamo in esempio il polinomio:

    $$ x^2 + 5x + 6 $$

    esistono due numeri che sommati danno 5 e moltiplicati danno 6? Sì, e sono +3 e +2. Avremo dunque la scomposizione in:

    $$ x^2 + 5x + 6 = (x + 2)\:(x + 3) $$

    Cosa succede se è presente anche un coefficiente $a$ per il termine al quadrato? La scomposizione è ancora possibile, ma con un accorgimento in più. Dato un trinomio della forma:

    $$ ax^2 + sx + p $$

    esso si potrà scomporre nel prodotto

    $$ ax^2 + sx + p = (ax + t_1)\left(x + \frac{t_2}{a}\right) $$

    dove $t_1$ e $t_2$, stavolta, sono due numeri che sommati danno $s$ e moltiplicati danno $a\cdot p$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Regola di Ruffini
    La scomposizione più odiata del mondo perché non consiste in una formula o in un metodo di due passaggi. 

    Sinceramente non so se metterla, sarebbe fondamentale se fossi una studentessa dello scientifico ma non credo sarà utile per delle domande di un test che dura pochissimo. 

    In caso fammi sapere se la vuoi messa, anche solo per curiosità.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Divisione tra polinomi
    > "Marco, uh, B. Porterai la divisione tra polinomi?"
    > 
    > "Ah, la merda. Emh. No."
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Equazioni di primo e secondo grado
    Le equazioni sono uguaglianze tra espressioni matematiche in cui compaiono una o più incognite; risolvere un'equazione significa determinare i valori numerici che, sostituiti al posto dell'incognita, rendono vera l'uguaglianza.

    ## Principi di equivalenza
    Concetto semplicissimo ma fondamentale, i calcoli svolti per risolvere le equazioni si basano su due principi:

    - *primo principio di equivalenza:* data una qualsiasi equazione, sommare o sottrarre entrambi i membri dell'equazione per una quantità non nulla ci fa ottenere un'equazione equivalente a quella di partenza. Applicazione pratica del primo principio: è possibile **spostare** un termine da un membro all'altro dell'equazione semplicemente cambiandolo di segno [es: $x - 1 = 3x + 2$ è equivalente a $x = 3x + 3$ perché ho spostato e cambiato di segno il $-1$] 
    - *secondo principio di equivalenza:* data una qualsiasi equazione, moltiplicare o dividere entrambi i membri dell'equazione per una quantità non nulla ci fa ottenere un'equazione equivalente a quella di partenza.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Equazioni di primo grado
    Un'equazione è definita di primo grado in un'incognita quando è riconducibile, utilizzando tecniche di scomposizione e sfruttando i principi di equivalenza, alla forma:  

    $$ ax = b $$

    Generalmente ci ritroveremo come equazione di partenza un'uguaglianza tra due polinomi di primo grado, entrambi in $x$. Una volta ridotta l'uguaglianza alla forma riportata di sopra, la soluzione dell'equazione è semplicemente: 

    $$ x = \frac{b}{a} $$

    Risolviamo per esempio la seguente equazione (mostriamo tutti i passaggi, a prova di scemo): 

    $$ 3x + 5 = 7 $$

    $$ 3x = 7 - 5 $$

    $$ 3x = 2 $$

    $$ \frac{\cancel3\:x}{\cancel3} = \frac{2}{3} $$

    $$ x = \frac{2}{3} $$

    ## Equazioni di secondo grado
    Un'equazione è invece definita di secondo grado in un'incognita quando è riconducibile alla forma: 

    $$ ax^2 + bx + c = 0$$

    Bisogna distinguere tra 4 casistiche in base ai coefficienti dell'equazione: 

    - se tutti i coefficienti sono diversi da zero, l'equazione di secondo grado si dice *completa*;
    - $a = 0$: in questo caso, abbiamo davanti di fatto un'equazione di primo grado;
    - $b = 0$: in questo caso, l'equazione si chiama *equazione di secondo grado pura*;
    - $c = 0$: in questo caso, si parla di *equazione di secondo grado spuria*.

    Per risolvere un'equazione di secondo grado completa, esiste la famosissima formula risolutiva: 

    $$ x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

    il segno del **discriminante** ($\Delta$), cioè la quantità presente sotto radice quadrata, ci permette di determinare la quantità e la natura delle soluzioni: 

    - se $\Delta < 0$, l'equazione non ammette soluzioni reali;
    - se $\Delta = 0$, l'equazione ammette due soluzioni reali e coincidenti;
    - se $\Delta > 0$, l'equazione ammette due soluzioni reali e distinte.

    Per risolvere invece un'equazione di secondo grado pura, bisogna svolgere i seguenti passaggi: 

    $$ ax^2 + c = 0 $$

    $$ ax^2 = -c $$

    $$ x^2 = -\frac{c}{a} $$

    $$ x_{1,2} = \pm\sqrt{-\frac{c}{a}} $$

    Per risolvere un'equazione di secondo grado spuria, bisogna effettuare il raccoglimento di $x$: 

    $$ ax^2 + bx = 0 $$

    $$ x\:(ax + b) = 0 $$

    e si applica la *legge di annullamento del prodotto*: se il prodotto di due quantità è zero, allora una delle due è pari a zero: 

    $$ x_1 = 0;\qquad x_2 = -\frac{b}{a}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Equazioni fratte
    Un'equazione si dice *fratta* se l'incognita compare almeno una volta al denominatore di una frazione. Sfruttando i principi di equivalenza è possibile ricondurle a delle equazioni di primo/secondo grado classiche, ma bisogna avere un'accortezza in più: bisogna prima studiare le **condizioni di esistenza**. In pratica, bisogna determinare quei valori di $x$ che rendono i denominatori in cui compare nulli; quei valori non saranno ammessi come eventuale soluzione dell'equazione. Svolgiamone una come esempio: 

    $$ \frac{x+4}{3x+3} = \frac{x}{1+x} $$

    per studiare le CE bisogna imporre che $\quad3x + 3 \neq 0\quad$ e che $\quad1 + x \neq 0$. 

    Entrambe le condizioni ci portano ad escludere $x = -1$ come soluzione dell'equazione. Possiamo adesso svolgere i calcoli:  

    $$ (x+4)\:(1+x) = x\:(3x+3) $$

    $$ x + x^2 + 4 + 4x = 3x^2 +3x $$

    $$ -2x^2 +5x + 4 = 0 $$

    $$ 2x^2 - 5x - 4 = 0 $$

    $$ x_{1,2} = \frac{5 \pm \sqrt{25-(-32)}}{10} = \frac{1 \pm \sqrt{57}}{2} $$

    Entrambe le soluzioni sono accettabili poiché diverse da $x = -1$.

    ## Equazioni parametriche
    Un'equazione si dice *parametrica* se, oltre all'incognita, sono presenti anche una o più parametri/variabili. Generalmente i parametri sono indicati con le lettere $a$, $b$, $c$, $k$ e $t$ e sono sostanzialmente dei placeholder per un numero a noi sconosciuto, **da non confondere con l'incognita**. Essendo un numero sconosciuto, la presenza della variabile renderà la soluzione dell'equazione **un'espressione algebrica** e non più un numero. Svolgiamo per esempio un'equazione parametrica di primo grado: 

    $$ a^2x = (a+1)\:(a-1) + ax $$

    $$ a^2x - ax = (a+1)\:(a-1) $$

    $$ ax\:(a-1) = (a+1)\:(a-1) $$

    $$ x = \frac{(a+1)\:\cancel{(a-1)}}{a\:\cancel{(a-1)}} = \frac{a+1}{a};\qquad \text{con}\:a\neq0$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Equazioni riconducibili al secondo grado

    Esistono alcuni tipo di equazioni di grado superiore al secondo che si possono risolvere in maniera *relativamente semplice*. Le equazioni in questione si chiamano *riconducibili al secondo grado* perché, appunto, è possibile trattarle come delle equazioni di secondo grado se si tiene conto di alcuni accorgimenti.

    Le equazioni riconducibili al secondo grado sono sostanzialmente divise in tre tipologie:

    - equazioni binomie;
    - equazioni trinomie;
    - equazioni scomponibili.

    ## Equazioni binomie
    Queste equazioni, come suggerisce il nome, sono composte da due soli termini. Sono dunque delle equazioni che si presentano nella forma:

    $$ ax^n + b = 0 $$

    Se $n = 1$ e $n = 2$, l'equazione prende una forma che già conosciamo e sappiamo risolvere, quindi ci concentriamo sui casi in cui $n>2$. Proviamo a risolverla: 

    $$ ax^n = -b $$

    $$ x^n = -\frac{b}{a}$$

    A questo punto basta applicare la radice $n-$esima per ottenere i valori di $x$. Bisogna però fare un'importante distinzione: 

    - se $n$ è dispari, non bisogna fare nessun controllo sul segno di $a$ e $b$ perché le radici con esponenti dispari **possono essere svolte su numeri negativi**. Pertanto, otterremo come soluzione:

    $$ x = -\sqrt[n]{\frac{b}{a}} $$

    - se $n$ è pari, invece, bisogna fare attenzione che la frazione $-b/a$ sia positiva. Una volta fatto questo controllo, se la frazione è negativa l'equazione non ammette soluzioni reali, se invece è positiva si avranno le seguenti soluzioni:

    $$ x_{1,2} = \pm \sqrt[n]{-\frac{b}{a}} $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Equazioni trinomie
    Queste equazioni sono riconducibili al secondo grado se si presentano nella particolare forma: 

    $$ ax^{2n} + bx^n + c = 0 $$

    Si può notare che se $n=1$ ci ritroviamo con una classica equazione di secondo grado completa, dunque ci soffermiamo sui casi in cui $n>1$.

    Per risolvere questo tipo di equazioni si svolge una *sostituzione*: sostanzialmente si pone l'uguaglianza $y = x^n$ (si può usare $t$ al posto di $y$, anche se di base puoi usare il simbolo che vuoi) e si sostituisce $y$ nell'equazione di partenza. Così facendo si ottiene: 

    $$ y = x^n \quad\rightarrow\quad ay^2 + by +c = 0$$

    Ci siamo appunto *ricondotti* ad un'equazione di secondo grado in $y$. Adesso è semplice risolvere l'equazione utilizzando la classica formula risolutiva.

    Una volta risolta, però, bisogna ricordarsi che l'equazione di partenza ci richiedeva di trovare delle soluzioni per la variabile $x$ e non $y$. Pertanto, una volta trovate le soluzioni per $y$, bisogna ritornare alla sostituzione che abbiamo fatto all'inizio: 

    $$ y = x^n \quad\rightarrow\quad x^n = y $$

    Avendo già risolto l'equazione in $y$, adesso per noi $y$ è solo un (o più) numero. Pertanto questa è diventata un'equazione binomia che va risolta come mostrato nel paragrafo di prima. Risolviamo un'equazione come esempio: 

    $$ x^6 + 5x^3 + 6 = 0 $$

    $$ y = x^3 \quad\rightarrow\quad y^2 + 5y + 6 = 0 $$

    $$ y_{1,2} = \frac{-5 \pm \sqrt{25-24}}{2} = \frac{-5 \pm 1}{2} \quad\rightarrow\quad y_1 = -3 \quad\lor\quad y_2 = -2$$

    $$ y = x^3 \quad\rightarrow\quad x^3 = -3 \quad\lor\quad x^3 = -2 $$

    $$ x_1 = \sqrt[3]{-3} \quad\lor\quad x_2 = \sqrt[3]{-2} $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Equazioni scomponibili
    Queste sono quelle dove ci vuole più fantasia di tutti per ricondurle a delle equazioni di secondo grado. Di base richiedono l'applicazione delle tecniche di scomposizione e, successivamente, della legge di annullamento del prodotto. Per quanto riguarda queste equazioni forse è meglio spiegarle provando a risolvere degli esempi: 

    - **Esempio 1:**

    $$ x^7 + 12x^6 + 35x^5 = 0 $$

    &ensp;&ensp;&ensp;&ensp;In questo caso, si può notare che è possibile raccogliere un bel $x^5$ in tutti termini. Così facendo otteniamo il prodotto tra un monomio e un trinomio del secondo grado completo: 

    $$ x^5\:(x^2 + 12x + 35) = 0 $$

    &ensp;&ensp;&ensp;&ensp;Sfruttando la legge di annullamento del prodotto otteniamo due equazioni, una monomia del quinto grado e una completa del secondo grado:

    $$ \left\| \begin{array}{l}
    x^5 = 0\\
     \\
    x^2 + 12x + 35 = 0
    \end{array} \right. $$

    &ensp;&ensp;&ensp;&ensp;La prima ha come soluzione banalmente $x_1 = 0$, svolgiamo la seconda:  

    $$ x^2 + 12x + 35 = 0 \quad\rightarrow\quad x_{2,3} = \frac{-12 \pm \sqrt{144-140}}{2} = \frac{-12 \pm 2}{2}
    \quad\rightarrow\quad x_2 = -7 \quad\lor\quad x_3 = -5 $$

    - **Esempio 2:**

    $$ x^5 + 3x^4 - x - 3 = 0 $$

    &ensp;&ensp;&ensp;&ensp;In questo caso è possibile scomporre il polinomio con un raccoglimento parziale, raccogliendo un $x^4$ e un $-1$: 

    $$ x^5 + 3x^4 - x - 3 = x^4\:(x + 3) - (x + 3) = (x + 3)\:(x^4 - 1) = 0 $$

    &ensp;&ensp;&ensp;&ensp;Anche qui applichiamo la legge di annullamento del prodotto: 

    $$ \left\| \begin{array}{l}
    x + 3 = 0\\
     \\
    x^4 - 1 = 0
    \end{array} \right. $$

    &ensp;&ensp;&ensp;&ensp;La prima equazione ha come soluzione $x_1 = -3$, risolviamo invece l'equazione binomia di quarto grado: 

    $$ x^4 - 1 = 0 \quad\rightarrow\quad x^4 = 1$$

    &ensp;&ensp;&ensp;&ensp;L'esponente è pari e il numero a destra dell'uguale è positivo, dunque l'equazione ammette le due soluzioni:  

    $$ x_{2,3} = \pm \sqrt[4]{1} = \pm 1 $$

    &ensp;&ensp;&ensp;&ensp;L'equazione in totale, dunque, ammette le tre soluzioni: 

    $$ x_1 = -3 \quad\lor\quad x_2 = -1 \quad\lor\quad x_3 = 1 $$
    """
    )
    return


if __name__ == "__main__":
    app.run()
