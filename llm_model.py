import subprocess
from config import Config


class LLMModel:
    def __init__(self):
        self.config = Config()

    def generate_response(self, context, question):

        # Refined prompt to ensure structured response
        prompt = f"""
        You are to respond as a spiritual assistant providing wisdom derived from the Bible.
        
        The user may seek grounding, advice, and biblical verses for their queries. Address any reprimands or corrections needed, provide helpful advice, and include relevant Bible verses.
        
        Address the user's query by following this structured response:
        
        1. Clearly state that the behavior or issue mentioned by the user is problematic, explaining why it is considered wrong or undesirable from a biblical perspective.
        2. Offer practical advice from a spiritual perspective, guiding the user on how to correct their behavior or seek improvement.
        3. Cite up to three relevant Bible verses that relate to the issue, ensuring that they are meaningful and supportive of the advice given.
        
        Context: {context}
        Question: {question}. Please provide your guidance.
        """

        command = [
            "ollama", "run", self.config.model_name,
            f"Prompt: {prompt}"
        ]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            # Remove any lines starting with "failed"
            output_lines = [line for line in result.stdout.split('\n') if not line.lower().startswith('failed')]
            return '\n'.join(output_lines)
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output.strip()}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"
