import json
import random
import uuid
from datetime import datetime, timedelta

TEAMS = [
    {"name": "Arsenal", "attack": 85, "defense": 82},
    {"name": "Aston Villa", "attack": 80, "defense": 78},
    {"name": "Chelsea", "attack": 82, "defense": 80},
    {"name": "Liverpool", "attack": 88, "defense": 84},
    {"name": "Manchester City", "attack": 90, "defense": 86},
    {"name": "Manchester United", "attack": 81, "defense": 79},
    {"name": "Newcastle United", "attack": 82, "defense": 78},
    {"name": "Tottenham Hotspur", "attack": 83, "defense": 77}
]

EVENT_TYPES = ["PASS", "SHOT", "FOUL", "CORNER", "CARD", "OFFSIDE", "SUBSTITUTION"]

def calculate_xg(distance, angle, pressure, situation):
    """Deterministic xG model mimicking optical/event tracking physics."""
    base_xg = 0.3 if situation == "OPEN_PLAY" else 0.15
    if situation == "PENALTY": return 0.76
    if situation == "HEADER": base_xg *= 0.5
    
    # Distance penalty (exponential decay)
    distance_factor = max(0.01, 1.0 - (distance / 40.0))
    # Angle penalty (worse angles = lower xG)
    angle_factor = max(0.1, 1.0 - (abs(angle) / 90.0))
    # Defensive pressure modifier
    pressure_factor = 0.4 if pressure == "HIGH" else (0.7 if pressure == "MEDIUM" else 1.0)
    
    return round(base_xg * distance_factor * angle_factor * pressure_factor, 3)

def generate_synthetic_match(home_team, away_team):
    match_id = str(uuid.uuid4())[:8]
    events = []
    
    # Base match time anchor
    start_time = datetime.utcnow() - timedelta(days=random.randint(1, 30))
    
    # Meta Initialization Event
    events.append({
        "event_id": str(uuid.uuid4()),
        "match_id": match_id,
        "timestamp": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "minute": 0,
        "second": 0,
        "type": "MATCH_START",
        "team": "SYSTEM",
        "player": "SYSTEM",
        "coordinates": {"x": 0.0, "y": 0.0},
        "details": {
            "home_team": home_team["name"],
            "away_team": away_team["name"],
            "stadium": f"{home_team['name']} Arena",
            "weather": random.choice(["Dry", "Rain", "Windy", "Overcast"])
        }
    })

    home_score = 0
    away_score = 0

    # Simulate 90 continuous structural event iterations
    for minute in range(1, 91):
        if random.random() > 0.45:  # ~40-50 major events per match
            continue
            
        # Determine dominant team based on raw stats + minor variance
        home_weight = home_team["attack"] / (home_team["attack"] + away_team["defense"])
        acting_team = home_team if random.random() < home_weight else away_team
        defending_team = away_team if acting_team == home_team else home_team
        
        event_type = random.choices(EVENT_TYPES, weights=[60, 18, 12, 5, 2, 2, 1])[0]
        event_second = random.randint(0, 59)
        
        # Calculate precise cascading timestamp for the event line
        event_time = start_time + timedelta(minutes=minute, seconds=event_second)
        
        event = {
            "event_id": str(uuid.uuid4()),
            "match_id": match_id,
            "timestamp": event_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "minute": minute,
            "second": event_second,
            "type": event_type,
            "team": acting_team["name"],
            "player": f"Player_{acting_team['name'][:3].upper()}_{random.randint(1, 25)}",
            "coordinates": {
                "x": round(random.uniform(50.0, 105.0) if random.random() > 0.3 else random.uniform(0.0, 50.0), 1),
                "y": round(random.uniform(0.0, 68.0), 1)
            },
            "details": {}
        }
        
        # Inject contextually dependent analytics payloads
        if event_type == "PASS":
            event["details"] = {
                "outcome": random.choices(["SUCCESSFUL", "INCOMPLETE", "INTERCEPTED"], weights=[75, 15, 10])[0],
                "length_meters": round(random.uniform(5.0, 45.0), 1),
                "zone": random.choice(["ATTACKING_THIRD", "MIDDLE_THIRD", "DEFENSIVE_THIRD"])
            }
        elif event_type == "SHOT":
            dist = round(random.uniform(5.5, 30.0), 1)
            ang = round(random.uniform(-45.0, 45.0), 1)
            press = random.choice(["HIGH", "MEDIUM", "LOW"])
            sit = random.choices(["OPEN_PLAY", "HEADER", "CORNER"], weights=[80, 15, 5])[0]
            xg_val = calculate_xg(dist, ang, press, sit)
            
            # Determine outcome structurally guided by the calculated xG
            outcome = "BLOCKED" if random.random() < 0.3 else ("OFF_TARGET" if random.random() > (xg_val + 0.4) else "SAVED")
            if random.random() < xg_val:
                outcome = "GOAL"
                if acting_team == home_team: home_score += 1
                else: away_score += 1

            event["details"] = {
                "expected_goals": xg_val,
                "distance_meters": dist,
                "angle_degrees": ang,
                "situation": sit,
                "pressure": press,
                "outcome": outcome
            }
        elif event_type == "FOUL":
            event["details"] = {
                "severity": random.choices(["MINOR", "TACTICAL", "RECKLESS"], weights=[70, 20, 10])[0],
                "suffered_by": f"Player_{defending_team['name'][:3].upper()}_{random.randint(1, 25)}"
            }
        elif event_type == "CARD":
            event["details"] = {
                "card_color": random.choices(["YELLOW", "RED"], weights=[92, 8])[0],
                "reason": random.choice(["Unsporting Behaviour", "Late Tackle", "Dissent"])
            }
            
        events.append(event)

    # Meta Wrap-up Event
    end_time = start_time + timedelta(minutes=90)
    events.append({
        "event_id": str(uuid.uuid4()),
        "match_id": match_id,
        "timestamp": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "minute": 90,
        "second": 0,
        "type": "MATCH_END",
        "team": "SYSTEM",
        "player": "SYSTEM",
        "coordinates": {"x": 0.0, "y": 0.0},
        "details": {
            "final_score": f"{home_score}-{away_score}",
            "home_goals": home_score,
            "away_goals": away_score,
            "total_events": len(events)
        }
    })
    
    return events

def run_generator(output_filename="data/synthetic/matches.jsonl", num_matches=5):
    print(f"Generating {num_matches} high-fidelity matches...")
    with open(output_filename, "w") as f:
        for _ in range(num_matches):
            home, away = random.sample(TEAMS, 2)
            match_events = generate_synthetic_match(home, away)
            for event in match_events:
                f.write(json.dumps(event) + "\n")
    print(f"Successfully exported data to {output_filename}!")

if __name__ == "__main__":
    run_generator()
