<h1>Descriere</h1>
<p>Acest proiect utilizeaza datele istorice ale indicelui S&P 500 pentru a construi un model de invatare automata care prezice daca pretul de inchidere al zilei urmatoare va fi mai mare decat pretul de inchidere al zilei curente. Modelul foloseste RandomForestClassifier pentru a face aceste previziuni si include o analiza de backtesting pentru evaluarea performantei modelului.</p>
<h1>Caracteristici</h1>
<h3>Colectarea Datelor</h3>
<ul>
  <li>Datele sunt colectate folosind yfinance pentru a obtine istoricul preturilor S&P 500</li>
</ul>
<h3>Curatarea si vizualizarea datelor</h3> 
<ul>
  <li>Datele sunt curatate prin eliminarea coloanelor irelevante si vizualizate pentru a intelege distributia preturilor si alte caracteristici</li>
</ul>
<h3>Crearea "Traget" pentru invatarea automata</h3>
<ul>
  <li>Se creează o coloană "Target" care indica daca pretul de inchidere al zilei urmatoare este mai mare decat cel al zilei curente</li>
</ul>
<h3>Antrenarea modelului</h3>
<ul>
  <li>Se antreneaza un model RandomForestClassifier pe datele istorice, folosind datele de inchidere si volumele de tranzactionare ca predictori</li>
</ul>
<h3>Evaluarea Modelului</h3>
<ul>
  <li>Se evalueaza performanta modelului folosind "precision_score" pe setul de date de testare</li>
  <li>Se efectueaza backtesting pentru a evalua performanta modelului in timp</li>
</ul>
<h3>Adaugare predictori suplimentari</h3>
<ul>
  <li>Se adauga noi predictori bazati pe rolling averages pentru a imbunatati modelul</li>
</ul>
<h3>Imbunatatirea modelului</h3>
<ul>
  <li>Se reface modelul folosind noi predictori si probabilitati in loc de valori discrete pentru a face previziuni mai precise</li>
</ul>
