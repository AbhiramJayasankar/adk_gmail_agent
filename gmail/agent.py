from google.adk.agents import Agent
from gmail.gmail_tool import get_latest_emails
from gmail.search_tool import search_emails
from gmail.attachment_tool import download_email_attachments

agent_instruction = """
You are an assistant that can help manage a user's Gmail inbox.

You have two tools available:
- `get_latest_email`: Use this when the user asks for their most recent email.
- `search_emails`: Use this when the user wants to find specific emails. You will need to ask them for a search query, like 'from:amazon' or 'subject:receipt'.
"""

root_agent = Agent(
    model="gemini-2.5-flash",
    name="email_agent",
    description="A helpful assistant for managing Gmail. It can retrieve the most recent email and perform searches using keywords, senders, or subjects to find specific messages. It can also download all attachments from an email and return localhost download links.",
    instruction=agent_instruction,
    tools=[
        get_latest_emails,
        search_emails,
        download_email_attachments
    ],
)