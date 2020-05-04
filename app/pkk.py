def genre_classifier(t):
    import pandas as pd
    import numpy as np
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pickle

    classifier_f = open("Drama.pickle", "rb")
    Drama = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Comedy.pickle", "rb")
    Comedy = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Adventure.pickle", "rb")
    Adventure = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("History.pickle", "rb")
    History = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("War.pickle", "rb")
    War = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Thriller.pickle", "rb")
    Thriller = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Crime.pickle", "rb")
    Crime = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Fantasy.pickle", "rb")
    Fantasy = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Horror.pickle", "rb")
    Horror = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Family.pickle", "rb")
    Family = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Documentary.pickle", "rb")
    Documentary = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Mystery.pickle", "rb")
    Mystery = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Romance.pickle", "rb")
    Romance = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("ScienceFiction.pickle", "rb")
    ScienceFiction = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("Action.pickle", "rb")
    Action = pickle.load(classifier_f)
    classifier_f.close()

    ##
    classifier_f = open("tfidf1.pickle", "rb")
    tfidf1 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf2.pickle", "rb")
    tfidf2 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf3.pickle", "rb")
    tfidf3 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf4.pickle", "rb")
    tfidf4 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf5.pickle", "rb")
    tfidf5 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf6.pickle", "rb")
    tfidf6 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf7.pickle", "rb")
    tfidf7 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf8.pickle", "rb")
    tfidf8 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf9.pickle", "rb")
    tfidf9 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf10.pickle", "rb")
    tfidf10 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf11.pickle", "rb")
    tfidf11 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf12.pickle", "rb")
    tfidf12 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf13.pickle", "rb")
    tfidf13 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf14.pickle", "rb")
    tfidf14 = pickle.load(classifier_f)
    classifier_f.close()

    classifier_f = open("tfidf15.pickle", "rb")
    tfidf15 = pickle.load(classifier_f)
    classifier_f.close()

    ##############

    t = np.array(t).reshape(-1,1)

    genre_ans = []

    #Drama_genre
    t1 = tfidf1.transform(t[0])
    if (Drama.predict(t1)[0]==1):
        genre_ans.append("Drama")

    #Comedy_genre
    t2 = tfidf2.transform(t[0])
    if (Comedy.predict(t2)[0]==1):
        genre_ans.append("Comedy")

    #Adventure_genre
    t3 = tfidf3.transform(t[0])
    if (Adventure.predict(t3)[0]==1):
        genre_ans.append("Adventure")

    #History_genre
    t4 = tfidf4.transform(t[0])
    if (History.predict(t4)[0]==1):
        genre_ans.append("History")

    #War_genre
    t5 = tfidf5.transform(t[0])
    if (War.predict(t5)[0]==1):
        genre_ans.append("War")

    #Thriller_genre
    t6 = tfidf6.transform(t[0])
    if (Thriller.predict(t6)[0]==1):
        genre_ans.append("Thriller")

    #Crime_genre
    t7 = tfidf7.transform(t[0])
    if (Crime.predict(t7)[0]==1):
        genre_ans.append("Crime")

    #Fantasy_genre
    t8 = tfidf8.transform(t[0])
    if (Fantasy.predict(t8)[0]==1):
        genre_ans.append("Fantasy")

    #Horror_genre
    t9 = tfidf9.transform(t[0])
    if (Horror.predict(t9)[0]==1):
        genre_ans.append("Horror")

    #Family_genre
    t10 = tfidf10.transform(t[0])
    if (Family.predict(t10)[0]==1):
        genre_ans.append("Family")

    #Documentary_genre
    t11 = tfidf11.transform(t[0])
    if (Documentary.predict(t11)[0]==1):
        genre_ans.append("Documentary")

    #Mystery_genre
    t12 = tfidf12.transform(t[0])
    if (Mystery.predict(t12)[0]==1):
        genre_ans.append("Mystery")

    #Romance_genre
    t13 = tfidf13.transform(t[0])
    if (Romance.predict(t13)[0]==1):
        genre_ans.append("Romance")

    #ScienceFiction_genre
    t14 = tfidf14.transform(t[0])
    if (ScienceFiction.predict(t14)[0]==1):
        genre_ans.append("Science Fiction")

    #Action_genre
    t15 = tfidf15.transform(t[0])
    if (Action.predict(t15)[0]==1):
        genre_ans.append("Action")
        
    return(genre_ans)

############################

def ner():
    import spacy 

    nlp = spacy.load('en_core_web_sm') 
    doc = nlp(sentence)

    from collections import defaultdict

    groups = defaultdict(list)

    for element in doc.ents: 
        groups[element.label_].append(element)

    ans = []
    ans.append(groups['PERSON'])
    ans.append(groups['GPE'])
    return ans




