import grpc
from concurrent import futures
import chatbot_pb2
import chatbot_pb2_grpc
from MyLanguageModels.models import BookChatbot  # Import from your model.py

class ChatbotServicer(chatbot_pb2_grpc.ChatbotServicer):
    """
    Implements the Chatbot service defined in the .proto file.
    """
    def __init__(self, db_file):
        """
        Initializes the service with a database file.
        :param db_file: The path to the database file.
        """
        self.chatbot = BookChatbot(db_file)

    def GetAnswer(self, request, context):
        """
        Handles the GetAnswer RPC call.
        :param request: The QueryRequest containing the user's question.
        :param context: The gRPC context for the call.
        :return: A QueryResponse containing the chatbot's answer.
        """
        try:
            question = request.question
            response = self.chatbot.respond_to_query(question)
            return chatbot_pb2.QueryResponse(answer=response)
        except Exception as e:
            return chatbot_pb2.QueryResponse(answer=f"Sorry, something went wrong. Please try again. Debug Info: {str(e)}")

def serve():
    """
    Starts the gRPC server and listens for incoming requests.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatbotServicer_to_server(ChatbotServicer('bible.db'), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
