# AutoGen Poetic AI Assistant

A simple demonstration of Microsoft's AutoGen framework that creates an AI assistant that responds in rhyme using OpenAI's GPT models.

## 🌟 Overview

This project showcases the basic usage of AutoGen (AG2) by implementing a conversational AI agent that:
- Responds to prompts in rhyming verse
- Supports interactive conversations
- Uses OpenAI's GPT models
- Demonstrates basic agent configuration

## 📋 Prerequisites

- Python 3.9-3.13
- OpenAI API key
- Compatible operating system (Windows/Linux/MacOS)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd autogen-poetic-assistant
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Option 1: Set environment variable
     ```bash
     # Windows
     set OPENAI_API_KEY=your-api-key-here
     
     # Linux/MacOS
     export OPENAI_API_KEY=your-api-key-here
     ```
   - Option 2: Uncomment and use the interactive prompt in the code

## 🚀 Running the Code

1. Basic execution:
```bash
python autogen_example.py
```

2. To enable interactive chat:
   - Uncomment the `response.process()` line
   - Run the script and interact with the agent

3. To view chat history:
   - Uncomment the message history section
   - Run the script to see the full conversation log

## 🔧 Customization

You can modify the following parameters in `autogen_example.py`:

- `model`: Change the GPT model (e.g., "gpt-4", "gpt-3.5-turbo")
- `system_message`: Modify the agent's personality/behavior
- `max_turns`: Adjust the conversation length
- `user_input`: Toggle interactive mode

## 📁 Project Structure

```
.
├── README.md
├── requirements.txt
└── autogen_example.py
```

## ⚠️ Important Notes

- Keep your API key secure and never commit it to version control
- The code includes commented sections for additional features
- Python version compatibility is crucial for AutoGen

## 🤝 Contributing

Feel free to:
- Open issues for bugs or suggestions
- Submit pull requests with improvements
- Share your experiences and use cases

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Additional Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
