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


#We detect the recommendations based on the tags that appear in the film
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=10000, stop_words='english') #i have 10000 rows
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray() #convert the values ​​from the tags into unicode (UTF) so that they can be read and transformed into a vector
print(vector.shape)

#Similarity between films -> by tags with the genre of the film
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector) #arata similaritatea filmelor

#exemple
#I need a title that I can access through the index
print(new_data[new_data['title']=='The Godfather'].index[0])

#calculate the distance based on similarity
distance = sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector: vector[1])

#The title of the first 5 films similar to The Godfather (which we take with the help of the index)
for i in distance[0:5]:
    print(new_data.iloc[i[0]].title)
    
    
#Function to obtain the title of the films
def recommand(movies):
    index = new_data[new_data['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    for i in distance[0:5]:
        print(new_data.iloc[i[0]].title)
        
recommand("Iron Man")


#Save the file with pickle to use it in the web application -> we need new_data and similarity
import pickle
pickle.dump(new_data, open('movies_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print(pickle.load(open('movies_list.pkl', 'rb')))


