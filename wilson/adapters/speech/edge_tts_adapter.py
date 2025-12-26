import edge_tts
from wilson.core.ports.ports import TTSPort

class EdgeTTSAdapter(TTSPort):
    async def text_to_speech(self, text: str, voice: str, output_file: str) -> None:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
