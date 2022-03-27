import os
import spacy
import pandas as pd


def extract_skills(text):

    # initialize spacy model, create document, and tokenize it
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text, disable=['tagger', 'ner', 'lemmatizer'])
    unigrams = [token.text for token in doc if not token.is_stop]

    # load the skills dataframe
    skillset = []
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'skills.csv'))
    skills = list(data.columns.values)

    # loop over all unigrams in the document
    for token in unigrams:
        if token.lower() in skills:
            skillset.append(token)

    # loop over all bigram/trigram noun chunks in the document
    for token in doc.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    # format all skills with proper capitalization
    skillset = [i.capitalize() for i in set([i.lower() for i in skillset])]
    return skillset
