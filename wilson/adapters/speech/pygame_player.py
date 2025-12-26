import os
import pygame
import asyncio
from wilson.core.ports.ports import AudioPlayerPort

class PygamePlayerAdapter(AudioPlayerPort):
    def __init__(self):
        pygame.mixer.init()

    async def play_audio(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            return

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
            
        # Optional: cleanup happens in Orchestrator or here?
        # The interface just says play_audio. 
        # Ideally we don't depend on global state, but pygame is global.
        # We'll leave file cleanup to the caller or do it here if we want to be strict.
