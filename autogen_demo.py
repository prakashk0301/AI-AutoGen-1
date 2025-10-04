"""
AutoGen Demo Script
------------------
Requirements:
- Python 3.9-3.13
- OpenAI API key
- Dependencies from requirements.txt
"""

# Import required libraries
from autogen import LLMConfig, ConversableAgent
import os
import getpass

def main():
    """Main function to demonstrate AutoGen capabilities"""
    
    # Step 1: API Key Setup
    # ---------------------
    # Uncomment below to set API key manually
    # if not os.environ.get("OPENAI_API_KEY"):
    #     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")
    
    # Step 2: LLM Configuration
    # ------------------------
    llm_config = LLMConfig(
        api_type="openai",         # Provider type
        model="gpt-4o-mini"        # Model name
        # Additional optional parameters:
        # temperature=0.7,         # Controls randomness (0.0-1.0)
        # max_tokens=150,          # Maximum length of response
        # top_p=0.9,              # Nucleus sampling parameter
    )
    
    # Step 3: Create AI Agent
    # ----------------------
    with llm_config:
        poetic_agent = ConversableAgent(
            name="poetic_agent",
            system_message="You are a poetic AI assistant. Respond in rhyme."
            # Additional optional parameters:
            # human_input_mode="NEVER",  # NEVER, TERMINATE, or ALWAYS
            # code_execution_config={"work_dir": "workspace"},
            # max_consecutive_auto_reply=3
        )
    
    # Step 4: Initialize Conversation
    # -----------------------------
    response = poetic_agent.run(
        message="In one sentence, what's the big deal about AI?",
        max_turns=3,              # Maximum conversation turns
        user_input=True           # Enable interactive input
        # Additional optional parameters:
        # raise_on_error=True,    # Raise exceptions on errors
        # silent=False            # Suppress console output
    )
    
    # Step 5: Process Conversation
    # --------------------------
    # Uncomment to enable interactive chat
    # response.process()
    
    # Step 6: Display Chat History
    # --------------------------
    # Uncomment to see conversation history
    # for i, msg in enumerate(response.messages):
    #     speaker = msg["name"]
    #     content = msg["content"]
    #     print(f"--- Turn {i+1} ---")
    #     print(f"{speaker}: {content}\n")

if __name__ == "__main__":
    # Execute only if run as a script
    main()

"""
Additional Configuration Options:
-------------------------------
# Custom LLM Provider Setup
# llm_config = LLMConfig(
#     api_type="azure",
#     api_base="https://your-endpoint.openai.azure.com",
#     api_version="2023-07-01-preview"
# )

# Custom Agent Configuration
# agent_config = {
#     "temperature": 0.7,
#     "max_tokens": 150,
#     "top_p": 0.9,
#     "frequency_penalty": 0.0,
#     "presence_penalty": 0.0
# }

# Error Handling Example
# try:
#     response = poetic_agent.run(message="Hello")
#     response.process()
# except Exception as e:
#     print(f"Error: {e}")
"""
