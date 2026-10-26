# intelligence/agent_tools.py
import json
from analytics.engine import FootballAnalyticsEngine

# 1. Initialize our analytical engine core
analytics_engine = FootballAnalyticsEngine()

def get_match_intelligence_manifest():
    """
    Returns the strict tool definition schema required by Microsoft Foundry
    to register our deterministic calculations into the Agent's tool cockpit.
    """
    return {
        "type": "function",
        "function": {
            "name": "calculate_match_analytics",
            "description": (
                "Invokes the Achilles deterministic analytics engine to retrieve precise structural metrics "
                "for a specific match. Includes shots, xG profiles, pass accuracy, the Match Reality Index (MRI), "
                "and the Collective Tactical Integrity & Excellence (CTIE) award winner. Use this whenever a user "
                "asks for a performance summary, statistics, or tactical evaluations of a match."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "match_id": {
                        "type": "string",
                        "description": "The unique 8-character identifier of the target football match (e.g., '5bf4db4a')."
                    }
                },
                "required": ["match_id"]
            }
        }
    }

def calculate_match_analytics(match_id: str) -> str:
    """
    The executable tool function invoked by the Foundry Agent routing layer.
    Takes a structural string input, queries our engine, and drops a stringified JSON back.
    """
    print(f"🤖 [Foundry Agent Tool Link] Invoking native calculation matrix for Match ID: {match_id}...")
    summary = analytics_engine.get_match_summary(match_id=match_id)
    
    if "error" in summary:
        return json.dumps({"status": "error", "message": summary["error"]})
        
    return json.dumps(summary)

if __name__ == "__main__":
    # Quick sanity test to verify our agent wrapper hooks up to our analytics engine cleanly
    print("="*60)
    print("   ACHILLES INTELLIGENCE - AGENT MANIFEST INITIALIZATION")
    print("="*60)
    print("Checking Microsoft Foundry registration schema...")
    print(json.dumps(get_match_intelligence_manifest(), indent=2))
