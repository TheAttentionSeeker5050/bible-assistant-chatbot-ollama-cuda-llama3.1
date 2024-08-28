# Divine Wisdom Chatbot: A Bible Assistant Using Python, Ollama3.1, Langchain


## Overview

The Divine Wisdom Chatbot is a Python-based application designed to offer spiritual guidance, advice, and support from a biblical perspective. This chatbot utilizes natural language processing (NLP) to enhance query matching and integrates with the Llama 3.1 model from Ollama to provide thoughtful responses based on Bible verses.

## Features

1. **Spiritual Guidance**: Offers insights and explanations on behavioral issues and moral dilemmas from a spiritual perspective.
2. **Practical Advice**: Provides actionable advice on personal development, forgiveness, and self-improvement.
3. **Bible Verses**: Cites up to three relevant Bible verses that align with the guidance provided.
4. **NLP Query Processing**: Uses NLTK for preprocessing queries to include synonyms and relevant terms for more accurate database matching.

## Components

- **`config.py`**: Contains configuration settings, including the model name.
- **`query_processor.py`**: Handles NLP preprocessing of user queries and transforms them for SQL database searches.
- **`llm_model.py`**: Interacts with the Llama 3.1 model to generate responses based on user input.
- **`main.py`**: Main script that integrates all components and facilitates user interaction.
- **`bible.db`**: SQLite database containing the Bible verses.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/TheAttentionSeeker5050/bible-assistant-chatbot-ollama-cuda-llama3.1
   cd bible-assistant-chatbot-ollama-cuda-llama3.1
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Make sure you have `ollama` installed and properly configured. You can install other required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```


4. **Install NLTK Data**

Run the following Python script to download the necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
```

5. **Install Ollama**

   Follow the installation instructions for Ollama, available at [Ollama Installation Guide](https://ollama.com/docs/installation).

6. **Pull Llama3.1**

   To pull and use the Llama3.1 model, follow the instructions on [Llama3.1 Model Guide](https://huggingface.co/models) or the Ollama documentation.

7. **Install CUDA**

   Follow the official [CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/) to install CUDA and ensure it is compatible with your GPU and system.

## Tested Hardware

This program has been tested with an Nvidia RTX 4060 graphics card.

## Usage

1. **Run the Chatbot**

To start the chatbot, execute the main script:

```bash
python main.py
```

2. **Interact with the Chatbot**

Follow the on-screen prompts to interact with the chatbot. Ask questions about personal issues, and the chatbot will provide biblical advice, reprimands, and relevant verses.

## Example Interaction

```
Welcome to the Divine Wisdom Chatbot! Ask me anything about your behavior or personal issues.

You: I feel envious of my colleague's success. What should I do?
Bot: My child, envy is a weighty sin that can lead you down a path of darkness and discontentment. It is wrong to covet another person's success or possessions, for it is rooted in pride and a lack of trust in God's provision for your own life (Proverbs 28:22).

Recognize that jealousy can consume your thoughts and actions, causing you to behave in ways that are contrary to God's will. It can lead you to compare yourself unfavorably with others, forget the blessings He has given you, and become envious of those who seem to have more (James 4:1-3).

To correct this behavior, I advise you to examine your heart and acknowledge before Me any feelings of resentment or bitterness towards your colleague's success. Recognize that their achievement is not a reflection of your worth, but rather a demonstration of God's goodness and faithfulness in their life.

Adopt an attitude of humility and gratitude by focusing on the blessings He has given you. Seek to understand the value of the gifts and opportunities He has provided for you, even if they differ from those of others (1 Timothy 6:6-8).

Here are three relevant Bible verses that can guide you in this journey:

1. "Pride goes before destruction, a haughty spirit before a fall." - Proverbs 16:18
2. "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God." - Philippians 4:6
3. "For we brought nothing into the world, and we can take nothing out of it. But if you have a mind that is any value at all, then use it well. As for me, my child, I will now leave this matter with you, in the hands of the Lord." - 1 Timothy 6:7-10
```

## Troubleshooting

- **Model Errors**: Ensure that `ollama` and the specified model are correctly installed and accessible. Check the configuration in `config.py`.
- **Output Issues**: If you encounter errors or unexpected output, review the `llm_model.py` script for handling subprocess errors and adjust as needed.
- **Database Issues**: Ensure that `bible.db` is correctly formatted and accessible.