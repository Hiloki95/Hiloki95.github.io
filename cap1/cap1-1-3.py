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
    # Cap. 1.1.3: Sistemi di equazioni e disequazioni - Indice
    - [Sistemi lineari](#sistemi-lineari)
        * [Metodo di sostituzione](#metodo-di-sostituzione)
        * [Metodo del confronto](#metodo-del-confronto)
        * [Metodo di riduzione](#metodo-di-riduzione)
        * [Metodo di Cramer](#metodo-di-cramer)
    - [Disequazioni](#disequazioni)
        * [Differenze tra disequazioni ed equazioni](#differenze-tra-disequazioni-ed-equazioni)
        * [Disequazioni di primo grado](#disequazioni-di-primo-grado)
        * [Disequazioni di secondo grado](#disequazioni-di-secondo-grado)
        * [Disequazioni con prodotto](#disequazioni-con-prodotto)
        * [Disequazioni fratte](#disequazioni-fratte)
    - [Sistemi di disequazioni](#sistemi-di-disequazioni)

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Sistemi lineari
    Un sistema di equazioni è un gruppo di due o più equazioni in cui sono presenti due o più incognite che vengono **correlate** tra loro. Mostro qualche esempio: 

    $$ \left\{ \begin{array}{l}
    x + 2y = 3 \\
     \\
    y = 4 - 3 x 
    \end{array} \right.
    \qquad\qquad
    \left\{ \begin{array}{l}
    x + 2z = 3 \\
     \\
    x = 4 - 5 y \\
    \\
    z = -2x+ 7y + 3
    \end{array} \right. $$

    In questo capitolo ci occupiamo in particolare dei sistemi *lineari*, cioè quelli in cui le equazioni presenti sono tutte di primo grado nelle varie incognite.

    **NB:** per far sì che siano risolvibili e che abbiano senso, i sistemi devono contenere **tante incognite quante sono le equazioni presenti**. Pertanto, nei sistemi di due equazioni devono essere presenti due incognite, in quelli a tre equazioni tre incognite, e così via.

    ## A cosa serve risolvere un sistema di equazioni? 
    Risolvere un sistema vuol dire trovare il valore delle incognite presenti tali per cui è possibile soddisfare le uguaglianze di tutte le equazioni presenti nel sistema stesso. Nei problemi di fisica (ma anche nei problemi di logica) è possibile trascrivere delle informazioni fornite sottoforma di equazioni, ma spesso non è possibile risolverle da sole perché contengono più di un'incognita. **Correlare** tra loro due o più informazioni si traduce matematicamente in "mettere a sistema" le equazioni che rappresentano quelle informazioni. Facciamo un esempio con un classico problema di logica che troveresti nei giochi del Professor Layton: 

    > Andrea e Beatrice sono due amici di famiglia. Quando Andrea ha iniziato la scuola materna, Beatrice aveva il doppio dell'età di Andrea. Dopo soltanto 4 anni, però, Beatrice aveva solo una volta e mezzo l'età di Andrea. Quanti anni aveva Andrea quando ha iniziato la scuola materna?

    Proviamo a risolvere l'enigma impostando un sistema di equazioni. Chiamiamo con $A$ l'età di Andrea quando ha iniziato la scuola materna e con $B$ l'età che aveva Beatrice nello stesso anno. 

    Innanzitutto, riusciremo a costruire un sistema risolvibile? Abbiamo due incognite che sono le età di Andrea e Beatrice quando Andrea ha iniziato la scuola materna; abbiamo inoltre due informazioni sulle suddette età: una riguardante l'anno in cui Andrea ha iniziato la scuola materna e un'altra riguardante i 4 anni successivi. Avendo due incognite e due informazioni (che possiamo trasformare in equazioni) è possibile costruire un sistema di equazioni risolvibile.

    Trasformiamo adesso le due informazioni in due equazioni nelle incognite $A$ e $B$: 

    - "Quando Andrea ha iniziato la scuola materna, Beatrice aveva il doppio dell'età di Andrea" $\quad\rightarrow\quad B = 2A$
    - "Dopo soltanto 4 anni, però, Beatrice aveva solo una volta e mezzo l'età di Andrea" $\quad\rightarrow\quad (B+4) = \frac{3}{2}\:(A+4)$

    Il sistema risultante è pertanto il seguente: 

    $$ \left\{ \begin{array}{l}
    B = 2A \\
     \\
    (B+4) = \frac{3}{2}\:(A+4) 
    \end{array} \right. $$

    Che ammette come risultato la seguente coppia di incognite (vediamo in seguito come risolverlo): 

    $$ A = 4 \quad\lor\quad B = 8 $$

    Dunque, la soluzione dell'enigma è 4.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Metodo di sostituzione
    Esistono quattro metodi di risoluzione dei sistemi lineari. Il metodo di sostituzione è quello concettualmente più semplice. Esso si basa sull'isolare una sola incognita (a caso) all'interno di una equazione (anche questa a caso); si otterrà un'espressione letterale che può essere **sostituita** in un'equazione differente.

    Questo permetterà, nel giro di uno o più sostituzioni, di ottenere una soluzione numerica per una delle incognite. Sostituendo la soluzione numerica in una delle equazioni di partenza del sistema, sarà possibile ricavare le soluzioni numeriche per le altre incognite. 

    Svolgiamo un esempio di sistema lineare a due equazioni e due incognite (chiamati anche sistemi 2x2): 

    $$ \left\{ \begin{array}{l}
    x + y = 5 \\
     \\
    x - y = 1 
    \end{array} \right. $$

    Decido (arbitrariamente) di isolare la $x$ nella prima equazione e sostituirla nella seconda: 

    $$ \left\{ \begin{array}{l}
    x = 5 - y \\
     \\
    x - y = 1 
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = \blue{5 - y} \\
     \\
    \blue{(5 - y)} - y = 1 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = 5 - y \\
     \\- 2y = -4 
    \end{array} \right.
    $$

    Adesso, dalla seconda equazione è possibile ottenere la soluzione numerica per l'incognita $y$. Una volta calcolata, la sostituisco a sua volta nella prima equazione per ottenere anche la soluzione per $x$: 

    $$ \left\{ \begin{array}{l}
    x = 5 - y \\
     \\ 
     y = \frac{-4}{-2} = 2
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = 5 - \blue{2} = 3 \\
     \\ 
     \blue{y = 2}
    \end{array} \right.
    $$

    Abbiamo ottenuto dunque la nostra soluzione al sistema, che si scrive nella seguente forma: 

    $$ \left\{ \begin{array}{l}
    x = 3 \\
     \\ 
    y = 2
    \end{array} \right. $$

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Risolviamo adesso un sistema 3x3. Il procedimento è lo stesso, ma i calcoli saranno leggermente più lunghi e complessi essendoci un'incognita in più: 

    $$ \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    x - y + z = 1 \\
     \\
    x + 2y + 3z = 6 
    \end{array} \right. $$

    Isoliamo la $x$ nella prima equazione e la sostituiamo nelle altre due equazioni: 

    $$ \left\{ \begin{array}{l}
    x = \blue{z - y} \\
     \\ 
    \blue{(z - y)} - y + z = 1 \\
     \\
    \blue{(z - y)} + 2y + 3z = 6 
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    2z - 2y = 1 \rightarrow z - y = \frac{1}{2}\\
     \\
    y + 4z = 6 
    \end{array} \right.$$

    Se facciamo attenzione, possiamo notare come le ultime due equazioni siano diventate un piccolo sistema 2x2, visto che l'incognita $x$ non è più presente in nessuna delle due equazioni. Pertanto, possiamo procedere "ignorando" la prima equazione e risolvendo le altre due come se fossero un sistema 2x2 a sé stante. Procediamo isolando la $z$ dalla seconda equazione e sostituendola nella terza (**solo** nella terza, ignoriamo la prima equazione): 

    $$ \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    z = \blue{y + \frac{1}{2}}\\
     \\
    y + 4\:\blue{(y + \frac{1}{2})} = 6 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    z = y + \frac{1}{2}\\
     \\
    y + 4y + 2 = 6 \rightarrow 5y = 4
    \end{array} \right.$$

    Abbiamo ottenuto la soluzione per $y$. Sostituendola nella seconda equazione otterremo il risultato di $z$; infine, possiamo sostituire sia $y$ che $z$ nella prima equazione per ottenere l'ultimo risultato: 

    $$\left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    z = \blue{\frac{4}{5}} + \frac{1}{2} = \frac{2\cdot4 + 5}{10} = \frac{13}{10}\\
     \\
    \blue{y = \frac{4}{5}} 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = \blue{\frac{13}{10}} - \blue{\frac{4}{5}} = \frac{13-2\cdot4}{10} = \frac{5}{10} = \frac{1}{2}\\
     \\ 
    \blue{z = \frac{13}{10}}\\
     \\
    \blue{y = \frac{4}{5}} 
    \end{array} \right.$$

    Ottenendo così la seguente soluzione: 

    $$ \left\{ \begin{array}{l}
    x = \frac{1}{2}\\
     \\ 
    y = \frac{4}{5}\\
     \\
    z = \frac{13}{10}
    \end{array} \right. $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Metodo del confronto 
    Il metodo del confronto consiste nell'isolamento di un'incognita **in due equazioni** per poi procedere all'uguaglianza tra le due espressioni alla destra dell'uguale. Il concetto di base è abbastanza semplice: se riesco a dire dall'equazione 1 che $x$ vale "pippo" e dall'equazione 2 ricavo che $x$ vale "pluto", vorrà dire per forza che "pippo" è uguale a "pluto".

    Risolviamo il sistema 2x2 che abbiamo risolto prima col metodo di sostituzione: 

    $$ \left\{ \begin{array}{l}
    x + y = 5 \\
     \\
    x - y = 1 
    \end{array} \right. $$

    Isoliamo dunque la $x$ in entrambe le equazioni ed eguagliamo le due espressioni a destra dell'uguale (una delle due equazioni si riscrive e si tiene lì ad ogni passaggio): 

    $$ \left\{ \begin{array}{l}
    x = \blue{5 - y}\\
     \\
    x = \blue{y + 1} 
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = 5 - y\\
     \\
    \blue{y + 1} = \blue{5 - y} 
    \end{array} \right. $$

    Adesso è possibile ricavare il valore di $y$ dalla seconda equazione e lo si può sostituire nella prima per ottenere anche la $x$: 

    $$ \left\{ \begin{array}{l}
    x = 5 - y\\
     \\
    2y = 4 
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = 5 - \blue{2} = 3\\
     \\
    \blue{y = 2} 
    \end{array} \right.
    $$

    Ottenendo dunque il risultato che ci aspettavamo: 

    $$ \left\{ \begin{array}{l}
    x = 3\\
     \\
    y = 2 
    \end{array} \right. $$

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Risolviamo adesso il sistema 3x3 già svolto col precedente metodo: 

    $$ \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    x - y + z = 1 \\
     \\
    x + 2y + 3z = 6 
    \end{array} \right. $$

    Anche in questo caso isoliamo la $x$ in tutte le equazioni: 

    $$ \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    x = y - z + 1 \\
     \\
    x = 6 - 2y - 3z
    \end{array} \right. $$

    L'espressione più semplice è venuta fuori dalla prima equazione, quindi useremo quella per il metodo del confronto, sostituendola alla $x$ che compare nella seconda e nella terza equazione: 

    $$ \left\{ \begin{array}{l}
    x = \blue{z - y} \\
     \\ 
    \blue{z - y} = y - z + 1 \\
     \\
    \blue{z - y} = 6 - 2y - 3z 
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    -2y + 2z = 1 \\
     \\
    y + 4z = 6 
    \end{array} \right.$$

    Come era successo con l'altro metodo, ci siamo ritrovati in una situazione per cui le ultime due equazioni non dipendono più da $x$ e costituiscono un sistema 2x2 a sé stante. Risolviamolo utilizzando di nuovo il confronto (**NB**: è possibile utilizzare anche un qualsiasi altro metodo. L'aver iniziato con un metodo non ti vincola a doverlo usare ogni volta), isolando questa volta la $y$ e sostituendo a catena per ottenere tutte e tre le incognite: 

    $$ \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    y = \green{z - \frac{1}{2}} \\
     \\
    y = \green{6 - 4z}
    \end{array} \right. 
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    y = z - \frac{1}{2} \\
     \\
    \green{z - \frac{1}{2}} = \green{6 - 4z}
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    y = z - \frac{1}{2} \\
     \\
    5z = 6 + \frac{1}{2} = \frac{12+1}{2} = \frac{13}{2}
    \end{array} \right.$$

    $$ \left\{ \begin{array}{l}
    x = z - y \\
     \\ 
    y = \green{\frac{13}{10}} - \frac{1}{2} = \frac{13-5}{10} = \frac{8}{10} = \frac{4}{5} \\
     \\
    \green{z = \frac{13}{10}}
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = \green{\frac{13}{10}} - \blue{\frac{4}{5}} = \frac{13-2\cdot4}{10} = \frac{5}{10} = \frac{1}{2} \\
     \\ 
    \blue{y = \frac{4}{5}}\\
     \\
    \green{z = \frac{13}{10}}
    \end{array} \right.$$

    Ottenendo così la soluzione che ci aspettavamo: 

    $$ \left\{ \begin{array}{l}
    x = \frac{1}{2}\\
     \\ 
    y = \frac{4}{5}\\
     \\
    z = \frac{13}{10}
    \end{array} \right. $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Metodo di riduzione
    Nel metodo di riduzione si sfrutta i principi di equivalenza per far scomparire un'incognita da una delle equazioni. Facciamo un esempio per capire il concetto dietro questo metodo. Prendiamo in esame le due seguenti equazioni:

    $$ A = B \quad\lor\quad C = D$$

    Dove $A,B,C,$ e $D$ sono i membri (non importa conoscerli in questo momento) delle due equazioni. Se è vero che $A=B$, allora sarà anche vero che, per qualsiasi coefficiente $a$:

    $$a\cdot A = a\cdot B$$

    secondo il secondo principio di equivalenza. Secondo il primo principio di equivalenza, invece, io posso sommare ai due membri $C,D$ della seconda equazione una qualsiasi entità. Ad esempio, posso sommare ad entrambi i membri della seconda equazione la quantità $a\cdot A$:

    $$ C = D \quad\rightarrow\quad a\cdot A + C = a\cdot A + D$$

    ma, sapendo che $a\cdot A = a\cdot B$, possiamo anche dire che:

    $$ C = D \quad\rightarrow\quad a\cdot A + C = a\cdot A + D \quad\rightarrow\quad a\cdot A + C = a\cdot B + D $$

    Dunque di fatto, applicando i principi di equivalenza, **abbiamo praticamente "sommato" le due equazioni tra di loro** ottenendo un'equazione equivalenza. Sfruttando questo concetto, è possibile eliminare un'incognita all'interno di un sistema lineare.

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Risolviamo il solito sistema 2x2 che abbiamo risolto precedentemente: 

    $$ \left\{ \begin{array}{l}
    \blue{x + y = 5} \\
     \\
    \green{x - y = 1} 
    \end{array} \right. $$

    In questo caso mi accorgo che in entrambe le equazioni ho già "tutto pronto" poiché mi ritrovo con un $+y$ in un'equazione e un $-y$ nell'altra. Pertanto, mi basta sommarle per far scomparire momentaneamente l'incognita $y$ (al solito riscriviamo una delle due equazioni):

    $$ \left\{ \begin{array}{l}
    x + y = 5 \\
     \\
    \blue{(x+y)} + \green{(x - y)} = \blue5 + \green1 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x + y = 5 \\
     \\
    2x +\cancel y - \cancel y = 6
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x + y = 5 \\
     \\
    x = 3
    \end{array} \right.
    $$

    Avendo isolato l'incognita $x$ è stato possibile calcolarne il valore. Adesso rimane solo da sostituirla in una delle due equazioni di partenza per ottenere anche il risultato per l'incognita $y$:

    $$\left\{ \begin{array}{l}
    \blue3 + y = 5 \\
     \\
    \blue{x = 3}
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x = 3 \\
     \\
    y = 2
    \end{array} \right.
    $$

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Risolviamo anche il solito sistema 3x3: 

    $$ \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    x - y + z = 1 \\
     \\
    x + 2y + 3z = 6 
    \end{array} \right. $$

    Anche in questo caso siamo molto fortunati: se sommassimo la prima e la seconda equazione, elimineremmo in un colpo solo sia l'incognita $y$ che quella $z$! Proprio per questo motivo, non lo faremo e prenderemo una strada più lunga, così da dover essere costretti ad usare anche il secondo principio di equivalenza.

    Mi accorgo che posso sommare la seconda e la terza equazione per eliminare l'incognita $y$, visto che compare con segni opposti. In questo caso, però, se le sommassi così come sono non si eliminerebbero: devo prima *dimezzare* la terza equazione o *raddoppiare* la seconda per far sì che si abbiamo delle incognite $y$ eliminabili. Decido di *raddoppiare* dunque la seconda equazione e di sommarla alla terza:

    $$ \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    \blue{2\cdot (}x - y + z\blue) = 1\blue{\cdot 2} \\
     \\
    x + 2y + 3z = 6 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    \blue{2x - 2y + 2z = 2} \\
     \\
    \green{x + 2y + 3z = 6} 
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    \blue{(2x - 2y + 2z)} + \green{(x + 2y + 3z)} = \blue{2} + \green{6} \\
     \\
    x + 2y + 3z = 6
    \end{array} \right.
    \quad\rightarrow\quad
    \left\{ \begin{array}{l}
    x + y - z = 0 \\
     \\ 
    3x + 5z = 8 \\
     \\
    x + 2y + 3z = 6
    \end{array} \right.$$

    Come si può notare, il metodo di riduzione ha permesso di rimuovere un'incognita da una delle equazioni, portandoci ad avere un sistema di equazioni più semplificato. Ma questo **non vuol dire necessariamente** che è sempre possibile riapplicare lo stesso metodo per continuare la risoluzione del sistema. In questo caso, infatti, non esiste un modo per eliminare un'altra incognita utilizzando la riduzione. Pertanto, si dovrà continuare la risoluzione utilizzando gli altri metodi. 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Metodo di Cramer
    Questo è molto utile per i sistemi 3x3 e fa risparmiare un sacco di calcoli. La sua implementazione, però, richiederebbe la costruzione di un determinante di 3 matrici e l'applicazione della regola di Sarrus...

    Insomma, è molto utile ma ci vorrebbe troppo per impararlo e masterarlo; e visto che **ogni** sistema lineare si può risolvere con gli altri tre metodi, io questo lo salto volentieri visto che non ti si chiederà mai di risolvere un sistema con un metodo in particolare, non siamo mica al liceo. 
    > Zau. Nya~

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #Disequazioni
    In questa parte introdurremo le disequazioni; lo faremo molto velocemente perché, una volta capite le differenze con le equazioni, capire come risolverle sarà una passeggiata

    ##Differenze tra disequazioni ed equazioni

    - mentre le equazioni impongono una uguaglianza tra due membri in cui è presente l'incognita $x$, nelle disequazioni si impone una *diseguaglianza* tra i due membri. Si chiede dunque di trovare dei valori di $x$ per il quale uno dei due membri è maggiore o minore dell'altro;

    - risolvere le equazioni consiste nel trovare uno o più valori dell'incognita $x$, le soluzioni delle disequazioni sono invece sempre degli **intervalli** di valori che l'incognita $x$ può assumere per rendere la diseguaglianza valida;

    - le equazioni sono *simmetriche*, le disequazioni richiedono che si inverta il segno di diseguaglianza per scambiare i due membri ottenendo una disequazione equivalente (es: dire $A > B$ è equivalente a dire che $B<A$, ricordandoci **sempre** di invertire i simboli di maggiore e minore);

    - se si sfrutta il secondo principio di equivalenza nelle disequazioni moltiplicando o dividendo **per un numero negativo**, allora è obbligatorio **invertire il simbolo di maggiore/minore**.  

    ---
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ##Disequazioni di primo grado
    Una disequazione si definisce di primo grado se entrambi i membri della disequazione sono polinomi di primo grado o inferiore. Si risolvono allo stesso modo delle equazioni di primo grado, facendo attenzione in più al simbolo di maggiore o minore. Svolgiamone una per esempio: 

    $$ \frac{x}{5} - 2 \le 3x + \frac{1}{5} $$

    $$ \blue{5\cdot} \left(\frac{x}{5} - 2 \right) \le \left(3x + \frac{1}{5}\right)\blue{\cdot 5} 
    \quad\rightarrow\quad
    x - 10 \le 15x + 1
    \quad\rightarrow\quad
    x - 15x \le 1 + 10
    \quad\rightarrow\quad - 14x \le 11 $$

    Vogliamo adesso dividere entrambi i membri per $-14$, che è negativo, quindi dobbiamo invertire il segno di minore o uguale:

    $$ \frac{\cancel{-14}x}{\blue{\cancel{-14}}} \green\ge \frac{11}{\blue{-14}} $$

    Ottenendo dunque la soluzione: 

    $$ x \ge -\frac{11}{14} $$

    Questa soluzione implica che, sostituendo qualsiasi numero che sia uguale o maggiore a $-11/14$ all'incognita $x$, la diseguaglianza di partenza sarà verificata.

    ---
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""##Disequazioni di secondo grado""")
    return


@app.cell
def _(mo):
    mo.md(r"""##Disequazioni con prodotto""")
    return


@app.cell
def _(mo):
    mo.md(r"""##Disequazioni fratte""")
    return


if __name__ == "__main__":
    app.run()
