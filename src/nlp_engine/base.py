from abc import ABC, abstractmethod
from typing import Dict, List, Any
from pydantic import BaseModel

class Scene(BaseModel):
    """Data model for a single movie scene."""
    scene_id: int
    description: str
    location: str
    time_of_day: str
    characters: List[str]
    dialogues: List[Dict[str, str]]
    mood: str

class Script(BaseModel):
    """Data model for the entire screenplay."""
    title: str
    summary_plot: str
    scenes: List[Scene]

class BaseNLPEngine(ABC):
    """Abstract base class for LLM-based script generation."""
    
    @abstractmethod
    def generate_script(self, prompt: str) -> Script:
        """Transform a creative prompt into a structured script."""
        pass

    @abstractmethod
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """Analyze the emotional tone of characters or scenes."""
        pass
