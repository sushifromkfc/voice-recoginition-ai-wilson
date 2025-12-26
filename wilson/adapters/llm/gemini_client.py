import asyncio
from google.genai import Client
from google.genai.errors import ClientError
from wilson.core.ports.ports import LLMPort
from wilson.core.domain.models import Message

class GeminiAdapter(LLMPort):
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        self.client = Client(api_key=api_key)
        self.model_name = model_name

    async def generate_response(self, messages: list[Message], system_prompt: str) -> str:
        # Construct the full prompt context
        # In a real app we might use specific chat history APIs, but for now we append context
        # or use the 'contents' parameter combined with system instructions if supported better.
        # Here we follow the previous pattern: sending a combined prompt or just the latest with system prompt context.
        
        # Simple implementation: Use the last user message, but prepend system prompt context. 
        # (For true history, we'd need to convert the list of Messages to the API format)
        
        last_user_message = next((m for m in reversed(messages) if m.role == 'user'), None)
        user_input = last_user_message.content if last_user_message else ""
        
        full_contents = f"{system_prompt}\n\nUser: {user_input}"

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_contents
            )
            return response.text
        except ClientError as e:
            if "429" in str(e):
                print("Error: API Rate limit exceeded. Please try again later.")
                return "I apologize, but I am currently overwhelmed with requests. Please try again in a moment."
            else:
                raise
