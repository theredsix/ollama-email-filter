from pathlib import Path

from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from inbox.listener import InboxListener
from inbox.provider.google import GmailProvider
from inbox.action.spam import SpamClassifyAction


# Use Path to construct a relative path that is independent of the runtime path
credentials_path = Path(__file__).parent / 'etc' / 'google_cred.json'
token_path = Path(__file__).parent / 'etc' / 'token.json'

# Initialize the GmailProvider with the constructed paths
gmail_provider = GmailProvider(
    credentials_path=str(credentials_path),
    token_path=str(token_path),
    scopes=['https://www.googleapis.com/auth/gmail.modify']
)
# Initialize Ollama with JSON output
# chat_model = ChatOllama(model="mistral", temperature=0)
# , stop=["}"])
# chat_model = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key="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", openai_organization="org-ZSwGrvq9TcfGi5YODV17fw3j")

# Initialize the SpamClassifyAction with the GmailProvider and Ollama chat model
spam_classify_action = SpamClassifyAction(provider=gmail_provider)

# Create an InboxListener with the GmailProvider and the SpamClassifyAction
inbox_listener = InboxListener(provider=gmail_provider, actions=[spam_classify_action])

# Start listening for emails to process
inbox_listener.listen()

