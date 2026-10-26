# analytics/engine.py
import json
import os
from ingestion.stream_parser import FootballStreamParser

class FootballAnalyticsEngine:
    def __init__(self, file_path="data/synthetic/matches.jsonl"):
        # Connect directly to your ingestion stream layer
        self.parser = FootballStreamParser(target_filepath=file_path)

    def get_match_summary(self, match_id=None):
        events = []
        
        # Stream lines directly via your ingestion generator
        for ev in self.parser.stream_events():
            if match_id is None or ev.get("match_id") == match_id:
                events.append(ev)

        if not events:
            return {"error": f"No events found for match_id: {match_id}"}

        # Explicitly extract the first and last event dictionaries from the list
        start_ev = events[0]
        end_ev = events[-1]
        
        # Safeguard if running globally without an ID to pull a valid target match block
        current_match_id = start_ev["match_id"]
        
        # Filter down events strictly to this single match context to prevent cross-contamination
        match_events = [e for e in events if e.get("match_id") == current_match_id]
        start_ev = match_events[0]
        end_ev = match_events[-1]

        home_team = start_ev["details"]["home_team"]
        away_team = start_ev["details"]["away_team"]
        
        metrics = {
            "match_id": current_match_id,
            "home_team": home_team,
            "away_team": away_team,
            "final_score": end_ev["details"].get("final_score", "0-0"),
            "weather": start_ev["details"].get("weather", "Unknown"),
            "stats": {
                home_team: {"shots": 0, "xg": 0.0, "passes": 0, "successful_passes": 0, "fouls": 0, "cards": 0},
                away_team: {"shots": 0, "xg": 0.0, "passes": 0, "successful_passes": 0, "fouls": 0, "cards": 0}
            }
        }

        for ev in match_events:
            t = ev.get("team")
            if t not in metrics["stats"]:
                continue
                
            if ev["type"] == "SHOT":
                metrics["stats"][t]["shots"] += 1
                metrics["stats"][t]["xg"] += ev["details"].get("expected_goals", 0.0)
            elif ev["type"] == "PASS":
                metrics["stats"][t]["passes"] += 1
                if ev["details"].get("outcome") == "SUCCESSFUL":
                    metrics["stats"][t]["successful_passes"] += 1
            elif ev["type"] == "FOUL":
                metrics["stats"][t]["fouls"] += 1
            elif ev["type"] == "CARD":
                metrics["stats"][t]["cards"] += 1

        for team in [home_team, away_team]:
            team_stats = metrics["stats"][team]
            team_stats["xg"] = round(team_stats["xg"], 2)
            pass_acc = (team_stats["successful_passes"] / max(1, team_stats["passes"])) * 100
            team_stats["pass_accuracy_pct"] = round(pass_acc, 1)
            
            # Match Reality Index calculation
            mri = (team_stats["xg"] * 40) + (pass_acc * 0.4) - (team_stats["fouls"] * 2)
            team_stats["match_reality_index"] = round(max(0, min(100, mri)), 1)

            # 🏆 Collective Tactical Integrity & Excellence (CTIE) Matrix
            team_fluidity = (team_stats["successful_passes"] * 0.5) + (team_stats["shots"] * 2.0)
            team_disruption = (team_stats["fouls"] * 4.0) + (team_stats["cards"] * 12.0)
            
            ctie_score = 50.0 + team_fluidity - team_disruption
            team_stats["collective_tactical_integrity_score"] = round(max(0, min(100, ctie_score)), 1)

        # Evaluate which complete team squad wins the technical honor
        h_ctie = metrics["stats"][home_team]["collective_tactical_integrity_score"]
        a_ctie = metrics["stats"][away_team]["collective_tactical_integrity_score"]
        
        if h_ctie == a_ctie:
            metrics["tactical_excellence_award_winner"] = "DRAW"
        else:
            metrics["tactical_excellence_award_winner"] = home_team if h_ctie > a_ctie else away_team
            
        return metrics

if __name__ == "__main__":
    engine = FootballAnalyticsEngine()
    # Discover the first match_id from the stream to run a clean structured summary
    sample_match_id = None
    for event in engine.parser.stream_events():
        if event.get("match_id"):
            sample_match_id = event["match_id"]
            break
            
    print(f"Analyzing Match ID context: {sample_match_id}...")
    print(json.dumps(engine.get_match_summary(match_id=sample_match_id), indent=2))
