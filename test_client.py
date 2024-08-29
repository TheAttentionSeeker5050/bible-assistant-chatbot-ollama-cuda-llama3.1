import grpc
import chatbot_pb2
import chatbot_pb2_grpc

def run():
    """
    Connects to the gRPC server and sends queries from the user.
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = chatbot_pb2_grpc.ChatbotStub(channel)

    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() in ['exit', 'quit']:
            break

        request = chatbot_pb2.QueryRequest(question=question)
        try:
            response = stub.GetAnswer(request)
            print("Bot:", response.answer)
        except grpc.RpcError as e:
            print(f"Error: {e.details()}")

if __name__ == '__main__':
    run()
