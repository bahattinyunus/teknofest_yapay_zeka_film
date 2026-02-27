import pytest
from main import DirectorOrchestrator

def test_orchestrator_initialization():
    orchestrator = DirectorOrchestrator()
    assert orchestrator is not None

def test_mock_script_generation():
    orchestrator = DirectorOrchestrator()
    script = orchestrator._generate_mock_script("test prompt")
    assert script.title == "Algorithm of Destiny"
    assert len(script.scenes) > 0
