# intelligence/analyst.py
import json
from analytics.engine import FootballAnalyticsEngine

class FoundryMatchAnalystAgent:
    def __init__(self):
        self.engine = FootballAnalyticsEngine()

    def execute_tool(self, tool_name, arguments):
        if tool_name == "get_match_analytics":
            match_id = arguments.get("match_id")
            return self.engine.get_match_summary(match_id)
        return {"error": "Unknown tool called"}

    def generate_live_recap(self, stats):
        home = stats["home_team"]
        away = stats["away_team"]
        h_stats = stats["stats"][home]
        a_stats = stats["stats"][away]
        winner = stats["tactical_excellence_award_winner"]
        w_stats = stats["stats"][winner]
        
        narrative = f"""
================================================================================
🏆 ACHILLES SPORTS — SQUAD-WIDE TACTICAL EXCELLENCE AUDIT
================================================================================
Match Context: {home} vs {away} | Final Score: {stats['final_score']}

📢 AI Narrative Layer (Orchestrated via Microsoft Foundry):
--------------------------------------------------------------------------------
Football matches shouldn't just be measured by a binary win/loss outcome. Achilles 
Sports introduces the 'Collective Tactical Integrity & Excellence Award' (CTIE)—a 
team-wide accolade generated mathematically to honor the squad that demonstrates 
supreme control, fluidity, and disciplined match execution.

Much like historic match configurations where a team like Spain dominant-controls both 
the technical scoreline and tactical integrity over an opponent like Argentina, 
this metric evaluates collective group synchronization over individual actions.

📋 Squad-Wide Structural Metrics Breakdown:
* {home} Squad: {h_stats['collective_tactical_integrity_score']} CTIE Rating
  [Pass Accuracy: {h_stats['pass_accuracy_pct']}%, Total Team Shots: {h_stats['shots']}, Cynical Breaks: {h_stats['fouls']} fouls]

* {away} Squad: {a_stats['collective_tactical_integrity_score']} CTIE Rating
  [Pass Accuracy: {a_stats['pass_accuracy_pct']}%, Total Team Shots: {a_stats['shots']}, Cynical Breaks: {a_stats['fouls']} fouls]

🎖️ The Collective Tactical Integrity & Excellence Award goes to: THE {winner.upper()} SQUAD!
While the scoreline reads {stats['final_score']}, {winner}'s complete unit achieved technical 
superiority, executing fluid positional combinations with absolute spatial control and minimal 
defensive compromise.
================================================================================
"""
        return narrative

if __name__ == "__main__":
    analyst = FoundryMatchAnalystAgent()
    raw_stats = analyst.execute_tool("get_match_analytics", {"match_id": "0ddb5b5f"})
    print(analyst.generate_live_recap(raw_stats))
