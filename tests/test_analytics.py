# tests/test_analytics.py
import unittest
import os
from analytics.engine import FootballAnalyticsEngine

class TestFootballAnalyticsEngine(unittest.TestCase):
    def setUp(self):
        """Initializes the engine pointing to the live synthetic match track."""
        self.engine = FootballAnalyticsEngine(file_path="synthetic/matches.jsonl")

    def test_file_existence(self):
        """Ensures the generated synthetic data file is present in the workspace."""
        self.assertTrue(os.path.exists(self.engine.file_path), "synthetic/matches.jsonl dataset is missing!")

    def test_match_summary_structure(self):
        """Validates that the engine outputs a structurally intact data contract for Microsoft Foundry."""
        summary = self.engine.get_match_summary()
        
        # Core Keys Verification
        self.assertIn("match_id", summary)
        self.assertIn("home_team", summary)
        self.assertIn("away_team", summary)
        self.assertIn("stats", summary)
        self.assertIn("tactical_excellence_award_winner", summary)
        
        # Collective Metric Validations
        home_team = summary["home_team"]
        home_stats = summary["stats"][home_team]
        
        self.assertIn("collective_tactical_integrity_score", home_stats)
        self.assertIn("match_reality_index", home_stats)
        self.assertIn("pass_accuracy_pct", home_stats)

    def test_metric_logical_boundaries(self):
        """Ensures the custom Collective Tactical Integrity Index stays bounded between 0 and 100."""
        summary = self.engine.get_match_summary()
        for team in [summary["home_team"], summary["away_team"]]:
            score = summary["stats"][team]["collective_tactical_integrity_score"]
            self.assertTrue(0 <= score <= 100, f"CTIE score {score} for {team} is outside logical 0-100 limits!")

if __name__ == "__main__":
    unittest.main()
