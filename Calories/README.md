<h1>Descriere</h1>
<p>Acest proiect dezvolta un model de regresie pentru a prezice numarul de calorii arse in functie de diferite caracteristici fizice si activitati de exercitiu. Modelul foloseste XGBoost Regressor, un algoritm de invatare automata puternic si eficient pentru probleme de regresie.</p>
<h1>Caracteristici</h1>
<h3>Colectarea si procesarea datelor</h3>
<ul>
  <li>Datele sunt incarcate din doua fisiere CSV care contin informatii despre exercitii si calorii arse</li>
</ul>
<h3>Analiza datelor</h3> 
<ul>
  <li>Se combina seturile de date si se efectueaza o analiza exploratorie a datelor, inclusiv analiza statistica si vizualizarea distributiilor</li>
</ul>
<h3>Conversia categoriilor textuale</h3>
<ul>
  <li>Se converteste coloana Gender in valori numerice pentru a putea fi utilizata de model</li>
</ul>
<h3>Vizualizarea datelor</h3>
<ul>
  <li>Se folosesc grafice pentru a vizualiza distributiile variabilelor si pentru a analiza corelatiile dintre acestea</li>
</ul>
<h3>Impartirea datelor</h3>
<ul>
  <li>Datele sunt impartite in seturi de antrenament si testare</li>
</ul>
<h3>Antrenarea modelului</h3>
<ul>
  <li>Modelul XGBoost Regressor este antrenat pe datele de antrenament</li>
</ul>
<h3>Evaluarea modelului</h3>
<ul>
  <li>Modelul este evaluat pe setul de date de testare folosind eroarea medie absoluta pentru diferenta medie dintre valorile prezise si cele reale</li>
</ul>
