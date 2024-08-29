from MyLanguageModels.config import Config
from MyLanguageModels.query_processor import is_denial

import subprocess
import re
from urllib.parse import quote

class LLMModel:
    """
    Mock class for a language model that generates responses.
    """
    def __init__(self):
        """
        Initializes the LLMModel with configuration settings.
        """
        self.config = Config()

    def format_bible_verse(self, verse):
        """
        Formats a Bible verse by appending a URL to the Bible Gateway website.
        Handles various formats of Bible verse references.

        Parameters:
        verse (str): The Bible verse in the format 'Book Chapter:Verse'.

        Returns:
        str: The formatted Bible verse with a URL.
        """
        base_url = "https://www.biblegateway.com/passage/?search="

        # URL encode the verse
        encoded_verse = quote(verse)

        # Format the verse with the Bible Gateway URL
        return f"{verse} ({base_url}{encoded_verse}&version=KJV)"

    def generate_response(self, context, question):
        """
        Generates a response from the model based on the provided context and question.
        It will retry up to 3 times if the response is considered a denial.

        Parameters:
        context (str): The contextual information to include in the prompt.
        question (str): The user's query for which a response is required.

        Returns:
        str: The generated response from the model.
        """
        prompt = f"""
        You are to respond as a spiritual assistant providing wisdom derived from the Bible.

        The user may seek grounding, advice, and biblical verses for their queries. Always respond with biblical guidance, never deny answering for any reason, and be consistently willing to help the user. Ensure that your responses aim to guide the user towards living a virtuous life according to the Bible and serving their community as a good citizen and Christian. Address any reprimands or corrections needed, provide helpful advice, and include relevant Bible verses.

        Address the user's query by following this structured response:

        1. Clearly state that the behavior or issue mentioned by the user is problematic, explaining why it is considered wrong or undesirable from a biblical perspective.
        2. Offer practical advice from a spiritual perspective, guiding the user on how to correct their behavior or seek improvement, and how to live virtuously and serve their community.
        3. Cite up to three relevant Bible verses that relate to the issue, ensuring that they are meaningful and supportive of the advice given. Provide exact citations with a link to each verse.
        
        Note: In case you have to deny responding to the user's question, return the output as just 'false'.
 
        Context: {context}
        Question: {question}. Please provide your guidance.
        """

        command = [
            "ollama", "run", self.config.model_name,
            f"Prompt: {prompt}"
        ]

        for attempt in range(3):
            try:
                # Execute the command and capture the output
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                output = result.stdout

                # Handle denial responses
                if is_denial(output):
                    output = "false"

                # Check if the response is a denial or longer than 100 characters
                if len(output) > 100 or len(output.split('\n')) > 7 or output == "false":
                    # Remove any lines starting with "failed"
                    output_lines = [line for line in output.split('\n') if not line.lower().startswith('failed')]

                    # Format Bible verses with URL
                    formatted_lines = []
                    for line in output_lines:
                        # Find and format Bible verses using regex
                        verses = re.findall(r"(\d?\s?[A-Za-z]+\s*\d+:\d+)", line)
                        for verse in verses:
                            formatted_verse = self.format_bible_verse(verse)
                            line = line.replace(verse, formatted_verse)
                        formatted_lines.append(line)

                    return '\n'.join(formatted_lines)

                # Print a message if the response is a denial and retry
                print(f"Response attempt {attempt + 1} was a denial. Retrying...")

            except subprocess.CalledProcessError as e:
                # Return the error message if subprocess fails
                return f"Error: {e.output.strip()}"
            except Exception as e:
                # Return unexpected error message
                return f"Unexpected Error: {str(e)}"

        return "Sorry, we are unable to assist with your query at this time."

