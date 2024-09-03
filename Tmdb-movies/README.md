<h1>Description</h1>
<p>This project is a movie recommendation system, built using Python and Streamlit. The system analyzes movie data, calculates similarities between movies, and provides recommendations based on a user-selected movie.</p>
<p>The project includes two main files:</p>
<p>1. Preprocessing and modeling (tmdb-movies.py)</p>
<p>2. Web application (app.py)</p>
<h1>Features</h1>
<h2>1. Preprocessing and modeling</h2>
<h3>Data loading</h3>
<ul>
  <li>Movie data is loaded from a CSV file, and basic information about the movies is displayed, such as the first 5 rows, statistical description, and column information</li>
</ul>
<h3>Feature selection</h3> 
<ul>
  <li>Only relevant columns are extracted from the dataset: "id", "title", "overview", "genre"</li>
  <li>A new column "tags" is created by combining the "overview" and "genre" columns</li>
</ul>
<h3>Text Vectorization</h3>
<ul>
  <li>The text in the "tags" column is vectorized using CountVectorizer with a maximum of 10,000 features, removing common English words</li>
</ul>
<h3>Similarity calculation</h3>
<ul>
  <li>Similarity between movies is calculated using cosine similarity</li>
</ul>
<h3>Recommendation function</h3>
<ul>
  <li>A function is implemented to recommend movies similar to a given movie</li>
</ul>
<h3>Model saving</h3>
<ul>
  <li>The model and processed data are saved using "pickle" for later use in the web application</li>
</ul>
<h2>2. Web application</h2>
<h3>Loading the model</h3>
<ul>
  <li>The processed data and similarities are loaded using the files saved with "pickle"</li>
</ul>
<h3>User interface</h3>
<ul>
  <li>The web application allows users to select a movie from a dropdown and get recommendations for similar movies</li>
</ul>
<h3>Displaying posters</h3>
<ul>
  <li>For each recommended movie, the application uses The Movie Database (TMDb) API to fetch and display the movie poster</li>
</ul>
