# Achilles Sports ⚽

**Football intelligence beyond the scoreline.**

Achilles Sports is an AI-powered football analytics platform that transforms football events into explainable match intelligence, performance metrics, and probability-based insights.

A final score tells us what happened. Achilles Sports aims to explain **how and why a match unfolded the way it did**.

By analyzing shots, possession, attacking pressure, expected goals (xG), match momentum, and other event-level signals, Achilles Sports helps users understand team performance beyond the scoreboard. Its goal is to make football intelligence useful and understandable for analysts, fans, broadcasters, and users interested in statistical betting analysis.

Built for the **Inside the Game: Developer Hackathon**, organized by Microsoft and the Premier League, Achilles Sports combines synthetic football simulation, deterministic analytics, and Microsoft Foundry-powered AI.

> **Data notice:** Achilles Sports uses synthetic, football-realistic data. It does not redistribute real Premier League match data.

## 🚀 Quickstart

### Web dashboard

The dashboard is a frontend demonstration and does not require Azure credentials.

```bash
cd frontend
npm install
npm run dev
```

Vite prints the local URL when the development server starts. To create a production build, run `npm run build` from `frontend`.

### Python analytics

From the repository root, run the summary engine against the bundled synthetic event stream:

```bash
python -m analytics.engine
```

Run the analytics tests with:

```bash
python -m unittest discover -s tests
```

The test suite currently has one known failure: `test_file_existence` expects a `file_path` attribute that `FootballAnalyticsEngine` does not expose.

## 🗂️ Project Layout

- `frontend/` contains the React dashboard and Vite development setup.
- `analytics/` contains the event-based match summary engine.
- `ingestion/` parses JSONL match event streams.
- `data/synthetic/` contains the bundled sample match data used by the analytics engine.
- `synthetic/` and `packages/simulation/` contain synthetic match and event generation code.
- `forecasting/` and `intelligence/` hold forecasting and analyst components under development.
- `integrations/` contains external service integrations; `main.py` is the optional Foundry inference entry point.
- `tests/` contains the Python analytics tests.

## 📍 Current Implementation

- The React dashboard is a visual demo. Its displayed metrics and status messages are generated in the browser and are not connected to the Python analytics engine, a live match feed, or Microsoft Foundry.
- The Python event parser reads JSONL match events, and `FootballAnalyticsEngine` computes a match summary, including xG totals, pass accuracy, Match Reality Index, and CTIE scores.
- `main.py` contains an optional Microsoft Foundry/Azure OpenAI inference path. It requires Azure project configuration and a deployed model; it is separate from the web dashboard.
- Forecasting, live event updates, market odds, multimodal ingestion, and AI-grounded match analysis described below are planned capabilities unless explicitly identified as implemented.

## 🎯 Vision

Football matches tell stories that final scores cannot fully explain.

A team can dominate possession without creating meaningful chances. Another can generate dangerous opportunities while having less of the ball. A late goal can change the result without accurately reflecting the balance of performance throughout the match.

Achilles Sports aims to uncover these deeper patterns by connecting event-level data, football metrics, probability estimates, and explainable AI.

The platform is built around three principles:

- **Beyond the scoreline:** Evaluate underlying performance rather than relying exclusively on results or standings.
- **Evidence before explanation:** Ground analytical insights in calculated metrics and traceable match events.
- **Probabilities, not guarantees:** Communicate uncertainty and distinguish statistical evidence from predictions about future outcomes.

The long-term vision is to deliver actionable match intelligence that helps users understand performance, assess possible outcomes, and explore statistical signals in football matches.

## ✨ Core Features

### 1. Beyond-the-Score Match Intelligence

Achilles Sports analyzes match events to identify patterns that may not be apparent from the score alone.

- Analyze shots, shots on target, corners, fouls, cards, and offsides.
- Track possession, attacking activity, and changes in match dynamics.
- Calculate expected goals (xG) estimates from shot attributes.
- Compare the scoreline with underlying chance creation and performance.
- Identify changes in attacking pressure and territorial control where the available data supports them.
- Explain important match developments using supporting metrics and events.

The objective is not simply to report statistics, but to explain what those statistics reveal about a match.

### 2. Synthetic Football Match Simulation

Synthetic data provides a reproducible environment for developing and evaluating football analytics.

