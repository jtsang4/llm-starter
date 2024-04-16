import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langfuse.callback import CallbackHandler

load_dotenv(verbose=True, override=True)

llm = ChatOpenAI(model="claude-3-haiku")

langfuse_handler = CallbackHandler(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

# Your Langchain code

# Add Langfuse handler as callback (classic and LCEL)
# chain.invoke({"input": "<user_input>"}, config={"callbacks": [langfuse_handler]})

print(
    llm.invoke(
        "how can langsmith help with testing?", config={"callbacks": [langfuse_handler]}
    ),
)
