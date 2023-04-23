import spacy

nlp = spacy.load('en_core_web_md')
planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


def watch_next(planet_hulk_description):
    max_similarity = 0
    next_movie = ""

    model_sentence = nlp(planet_hulk_description)

    with open('movies.txt', 'r') as file:
         for line in file:
             fields = line.strip().split(" ")
             line_description = " ".join(fields[2:])

             similarity = nlp(line_description).similarity(model_sentence)
             if similarity > max_similarity:
                 max_similarity = similarity
                 next_movie = " ".join(fields[0:2])

    return next_movie