- Generate football-realistic matches and event sequences.
- Simulate goals, passes, shots, fouls, corners, cards, and other match events.
- Create reproducible scenarios for analytical testing.
- Replay events incrementally to simulate live match conditions.
- Generate structured match data for downstream metrics, forecasting, and AI analysis.
- Test situations such as possession dominance without goals, high-pressure attacking periods, and scorelines that differ from underlying performance.

All generated matches and scenarios are synthetic and intended for development, demonstration, and evaluation.

### 3. Football Metrics and Statistical Analysis

The metrics engine calculates football statistics independently of AI-generated explanations.

- Calculate match metrics from structured event data.
- Estimate xG from available shot attributes.
- Analyze attacking activity, possession patterns, and match momentum.
- Identify meaningful changes in performance over time.
- Compare statistical performance between teams.
- Estimate probabilities for selected football outcomes.
- Evaluate analytical results against known synthetic scenarios.

Where appropriate, Achilles Sports will distinguish directly calculated metrics from estimates and derived indicators.

### 4. Match Reality Index — Performance Beyond the Score

The planned **Match Reality Index** is a composite indicator designed to summarize underlying team performance beyond the current scoreline.

It may combine normalized measures such as:

- Chance quality and expected goals.
- Attacking pressure and territorial control.
- Progression into dangerous areas.
- Defensive stability and transition risk.
- Sustained attacking activity.

The index is intended to make complex match statistics easier to interpret while preserving access to the underlying evidence.

Its components, weights, and evaluation methodology will be documented and tested against synthetic scenarios. It will remain distinct from outcome probabilities: a team performing better statistically is not necessarily the team most likely to win from the current match state.

### 5. Outcome Probabilities and Statistical Betting Analysis

Achilles Sports aims to support evidence-based analysis of selected football betting markets.

- Estimate win, draw, and loss probabilities where supported by the model.
- Track how estimated probabilities change as match events unfold.
- Compare underlying team performance with the current scoreline.
- Explain the statistical evidence behind probability estimates.
- Represent uncertainty and identify situations where the available data is insufficient.
- Support comparisons with market-implied probabilities when reliable odds data is available.
- Evaluate forecasts using reproducible synthetic scenarios and appropriate statistical metrics.

Market comparisons will account for bookmaker margin where applicable. Simulated odds will be clearly distinguished from real market prices.

Probability estimates are model outputs, not guarantees of future results or profitability. Forecast quality must be evaluated before any claims about predictive performance are made.

## 🏆 Feature Highlight: Collective Tactical Integrity & Excellence Award (CTIE)

Achilles Sports completely reimagines traditional, highly subjective "Fair Play" or "Team of the Month" accolades by computing an entirely data-driven, squad-wide honor: **The Collective Tactical Integrity & Excellence (CTIE) Award**.

