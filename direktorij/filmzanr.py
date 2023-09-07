import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# Priprema podataka
descriptions = [
    "Ovo je film o obiteljskim odnosima i emocijama. Dramski film ispunjen je preokretima, lažima, spletkama te vrlo dramatičnim scenama. Likovi dolaze u sukobe, što daje dramatičan ton filmu jer gledatelj ne zna što očekivati, bili to sukobi u obiteljskim odnosima, ljubavnim odnosima ili prijateljskim odnosima.",
    "Grupa hrabrih junaka bori se protiv zločina u ovom akcijskom filmu, ispunjen je borbom, ratom, borilačkim vještinama, eksplozijama te raznim automobilskim potjerama prilikom hvatanja zločinaca. U ovakvom filmu često se pojavljuju špijuni, brojni likovi su naoružani te je u pitanju uglavnom borba za život",
    "Smijeh ne prestaje u ovoj urnebesnoj komediji, svi likovi su komični, u komičnom filmu prevladava humor te brojne neobične situacije koje dovode do urnebesnih prizora. Ovakav film uglavnom ima sretan kraj",
    "Putujte u svemir i otkrijte tajne izvanzemaljskog života u ovom znanstveno-fantastičnom filmu, u ovakvom film prevladava napredna tehnologija, često se pojavljuju brojna izmišljena stvorenja koja žive u nestvarnom svijetu. Često se pojavčjuje i putovanje kroz vrijeme, viljenjaci, superheroji, čudovišta, magija, hobiti, patuljci, zombiji i slično ",
    "Proživite sve zaplete u ljubavnoj priči dvoje zaljubljenih ljudi punoj emocija.Ljubavni film karakterizira sreća i zaljubljenost između dvoje ljudi, često je u pitanju i ljubav na prvi pogled, postoje i mnoge nesretne ljubavi i isto tako i neočekivane ljubavi. Film uglavnom prati napredovanje odnosa iz prijateljstva koje vodi do ljubavne veze i na koncu brak. ",
    "Slijedite dječje heroje u njihovim avanturama na putu do ostvarenja snova. Animirani filmovi prikazuju pustolovine mladih heroja, ispunjen je zabavom i srećom te likovima poput princeza, sirena, prinčeva, životinja koje pričaju. Animirani film uglavnom je sretan i veseo kroz cijelu radnju"
]
genres = ['drama', 'akcija', 'komedija', 'znanstvena fantastika', 'ljubavni', 'animirani film']

#def evaluate_model():
#    y_true = genres
#    y_pred = mlp_model.predict(X)
#    accuracy = accuracy_score(y_true, y_pred)
#    report = classification_report(y_true, y_pred, target_names=genres)
#    confusion = confusion_matrix(y_true, y_pred, labels=genres)
#   
#    st.write("Točnost modela: {:.2f}".format(accuracy))
#    st.write("Izvještaj klasifikacije:\n", report)
#    st.write("Matrica zabune:\n", confusion)

# Vektorizacija opisa filma
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(descriptions)

# Inicijalizacija i treniranje MLP modela
mlp_model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=100, random_state=42)
mlp_model.fit(X, genres)

# Funkcija za predviđanje žanra
def predict_genre(description):
    vectorized_description = vectorize_description(description)
    predicted_genre = mlp_model.predict(vectorized_description)[0]

    # Prikazivanje ključnih riječi za predviđeni žanr
    genre_keywords = keywords[predicted_genre]
    st.write("Ključne riječi za žanr {}: {}".format(predicted_genre, ", ".join(genre_keywords)))
    return predicted_genre




# Definicija ključnih riječi za svaki žanr
keywords = {
    'drama': ['obiteljski odnosi', 'ljubavni odnosi', 'spletke', 'laži', 'preokret' 'dramatičan ton'],
    'akcija': ['hrabri', 'zločin', 'junak', 'zatvor', 'borilačke vještine', 'rat', 'eksplozija', 'borba za život', 'hvatanje zločinaca'],
    'komedija': ['smijeh', 'urnebesno', 'zabava', 'ironija', 'prijatelji', 'sretan kraj','komično'],
    'znanstvena fantastika': ['hobiti','vilenjaci', 'izvanzemaljci', 'napredna tehnologija', 'svemir', 'putovanje kroz vrijeme', 'superjunaci'],
    'ljubavni': ['ljubav', 'zaplet', 'zaljubljen', 'sreća', 'ljubavna veza', 'brak', 'emocije', 'ljubav na prvi pogled'],
    'animirani film': ['dječji', 'likovi', 'avantura', 'snovi', 'pustolovina', 'princeze', 'sirene', 'životinje koje pričaju']
}

# Funkcija za vektorizaciju opisa filma
def vectorize_description(description):
    return vectorizer.transform([description])


#softmax izlaz 
def predict_genre(description):
    vectorized_description = vectorize_description(description)
    predicted_probabilities = mlp_model.predict_proba(vectorized_description)[0]

    # Prikazivanje kategorija s postotcima
    category_probabilities = zip(genres, predicted_probabilities)
    sorted_categories = sorted(category_probabilities, key=lambda x: x[1], reverse=True)
    
    for category, probability in sorted_categories[:3]:  # Prikazi tri najvjerojatnije kategorije
        st.write("Kategorija: {}, Vjerojatnost: {:.2f}%".format(category, probability * 100))

    return sorted_categories[0][0]  # Vrati najvjerojatniju kategoriju



# Streamlit aplikacija
st.title("Predviđanje žanra filma")
description = st.text_area("Unesite opis filma:")
if st.button("Predviđanje"):
    predicted_genre = predict_genre(description)
    

    
