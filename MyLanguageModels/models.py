from MyLanguageModels.llm_model import LLMModel
from MyLanguageModels.query_processor import query_database

class QueryProcessor:
    """
    Processes queries to find relevant verses from the database.
    """
    def __init__(self, db_file):
        """
        Initializes the query processor with a database file.
        :param db_file: The path to the database file.
        """
        self.db_file = db_file

    def find_verses(self, query):
        """
        Finds verses relevant to the given query from the database.
        :param query: The user's query.
        :return: A list of relevant verses.
        """
        # Use the query_database function from query_preprocessor.py to perform the search
        results = query_database(query)
        return [row[0] for row in results if row]


class BookChatbot:
    """
    Main chatbot class that uses a query processor and a language model.
    """
    def __init__(self, db_file):
        """
        Initializes the chatbot with a query processor and a language model.
        :param db_file: The path to the database file.
        """
        self.query_processor = QueryProcessor(db_file)
        self.llm_model = LLMModel()

    def respond_to_query(self, question):
        """
        Responds to a user's question using the query processor and language model.
        :param question: The user's question.
        :return: The chatbot's response.
        """
        verses = self.query_processor.find_verses(question)
        if verses:
            context = "\n".join(verses)
        else:
            context = "No relevant verses found."

        # Ensure the response aligns with biblical context
        response = self.llm_model.generate_response(context, question)
        return response