Inspired by standard-setting performances (such as Spain's historic positional mastery where they simultaneously dominate both the scoreboard and structural style against heavyweights like Argentina), this feature serves as an objective validator of beautiful, constructive team football.

### 🧠 The Mathematical Blueprint
Instead of relying on human committees or bias, our underlying python metrics engine reads the event stream to evaluate the whole squad's collective tactical footprint:
* **Baseline Score (50.0):** Every squad starts on a flat tracking plane.
* **Fluidity Bonuses:** Programmatically scales up based on high-velocity **Successful Passes (+0.5)** and positive **Shot Volume (+2.0)**.
* **Anti-Football Penalties:** Drastically penalizes teams relying on cynical or negative disruptions to preserve scorelines, deducting heavily for **Fouls (-4.0)** and **Yellow/Red Cards (-12.0)**.

### 🤖 Microsoft Foundry Tool Integration
This complex evaluation is decoupled from the LLM to prevent hallucinations. The process is orchestrated cleanly via Microsoft Foundry:
1. **Tool Binding:** The deterministic metrics engine (`analytics/engine.py`) is registered directly to the Microsoft Foundry workspace as a custom agent tool capability.
2. **Intent Routing:** When a fan or broadcaster queries the match center, the Foundry agent cleanly invokes the native manifest, pulling structurally bounded integers without raw prompt guessing.
3. **Grounded Narratives:** The agent translates the factual data variances into production-ready media recaps, explicitly calling out statistical anomalies (e.g., when a team loses the scoreline but securely wins the CTIE Award due to outstanding discipline and spatial dominance).


## 🚀 Microsoft Foundry AI Integration

Achilles Sports leverages **Microsoft Foundry** as the core engine to orchestrate, evaluate, and scale our AI intelligence layer. Instead of relying on traditional, fragmented LLM pipelines, Foundry accelerates our development lifecycle and ensures production-grade reliability across our football analytics workflow.

### 1. Agent Orchestration & Custom Tools (Developer Productivity)
* **Unified Workspace:** We use Microsoft Foundry to manage our multi-agent framework, bypassing the need for complex, manual prompt-chaining code.
* **Deterministic Tool Binding:** Foundry seamlessly maps our specialized Python metrics engine (xG models, Match Reality Index) as executable tools for the AI agents, enabling text-based queries to securely trigger deep numerical calculations.

### 2. Multi-Modal Event Ingestion & Inference (Scalable AI Experiences)
* **High-Throughput Processing:** Match event data streams through Foundry's managed inference endpoints, handling synthetic JSONL match structures efficiently.
* **Extensible Modalities:** Foundry’s underlying platform architecture ensures that as Achilles Sports evolves to support video, audio commentary, and player-tracking data, our infrastructure can scale without a full backend rewrite.

### 3. Rigorous AI Evaluation & Grounding (Faster Innovation)
* **Automated Factual Auditing:** Football narratives can suffer from AI hallucinations. We use Foundry’s evaluation suites to test generated match recaps against the underlying deterministic data.
* **Metrics-Driven Refinement:** Foundry drastically reduced our prompt engineering cycle, allowing us to benchmark agent responses for accuracy, token latency, and alignment with statistical evidence.

### 4. Enterprise Observability & Safety
* **Granular Traceability:** Every agent decision, tool execution, and LLM call is tracked using Foundry’s native monitoring capabilities, letting us isolate and resolve pipeline bottlenecks instantly.
* **Responsible Football Intelligence:** Foundry ensures that statistical betting analysis and outcome probabilities are presented safely, accurately communicating uncertainty without generating misleading financial advice.


### 7. Planned User Experience

The planned interface will bring match statistics, analytical evidence, and AI explanations together.

- **Match Overview:** Scoreline, team statistics, and key performance indicators.
- **Live Match Center:** Event timeline, changing match metrics, and significant match developments.
- **Beyond-the-Score Analysis:** Compare the scoreline with underlying team performance.
- **Match Reality Index:** Inspect the components behind a composite performance indicator.
- **Probability Tracker:** View estimated outcome probabilities and their changes over time.
- **AI Match Analyst:** Ask questions and receive explanations grounded in calculated metrics.
- **Statistical Market Analysis:** Explore probability estimates and compare them with available market odds.
- **Automated Match Recaps:** Generate evidence-based summaries of important moments and overall match dynamics.

> **Implementation status:** Features described as planned or intended are part of the product roadmap and are not necessarily available in the current version.

## 🏗️ Architecture

Achilles Sports separates data ingestion, synthetic match generation, deterministic football analytics, probability estimation, and AI-powered interpretation into modular components.

The initial implementation uses structured JSONL data to represent synthetic, football-realistic match events. The ingestion architecture is designed to support additional data modalities in the future, including video, audio commentary, images, and player-tracking data.

The goal is to allow new data sources to be integrated without redesigning the core analytics engine.

```text
                 Synthetic and External Data
                             |
              +--------------+--------------+
              |              |              |
              v              v              v
         JSONL Events     Video/Images   Audio/Tracking
         (Initial)         (Future)        (Future)
              |              |              |
              +--------------+--------------+
                             |
                             v
                  Extensible Ingestion Layer
                  - JSONL event parser
                  - Modality-specific adapters
                  - MCP-connected data sources
                             |
                             v
                Normalization and Synchronization
                - Match and event identifiers
                - Timestamps and metadata
                - Data provenance and validation
                             |
                             v
                    Canonical Match Model
                             |
              +--------------+--------------+
              |                             |
              v                             v
       Football Metrics              Multimodal Evidence
       and Event Analysis             (When Available)
              |                             |
              +--------------+--------------+
                             |
                             v
                  Outcome Probability Models
                             |
                             v
                    Evidence and Metrics Tools
                             |
                             v
                    Microsoft Foundry
                   AI Agent Orchestration
                             |
                             v
                 Explainable Match Intelligence
                             |
                  +----------+----------+
                  |          |          |
                  v          v          v
               Match UI   AI Analyst   Match Recaps
