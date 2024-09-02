import pandas as pd

data = pd.read_csv('movies.csv')
print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())
print(data.columns)


#Feature Selection
movies = data[['id', 'title', 'overview', 'genre']]
movies['tags'] = movies['overview']+movies['genre']
new_data = movies.drop(columns=['overview', 'genre'])


#Facem detectarea recomandarilor pe baza tagurilor care apar in film
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=10000, stop_words='english') #avem 10000 rows
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray() #convertim valorile din tags in unicode(UTF) pt a putea fi citit is le transformam in vector
print(vector.shape)

#Similaritate intre filme -> prin tags cu genul filmului
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector) #arata similaritatea filmelor

#exemplu
#am nevoie de titlu pe care in accesz prin index
print(new_data[new_data['title']=='The Godfather'].index[0])

#calculam distanta bazata pe similaritate
distance = sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector: vector[1])

#Titlul primelor 5 filme similare cu The Godfather (pe care il luam cu ajutorul indexului)
for i in distance[0:5]:
    print(new_data.iloc[i[0]].title)
    
    
#Functia pentru a obtine titlul fimelor
def recommand(movies):
    index = new_data[new_data['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    for i in distance[0:5]:
        print(new_data.iloc[i[0]].title)
        
recommand("Iron Man")


#Salvam fisierul cu pickle pentru a-l folosi in aplicatia web -> avem nevoie de new_data si similarity
import pickle
pickle.dump(new_data, open('movies_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print(pickle.load(open('movies_list.pkl', 'rb')))


