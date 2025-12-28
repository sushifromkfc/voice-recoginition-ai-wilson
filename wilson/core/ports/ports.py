from abc import ABC, abstractmethod
from typing import AsyncGenerator, Optional
from wilson.core.domain.models import Message

class LLMPort(ABC):
    @abstractmethod
    async def generate_response(self, messages: list[Message], system_prompt: str) -> str:
        pass

class STTPort(ABC):
    @abstractmethod
    async def listen_and_transcribe(self) -> str:
        """Listens to microphone input and returns transcribed text."""
        pass

class TTSPort(ABC):
    @abstractmethod
    async def text_to_speech(self, text: str, voice: str, output_file: str) -> None:
        pass

class AudioPlayerPort(ABC):
    @abstractmethod
    async def play_audio(self, file_path: str) -> None:
        pass
