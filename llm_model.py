import subprocess
from config import Config


class LLMModel:
    def __init__(self):
        self.config = Config()

    def generate_response(self, context, question):
        # Refined prompt to ensure structured response
        prompt = f"""
        You are to respond as if you are God providing divine wisdom from the Bible. 
        
        The user may seek grounding, advice, and biblical verses for their query. Address any reprimands or corrections needed, provide helpful advice, and include relevant verses from the Bible.
        
        Address the user's query by following this structured response:
        
        1. Clearly state that the sin or issue mentioned by the user is wrong, explaining why it is considered sinful or problematic from a biblical perspective.
        2. Provide a piece of advice from a divine perspective, offering guidance on how the user might correct their behavior or seek forgiveness.
        3. Cite up to three relevant Bible verses that relate to the sin or issue, ensuring that they are meaningful and supportive of the advice given.

        Context: {context}
        Question: {question}. Please help me.
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
