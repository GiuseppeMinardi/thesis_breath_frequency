# Breath Frequency MedThesis

Estimate Ventilatory Threshold from Respiratory Rate

## Descrizione del Progetto

Il progetto consiste in uno studio statistico per una tesi di specializzazione in Medicina dello Sport. L'obiettivo è validare l'utilizzo della dinamica della frequenza respiratoria e della sua variabilità come metodo non invasivo per stimare le soglie ventilatorie ($VT_1$ e $VT_2$) durante uno sforzo fisico incrementale, confrontandole con il Gold Standard dei gas espirati.

## Analisi

### Validazione delle Soglie Ventilatorie

L'obiettivo è verificare la correlazione tra le soglie stimate tramite frequenza respiratoria e quelle ottenute tramite test cardiopolmonare tradizionale. Le soglie respiratorie sono individuate tramite interpolazione polinomiale e calcolo della derivata seconda per trovare i punti di massima accelerazione (validazione del metodo gia' fornito).

#### Test Statistici

* **Correlazione**: Utilizzo della correlazione di Pearson o Spearman, valutando la scelta in base alla distribuzione dei dati data la dimensione ridotta del campione ($n=20$). Si valuta anche di usare altri metodi per rendere piu' robusta l'analisi data la bassa numerosita' del campione e per fornire anche una stima dell'errore.
* **Accordo tra i metodi**: Creazione di **Bland-Altman Plot** per valutare l'accordo tra il nuovo metodo e il Gold Standard, con relativo calcolo del *Standard Error of Estimate* (SEE).

### Studio della Variabilità Respiratoria (BRV)

Lo studio analizza come la variabilità del respiro si modifichi all'aumentare dell'intensità dell'esercizio.

* **Analisi nel Dominio del Tempo**: Calcolo del parametro **RMSSD** (Root Mean Square of Successive Differences) applicato agli intervalli respiro-su-respiro ($T_{tot}$).
* **Analisi nelle Zone Metaboliche**: Dimostrazione della riduzione della variabilità nel passaggio dalla Zona 1 (aerobica) alla Zona 3 (massimale).
* **Parametri Aggiuntivi**: Valutazione dell'andamento del Volume Corrente ($V_t$) e della Ventilazione al minuto ($V_e$) per verificare se l'integrazione di queste grandezze possa migliorare l'accuratezza predittiva del metodo.
