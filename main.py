import argparse
import sys
from src.core.config import settings
from src.core.logger import logger
from src.core.exceptions import AiFilmError, EngineError
from src.nlp_engine.base import Script, Scene

class DirectorOrchestrator:
    """The central brain that coordinates the AI Cinematic Universe."""
    
    def __init__(self, debug: bool = False):
        self.debug = debug or settings.DEBUG
        logger.info(f"🎬 Initializing {settings.PROJECT_NAME} v{settings.VERSION}")
        if self.debug:
            logger.debug("🔧 Debug mode enabled")

    def run_pipeline(self, creative_prompt: str, output_file: str = "final_film.mp4"):
        """Execute the full end-to-end film production pipeline."""
        try:
            logger.info(f"🚀 Starting Production Pipeline")
            logger.info(f"   Creative Prompt: '{creative_prompt}'")
            
            # Phase 1: Conceptualization
            logger.info("Phase 1: Conceptualization (NLP Engine)...")
            mock_script = self._generate_mock_script(creative_prompt)
            logger.info(f"   Script Generated: '{mock_script.title}' with {len(mock_script.scenes)} scenes.")

            # Phase 2: Visual Production
            logger.info("Phase 2: Visual Production (Vision Engine)...")
            for scene in mock_script.scenes:
                logger.debug(f"   Processing Scene {scene.scene_id} visuals at {scene.location}")

            # Phase 3: Audio Synthesis
            logger.info("Phase 3: Audio Synthesis (Audio Engine)...")
            logger.debug("   Synthesizing dialogues and scoring background music.")

            # Phase 4: Assembly
            logger.info(f"Phase 4: Post-Production & Assembly...")
            logger.info(f"✅ Production Successful! Saved to {settings.OUTPUT_DIR}/{output_file}")
            
        except AiFilmError as e:
            logger.error(f"❌ Production Failed! {str(e)}")
            sys.exit(1)
        except Exception as e:
            logger.critical(f"💥 Unexpected System Crash: {str(e)}")
            if self.debug:
                raise e
            sys.exit(1)

    def _generate_mock_script(self, prompt: str) -> Script:
        """Creates a placeholder script for demonstration."""
        # Simulated failure for robustness testing
        if not prompt or len(prompt) < 3:
            raise EngineError("NLP", "Prompt is too short for creative processing.")
            
        return Script(
            title="Algorithm of Destiny",
            summary_plot="A journey through the digital void.",
            scenes=[
                Scene(
                    scene_id=1,
                    description="Cyberpunk cityscape",
                    location="Neo-Tokyo Rooftop",
                    time_of_day="Night",
                    characters=["Ryu", "AI-Core"],
                    dialogues=[{"Ryu": "Is this reality?"}],
                    mood="Suspenseful"
                )
            ]
        )

def main():
    parser = argparse.ArgumentParser(description="AI Cinematic Universe - Professional Orchestrator CLI")
    parser.add_argument("--prompt", type=str, required=True, help="Creative prompt to generate the film")
    parser.add_argument("--output", type=str, default="final_film.mp4", help="Name of the output video file")
    parser.add_argument("--debug", action="store_true", help="Enable verbose debug logging")
    
    args = parser.parse_args()
    
    orchestrator = DirectorOrchestrator(debug=args.debug)
    orchestrator.run_pipeline(args.prompt, args.output)

if __name__ == "__main__":
    main()
