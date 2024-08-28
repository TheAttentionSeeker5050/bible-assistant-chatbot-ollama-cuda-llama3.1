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

```markdown
Welcome to the Divine Wisdom Chatbot! Ask me anything about your behavior or personal issues.

You: I feel envious of my colleague's success. What should I do?
Bot: I'm so glad you're seeking guidance on this matter!

**1. The Problem:**
Feeling envious of someone else's success is a problematic behavior, my friend. From a biblical perspective, envy is considered a root of all kinds of evil (1 Timothy 6:6-10). When
 we covet what others have, it can lead to bitterness, resentment, and even anger. This negative attitude can poison our relationships, hinder our own growth, and distract us from pursuing God's best for our lives.

**2. Practical Advice:**
To overcome this envy, let's focus on three essential steps:

a) **Reflect on your own values and goals**: Take time to prayerfully assess what truly matters to you. What are your passions? What are your strengths? Focus on developing those qualities, and God will help you find success in His way.

b) **Practice gratitude**: Regularly express thankfulness for the blessings you already have, no matter how small they may seem. A grateful heart is less prone to envy (1 Thessalonians 5:18). Cultivate a mindset that says, "God is good, and I am blessed."

c) **Celebrate others' successes with joy**: When your colleague achieves something remarkable, genuinely rejoice with them! This attitude will help you see that their success doesn't diminish yours. In fact, it can inspire and motivate you to strive for greatness in your own life (Romans 12:15).

**3. Relevant Bible Verses:**

* "For God is not a God of disorder but of peaceâ€”as also in all the congregations of his holy people." (1 Corinthians 14:33) - This verse reminds us that envy can lead to chaos and unrest, while gratitude and joy promote harmony and peace.
* "Do nothing out of selfish ambition or vain conceit. Rather, in humility value others above yourselves..." (Philippians 2:3) - Humility is the antidote to envy. Focus on valuing others and serving with a humble heart.
* "Let your yes be yes and your no be no... Whatever you say or do, say it or do it as those who are under Godâ€™s authority." (James 5:12) - This verse encourages us to maintain integrity in our words and actions. Seek to honor God in all that you do.

Remember, my friend, you are not defined by your envy. You have the power to choose a different path â€“ one of gratitude, humility, and joy. May God's wisdom guide you as you navigate this journey!
```

## Troubleshooting

- **Model Errors**: Ensure that `ollama` and the specified model are correctly installed and accessible. Check the configuration in `config.py`.
- **Output Issues**: If you encounter errors or unexpected output, review the `llm_model.py` script for handling subprocess errors and adjust as needed.
- **Database Issues**: Ensure that `bible.db` is correctly formatted and accessible.