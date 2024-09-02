<h1>Descriere</h1>
<p>Acest proiect este un sistem de recomandare a filmelor, construit utilizand Python si Streamlit. Sistemul analizeaza datele filmelor, calculeaza similaritatile dintre filme si ofera recomandari pe baza unui film selectat de utilizator.</p>
<p>Proiectul include doua fisiere principale:</p>
<p>1. Preprocesare si modelare (tmdb-movies.py)</p>
<p>2. Aplicatia web (app.py)</p>
<h1>Caracteristici</h1>
<h2>1. Preprocesarea si modelarea</h2>
<h3>Incarcarea datelor</h2>
<ul>
  <li>Datele despre filme sunt incarcate dintr-un fisier CSV si sunt afisate informatii de baza despre acestea, cum ar fi primele 5 randuri, descrierea statistica si informatiile despre coloane</li>
</ul>
<h3>Selectia caracteristicilor</h3> 
<ul>
  <li>Din setul de date sunt extrase doar coloanele relevante: "id", "title", "overview", "genre". Se creeaza o noua coloana "tags" prin combinarea coloanelor "overview" și "genre".</li>
</ul>
<h3>Vectorizarea textului</h3>
<ul>
  <li>Textul din coloana tags este vectorizat folosind CountVectorizer cu un maxim de 10.000 de caracteristici, eliminand cuvintele comune din limba engleza</li>
</ul>
<h3>Calculul similaritatii</h3>
<ul>
  <li>Se calculeaza similaritatea dintre filme utilizand similaritatea cosinus</li>
</ul>
<h3>Functia de recomandare</h3>
<ul>
  <li>Se implementeaza o functie pentru a recomanda filme similare cu un film dat</li>
</ul>
<h3>Salvarea modelului</h3>
<ul>
  <li>Modelul si datele procesate sunt salvate folosind "pickle" pentru a fi utilizate ulterior in aplicatia web</li>
</ul>
<h2>2. Aplicatia Web</h2>
<h3>Incarcarea modelului</h3>
<ul>
  <li>Se incarca datele si similaritatile procesate utilizand fisierele salvate cu "pickle"</li>
</ul>
<h3>Interfata cu utilizatorul</h3>
<ul>
  <li>Aplicatia web permite utilizatorilor sa selecteze un film dintr-un dropdown si sa obtina recomandari de filme similare</li>
</ul>
<h3>Afisarea posterelor</h3>
<ul>
  <li>Pentru fiecare film recomandat, aplicatia utilizeaza API-ul The Movie Database (TMDb) pentru a obtine si afisa posterul filmului</li>
</ul>
