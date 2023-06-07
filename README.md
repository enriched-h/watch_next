-Watch_Next

In this code, the watch_next() function takes in the planet_hulk_description parameter, sets up the Spacy model using en_core_web_md, and initializes the
 max_similarity and next_movie variables.

The function then opens the movies.txt file and iterates over the lines of the file. For each line, there is a movie and a movie description, the function extracts 
the description and calculates the similarity between the movie's description and the planet_hulk_description using Spacy's similarity() method. If the similarity score
is higher than the previous highest score, it updates the max_similarity and next_movie variables.

After iterating over all the lines in the file, the function returns the value of next_movie, which should be the title of the most similar movie.

This algorithm can be used to suggest movies to users based on their previously watched movies by finding movies with similar descriptions.
