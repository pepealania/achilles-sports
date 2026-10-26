# analytics/engine.py
import json
import os

class FootballAnalyticsEngine:
    def __init__(self, file_path="synthetic/matches.jsonl"):
        self.file_path = file_path

    def get_match_summary(self, match_id=None):
        if not os.path.exists(self.file_path):
            return {"error": f"Dataset file not found at {self.file_path}"}

        events = []
        with open(self.file_path, "r") as f:
            for line in f:
                if line.strip():
                    ev = json.loads(line)
                    if match_id is None or ev.get("match_id") == match_id:
                        events.append(ev)

        if not events:
            return {"error": f"No events found for match_id: {match_id}"}

        # FIX: Explicitly extract the first [0] and last [-1] event dictionaries from the list
        start_ev = events[0]
        end_ev = events[-1]
        
        home_team = start_ev["details"]["home_team"]
        away_team = start_ev["details"]["away_team"]
        
        metrics = {
            "match_id": start_ev["match_id"], # FIX: Pull from dictionary, not list
            "home_team": home_team,
            "away_team": away_team,
            "final_score": end_ev["details"].get("final_score", "0-0"),
            "weather": start_ev["details"].get("weather", "Unknown"),
            "stats": {
                home_team: {"shots": 0, "xg": 0.0, "passes": 0, "successful_passes": 0, "fouls": 0, "cards": 0},
                away_team: {"shots": 0, "xg": 0.0, "passes": 0, "successful_passes": 0, "fouls": 0, "cards": 0}
            }
        }

        for ev in events:
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
        
        metrics["tactical_excellence_award_winner"] = home_team if h_ctie > a_ctie else away_team
        return metrics

if __name__ == "__main__":
    engine = FootballAnalyticsEngine()
    print(json.dumps(engine.get_match_summary(), indent=2))
