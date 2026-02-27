from abc import ABC, abstractmethod
from typing import List

class BaseVisionEngine(ABC):
    """Abstract base class for AI image/video generation."""
    
    @abstractmethod
    def generate_image(self, prompt: str, output_path: str) -> str:
        """Generate a static image for a scene."""
        pass

    @abstractmethod
    def animate_scene(self, image_path: str, motion_prompt: str) -> str:
        """Convert a static image into a video clip."""
        pass

class BaseAudioEngine(ABC):
    """Abstract base class for AI voice and music generation."""
    
    @abstractmethod
    def generate_voice(self, text: str, character_id: str) -> str:
        """Generate high-fidelity voice for dialogue."""
        pass

    @abstractmethod
    def generate_music(self, mood: str, duration: int) -> str:
        """Generate atmospheric background music."""
        pass
