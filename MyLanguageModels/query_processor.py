import sqlite3
# import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
import string

# Download necessary NLTK data files (you only need to do this once)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt_tab')

# Set of stopwords and punctuation
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)


def preprocess_query(query):
    """
    Preprocesses the user query for better database matching using NLP techniques.

    Parameters:
    query (str): The user's query.

    Returns:
    str: The preprocessed query suitable for SQL LIKE queries.
    """
    # Tokenize the query
    tokens = word_tokenize(query.lower())

    # Remove stop words and punctuation
    filtered_tokens = [token for token in tokens if token not in stop_words and token not in punctuation]

    # Join tokens into a single string
    preprocessed_query = ' '.join(filtered_tokens)

    return preprocessed_query


def get_synonyms(word):
    """
    Returns a list of synonyms for a given word using WordNet.

    Parameters:
    word (str): The word to find synonyms for.

    Returns:
    list: A list of synonyms.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)


def expand_query_with_synonyms(query):
    """
    Expands the user query to include synonyms for better matching in the database.

    Parameters:
    query (str): The user's query to be expanded.

    Returns:
    str: The expanded query with synonyms.
    """
    tokens = word_tokenize(query.lower())
    expanded_tokens = []

    for token in tokens:
        # Add the original token
        expanded_tokens.append(token)
        # Add synonyms
        synonyms = get_synonyms(token)
        expanded_tokens.extend(synonyms)

    # Remove duplicates and punctuation
    expanded_tokens = [token for token in expanded_tokens if token not in stop_words and token not in punctuation]

    # Join tokens into a single string
    expanded_query = ' '.join(expanded_tokens)

    return expanded_query


def transform_query_for_db(query):
    """
    Transforms the user query into a format suitable for SQL LIKE queries, including synonyms.

    Parameters:
    query (str): The user's query to be transformed.

    Returns:
    str: The transformed query suitable for SQL LIKE queries.
    """
    # Preprocess the query
    preprocessed_query = preprocess_query(query)

    # Expand query with synonyms
    expanded_query = expand_query_with_synonyms(preprocessed_query)

    # Escape special characters and add wildcards
    transformed_query = expanded_query.replace("'", "''")
    transformed_query = f"%{transformed_query}%"

    return transformed_query


def query_database(query):
    """
    Queries the database using the transformed query.

    Parameters:
    query (str): The user's query to be used for searching the database.

    Returns:
    list: A list of results matching the query.
    """
    db_path = '../bible.db'
    transformed_query = transform_query_for_db(query)
    results = []

    try:
        # Connect to the database
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            # Query the database
            cursor.execute("SELECT * FROM bible WHERE verse LIKE ?", (transformed_query,))
            results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    return results

def is_denial(response):
    """
    Checks if the response is a denial based on specific keywords.
    If the response is longer than 7 lines, it is considered non-denial automatically.

    Parameters:
    response (str): The text response from the model.

    Returns:
    bool: True if the response is a denial, False otherwise.
    """
    denial_keywords = ["deny", "unable to assist", "cannot help", "no answer", "not applicable"]
    return any(keyword in response.lower() for keyword in denial_keywords)