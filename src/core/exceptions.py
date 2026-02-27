class AiFilmError(Exception):
    """Base exception for all AI Film errors."""
    pass

class EngineError(AiFilmError):
    """Raised when an AI engine (NLP, Vision, Audio) fails."""
    def __init__(self, engine_name: str, message: str):
        self.engine_name = engine_name
        super().__init__(f"[{engine_name}] Engine Failure: {message}")

class ConfigurationError(AiFilmError):
    """Raised when there's an issue with environment variables or config files."""
    pass

class CompositorError(AiFilmError):
    """Raised during the final video assembly phase."""
    pass
