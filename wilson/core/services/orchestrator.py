import os
import asyncio
from wilson.core.ports.ports import LLMPort, TTSPort, AudioPlayerPort, STTPort
from wilson.core.domain.models import Message, AssistantConfig

class Orchestrator:
    def __init__(
        self, 
        llm: LLMPort, 
        tts: TTSPort, 
        player: AudioPlayerPort,
        stt: STTPort,
        config: AssistantConfig
    ):
        self.llm = llm
        self.tts = tts
        self.player = player
        self.stt = stt
        self.config = config
        self.history: list[Message] = []

    async def run_loop(self):
        """Continuous voice loop."""
        while True:
            # Listen
            user_text = await self.stt.listen_and_transcribe()
            
            if not user_text:
                continue
                
            if "exit" in user_text.lower() or "quit" in user_text.lower():
                print("Exiting voice loop.")
                break
                
            await self.process_user_input(user_text)

    async def process_user_input(self, user_text: str):
        print(f"User: {user_text}")
        
        # Add to history
        self.history.append(Message(role="user", content=user_text))
        
        # Generate Response
        ai_response_text = await self.llm.generate_response(
            messages=self.history,
            system_prompt=self.config.system_prompt
        )
        
        print(f"{self.config.name}: {ai_response_text}")
        self.history.append(Message(role="model", content=ai_response_text))
        
        # Turn to speech
        output_file = "response.mp3"
        await self.tts.text_to_speech(
            text=ai_response_text,
            voice=self.config.voice_name,
            output_file=output_file
        )
        
        # Play audio
        await self.player.play_audio(output_file)
        
        # Cleanup
        if os.path.exists(output_file):
            os.remove(output_file)

