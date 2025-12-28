from wilson.config.settings import Settings
from wilson.core.domain.models import AssistantConfig
from wilson.core.services.orchestrator import Orchestrator
from wilson.adapters.llm.gemini_client import GeminiAdapter
from wilson.adapters.speech.edge_tts_adapter import EdgeTTSAdapter
from wilson.adapters.speech.pygame_player import PygamePlayerAdapter
from wilson.adapters.speech.stt_adapter import SpeechRecognitionAdapter

def build_app() -> Orchestrator:
    settings = Settings()
    
    # Adapters
    llm_adapter = GeminiAdapter(
        api_key=settings.GEMINI_API_KEY, 
        model_name=settings.GEMINI_MODEL
    )
    tts_adapter = EdgeTTSAdapter()
    player_adapter = PygamePlayerAdapter()
    stt_adapter = SpeechRecognitionAdapter()
    
    # Config
    assistant_config = AssistantConfig(
        name="W.I.L.S.O.N.",
        system_prompt=settings.SYSTEM_PROMPT,
        voice_name=settings.DEFAULT_VOICE
    )
    
    # Service
    return Orchestrator(
        llm=llm_adapter, 
        tts=tts_adapter, 
        player=player_adapter,
        stt=stt_adapter,
        config=assistant_config
    )
