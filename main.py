# import sqlite3
# from llm_model import LLMModel
# from query_processor import query_database
#
# #
# # class QueryProcessor:
# #     def __init__(self, db_file):
# #         self.db_file = db_file
# #
# #     def find_verses(self, query):
# #         """
# #         Finds verses relevant to the given query from the database.
# #         :param query: The user's query.
# #         :return: A list of relevant verses.
# #         """
# #         # Use the query_database function from query_preprocessor.py to perform the search
# #         results = query_database(query)
# #         return [row[0] for row in results if row]
# #
# #
# # class BookChatbot:
# #     def __init__(self, db_file):
# #         self.query_processor = QueryProcessor(db_file)
# #         self.llm_model = LLMModel()
# #
# #     def respond_to_query(self, question):
# #         verses = self.query_processor.find_verses(question)
# #         if verses:
# #             context = "\n".join(verses)
# #         else:
# #             context = "No relevant verses found."
# #
# #         # Ensure the response aligns with biblical context
# #         response = self.llm_model.generate_response(context, question)
# #         return response
#
#
# def main():
#     db_file = 'bible.db'
#     chatbot = BookChatbot(db_file)
#
#     print("Greetings, child of God. What is your question for divine guidance?")
#
#     while True:
#         user_query = input("> ")
#         if user_query.lower() in ['exit', 'quit']:
#             print("Goodbye!")
#             break
#         try:
#             response = chatbot.respond_to_query(user_query)
#             print("Bot:", response)
#         except Exception as e:
#             print("Bot: Sorry, something went wrong. Please try again.")
#             print(f"Debug Info: {str(e)}")
#
#
# if __name__ == "__main__":
#     main()
