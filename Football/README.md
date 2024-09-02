<h1>Descriere</h1>
<p>Acest proiect este un instrument de machine learning bazat pe Python, destinat prezicerii rezultatelor meciurilor de fotbal folosind date istorice. Codul utilizeaza un RandomForestClassifier pentru a antrena un model pe datele despre meciuri si apoi pentru a prezice rezultatele viitoarelor meciuri. Este util pentru analisti sportivi si pentru oricine doreste sa imbunatateasca acuratetea predictiilor privind rezultatele meciurilor de fotbal.</p>
<h1>Caracteristici</h1>
<h3>Procesarea datelor</h2>
<ul>
  <li>Incarcarea datelor despre meciuri dintr-un fisier CSV</li>
  <li>Curatarea datelor si generarea de noi caracteristici, inclusiv codificarea variabilelor categorice, extragerea caracteristicilor din date si ore, si generarea unor noi variabile pe baza acestora</li>
</ul>
<h3>Antrenarea modelului</h3> 
<ul>
  <li>Datele sunt impartite in seturi de antrenament si testare, in functie de data meciurilor</li>
  <li>Se antreneaza un model Random Forest pentru a prezice daca o echipa va castiga un meci pe baza unor factori precum locatia meciului, adversarul, ora si ziua saptamanii</li>
</ul>
<h3>Predictii</h3>
<ul>
  <li>Modelul este utilizat pentru a prezice rezultatele meciurilor din setul de testare</li>
  <li>Precizia predictiilor este calculata folosind metrica accuracy_score</li>
  <li>De asemenea, se calculeaza scorul de precizie (precision_score) pentru a evalua performanta modelului</li>
</ul>
<h3>Analiza avansata</h3>
<ul>
  <li>Se genereaza rolling averages pentru diferite caracteristici ale meciurilor pentru a imbunatati predictiile</li>
  <li>Se prezic rezultatele meciurilor utilizand aceste rolling averages si se evalueaza din nou precizia modelului</li>
  <li>Se combina si se compara predictiile cu rezultatele reale ale meciurilor</li>
</ul>
<h3>Maparea si combinarea datelor</h3>
<ul>
  <li>Se mapeaza denumirile echipelor folosind un dictionar pentru a standardiza numele acestora</li>
  <li>Se combina rezultatele predictiilor pentru echipele oponente pentru a analiza situatiile in care o echipa prezisa sa castige infrunta o echipa prezisa sa piarda</li>
</ul>
