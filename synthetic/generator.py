
import argparse
import json
import random
from pathlib import Path

TEAMS = [
    "Northbridge FC",
    "Kingswell United",
    "Riverside Athletic",
    "Westhaven Town",
    "Eastford Rovers",
    "Redmont City",
]

EVENT_TYPES = [
    "pass",
    "carry",
    "tackle",
    "interception",
    "shot",
    "foul",
    "corner",
]


def generate_match(match_number: int, rng: random.Random) -> tuple[dict, list[dict]]:
    home, away = rng.sample(TEAMS, 2)
    match_id = f"SYN_{match_number:05d}"

    teams = [
        {"team_id": f"{match_id}_HOME", "name": home, "side": "home"},
        {"team_id": f"{match_id}_AWAY", "name": away, "side": "away"},
    ]

    events = []
    score = {"home": 0, "away": 0}
    possession = 0

    for minute in range(1, 91):
        team = rng.choice(teams)
        side = team["side"]
        possession += 1

        player_number = rng.randint(1, 11)
        player_id = f"{team['team_id']}_P{player_number:02d}"

        event_type = rng.choices(
            EVENT_TYPES,
            weights=[45, 15, 10, 8, 12, 6, 4],
        )[0]

        x = round(rng.uniform(0, 100), 2)
        y = round(rng.uniform(0, 100), 2)
        outcome = "successful"
        extra = {}

        if event_type == "pass":
            outcome = (
                "successful" if rng.random() < 0.84 else "failed"
            )
            extra["pass_length"] = round(rng.uniform(3, 40), 2)

        elif event_type == "shot":
            x = round(rng.uniform(65, 98), 2)
            xg = round(
                min(0.85, max(0.01, ((x - 55) / 45) * rng.uniform(0.05, 0.5))),
                3,
            )
            goal = rng.random() < xg * 0.65
            on_target = goal or rng.random() < 0.35

            if goal:
                outcome = "goal"
                score[side] += 1
            elif on_target:
                outcome = "saved"
            else:
                outcome = "off_target"

            extra.update({
                "xg": xg,
                "is_on_target": on_target,
            })

        elif event_type == "tackle":
            outcome = (
                "successful" if rng.random() < 0.65 else "foul_committed"
            )

        event = {
            "event_id": f"{match_id}_E{len(events) + 1:06d}",
            "match_id": match_id,
            "period": 1 if minute <= 45 else 2,
            "minute": minute,
            "second": rng.randint(0, 59),
            "team_id": team["team_id"],
            "player_id": player_id,
            "possession_id": f"{match_id}_POS{possession:05d}",
            "event_type": event_type,
            "x": x,
            "y": y,
            "outcome": outcome,
            "score_home": score["home"],
            "score_away": score["away"],
            "synthetic": True,
            **extra,
        }

        events.append(event)

    match = {
        "match_id": match_id,
        "home_team": home,
        "away_team": away,
        "home_score": score["home"],
        "away_score": score["away"],
        "duration_minutes": 90,
        "synthetic": True,
        "events_count": len(events),
    }

    return match, events


def main():
    parser = argparse.ArgumentParser(
        description="Achilles Sports synthetic football dataset generator"
    )
    parser.add_argument("--matches", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/generated"),
    )
    args = parser.parse_args()

    if args.matches < 1:
        parser.error("--matches must be positive")

    rng = random.Random(args.seed)
    args.output.mkdir(parents=True, exist_ok=True)

    matches = []
    events_path = args.output / "events.jsonl"

    with events_path.open("w", encoding="utf-8") as file:
        for number in range(1, args.matches + 1):
            match, events = generate_match(number, rng)
            matches.append(match)

            for event in events:
                file.write(json.dumps(event) + "\n")

    matches_path = args.output / "matches.json"
    matches_path.write_text(
        json.dumps({
            "dataset": "Achilles Sports Synthetic Football",
            "synthetic": True,
            "seed": args.seed,
            "matches": matches,
        }, indent=2),
        encoding="utf-8",
    )

    print(f"Generated {len(matches)} matches")
    print(f"Events:  {events_path}")
    print(f"Matches: {matches_path}")


if __name__ == "__main__":
    main()
