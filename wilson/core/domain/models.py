from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Message:
    role: str
    content: str
    
@dataclass
class AssistantConfig:
    name: str = "W.I.L.S.O.N."
    system_prompt: str = ""
    voice_name: str = "en-GB-RyanNeural"
