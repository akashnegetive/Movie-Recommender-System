# Project: Movie Recommender System Using Machine Learning!

<img src="demo/4.png" alt="workflow" width="60%">

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# Types of Recommendation System :

<img src="demo/5.png" alt="workflow" width="70%">

### 1 ) Content Based :

- Content-based systems, which use characteristic information and takes item attriubutes into consideration .

- Twitter , Youtube .

- Which music you are listening , what singer are you watching . Form embeddings for the features .
	
- User specific actions or similar items reccomendation .
	
- It will create a vector of it .
	
- These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future
	
- One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).

### 2 ) Collaborative Based :
		
- Collaborative filtering systems, which are based on user-item interactions.
	
- Clusters of users with same ratings , similar users .
	
- Book recommendation , so use cluster mechanism .
	
- We take only one parameter , ratings or comments .
	
- In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in the second item . 
	
- Issues are :

	- User-Item nXn matrix , so computationally expensive .

	- Only famous items will get reccomended .

	- New items might not get reccomended at all .   

### 3 ) Hybrid Based :
	
- Hybrid systems, which combine both types of information with the aim of avoiding problems that are generated when working with just one kind.

- Combination of both and used now a days .

- Uses : word2vec , embedding .           

## Dataset

The dataset used for this project contains information about movies, including their titles and IDs. It is processed and stored in `movie_data.pkl`. The dataset is used to calculate the cosine similarity between movies.
* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Model

The model for recommending movies is based on cosine similarity. Cosine similarity is used to measure the similarity between movie titles. The model computes the similarity scores and suggests the top 10 similar movies based on the selected movie title.


## Difference Between Euclidean Distance and Cosine Similarity

<img width="400" height="215" alt="image" src="https://github.com/user-attachments/assets/09e2f6ad-7a26-4e8b-9c71-03353d404caa" />

-Euclidean: Best for numeric, dense, or continuous data
                    (e.g., user ratings, spatial coordinates).
-Cosine: Best for textual, sparse, or high-dimensional data
              (e.g., NLP vectors, TF-IDF, CountVectorizer).

-Euclidean: Ranges from 0 → ∞ (distance).
-Cosine: Ranges from –1 → +1

<img width="400" height="111" alt="image" src="https://github.com/user-attachments/assets/f18ed1e0-f7ab-4db3-9301-e8f0aad41cf5" />


## Compare Cosine Vs Euclidean 

<img width="400" height="742" alt="image" src="https://github.com/user-attachments/assets/c4d6c303-c604-462d-9f91-72181370ad49" />


## Concept used to build the model.pkl file : cosine_similarity

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://www.learndatasci.com/glossary/cosine-similarity/

## Results

The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.

## Website Link   [🔗](https://movie-recommender-system-akash.streamlit.app/)

<img src="demo/1.png" alt="workflow" width="70%">

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">

# Thanks Watching !!

