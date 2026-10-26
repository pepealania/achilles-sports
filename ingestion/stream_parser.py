import json
import os
import logging
from typing import Generator, Dict, Any

# Configure structured logging for the ingestion pipeline
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] Ingestion Pipeline: %(message)s"
)
logger = logging.getLogger(__name__)

class FootballStreamParser:
    """Handles parsing, validation, and streaming of synthetic match data events."""
    
    def __init__(self, target_filepath: str = "data/synthetic/matches.jsonl"):
        self.target_filepath = target_filepath

    def verify_source(self) -> bool:
        """Checks if the data feed exists and is populated before parsing."""
        if not os.path.exists(self.target_filepath):
            logger.error(f"Source ingestion stream missing at: {self.target_filepath}")
            return False
        
        file_size = os.path.getsize(self.target_filepath)
        if file_size == 0:
            logger.warning(f"Ingestion source file at {self.target_filepath} is empty.")
            return False
            
        logger.info(f"Verified ingestion stream anchor. Stream size: {file_size} bytes.")
        return True

    def stream_events(self) -> Generator[Dict[Any, Any], None, None]:
        """Yields football event entries line-by-line out of the data payload."""
        if not self.verify_source():
            return

        logger.info(f"Opening continuous event parser for: {self.target_filepath}")
        
        try:
            with open(self.target_filepath, "r", encoding="utf-8") as file:
                for line_idx, line in enumerate(file, start=1):
                    clean_line = line.strip()
                    if not clean_line:
                        continue # Skip accidental whitespace rows
                        
                    try:
                        event_payload = json.loads(clean_line)
                        # Yield validated data downstream
                        yield event_payload
                    except json.JSONDecodeError as json_err:
                        logger.error(f"Malformed structural payload skipped at line {line_idx}: {json_err}")
                        continue
        except Exception as e:
            logger.critical(f"Critical stream failure during data feed parsing: {e}")
            raise e

def execute_ingestion_diagnostic():
    """Diagnostic hook to test streaming performance from the folder directory root."""
    # Handle path routing context if run directly inside /ingestion or the project root
    path_prefix = "" if os.path.exists("data") else "../"
    parser = FootballStreamParser(target_filepath=f"{path_prefix}data/synthetic/matches.jsonl")
    
    match_count = 0
    total_events = 0
    
    print("\n" + "="*60)
    print("      ACHILLES SPORTS - INGESTION ENGINE DIAGNOSTIC")
    print("="*60)
    
    for event in parser.stream_events():
        total_events += 1
        if event.get("type") == "MATCH_START":
            match_count += 1
            details = event.get("details", {})
            print(f"🚀 Found Match {match_count}: {details.get('home_team')} vs {details.get('away_team')} (Weather: {details.get('weather')})")
        elif event.get("type") == "MATCH_END":
            details = event.get("details", {})
            print(f"🏁 Match Ended | Final Scoreline: {details.get('final_score')} | Total Game Events: {details.get('total_events')}")
            print("-" * 60)

    print(f"\n📊 Diagnostics Complete: Successfully parsed {total_events} distinct football matrices across {match_count} matches.")

if __name__ == "__main__":
    execute_ingestion_diagnostic()
