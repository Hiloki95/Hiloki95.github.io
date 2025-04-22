import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    return mo, plt


@app.cell
def _(mo):
    mo.md(
        r"""
        [questo capitolo è più per me per fare pratica con questo notebook python che per te *xd*]
        ## Capitolo 0 - TOLC-I
        ### Struttura del TOLC-I

        Il test è composto da 4 sezioni:

        - *Matematica* → 20 domande in 50 minuti;
        - *Logica* → 10 domande in 20 minuti;
        - *Scienze* → 10 domande in 20 minuti;
        - *Comprensione verbale* → 10 domande in 20 minuti.

        Dopo aver svolto queste 4 sezioni, è prevista un'ulteriore sezione formata da 30 domande di inglese da svolgere in 15 minuti.  
        Il sistema di attribuzione dei punti per le prime 4 sezioni è il seguente:

        - **1 punto** per ogni risposta **corretta**;
        - **0 punti** per ogni risposta **non data**;
        - **-0.25 punti** per ogni risposta **sbagliata**.

        Per quanto riguarda la parte di inglese, **non ci saranno penalizzazioni** per le risposte sbagliate. Non che avrai mai problemi in inglese, ma almeno sai che volendo puoi buttarti a caso.

        ### Ammissione a UNISA

        Per l'ammissione ad informatica senza colmare gli Obblighi Formativi Aggiuntivi (OFA) serve aver raggiunto un punteggio $\geq 16/50$. Con un punteggio compreso tra 9 (incluso) e 16 si è ammessi con l'obbligo degli OFA, mentre con un punteggio $\lt 9$ viene consigliato un anno di corsi di preparazione (wtf).
        """
    )
    return


if __name__ == "__main__":
    app.run()
