# Achilles Sports ⚽

**Football intelligence beyond the scoreline.**

Achilles Sports is an AI-powered football analytics platform that transforms football events into explainable match intelligence, performance metrics, and probability-based insights.

A final score tells us what happened. Achilles Sports aims to explain **how and why a match unfolded the way it did**.

By analyzing shots, possession, attacking pressure, expected goals (xG), match momentum, and other event-level signals, Achilles Sports helps users understand team performance beyond the scoreboard. Its goal is to make football intelligence useful and understandable for analysts, fans, broadcasters, and users interested in statistical betting analysis.

Built for the **Inside the Game: Developer Hackathon**, organized by Microsoft and the Premier League, Achilles Sports combines synthetic football simulation, deterministic analytics, and Microsoft Foundry-powered AI.

> **Data notice:** Achilles Sports uses synthetic, football-realistic data. It does not redistribute real Premier League match data.

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

### 6. Microsoft Foundry AI Integration

Microsoft Foundry provides the AI layer that turns calculated football metrics into understandable and useful explanations.

The intended integration includes:

- Explain statistical patterns using evidence retrieved from match data.
- Generate contextual match summaries and narratives.
- Answer questions about team performance and match dynamics.
- Use analytical tools to retrieve calculated metrics rather than inventing statistics.
- Orchestrate multi-step analysis when a question requires several calculations or evidence sources.
- Adapt explanations for different audiences, including fans, analysts, and broadcasters.
- Evaluate AI responses for factual grounding, relevance, consistency, and usefulness.
- Inspect agent execution, tool calls, latency, and failures using available observability capabilities.

The analytics engine remains responsible for calculating authoritative statistics. The AI layer interprets those results, explains their implications, and communicates uncertainty.

The goal is to demonstrate how Microsoft Foundry can accelerate development and orchestrate reliable AI-powered football intelligence, rather than using an LLM solely to generate text.

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

Achilles Sports separates synthetic event generation, deterministic football analytics, probability estimation, and AI-powered interpretation.

```text
              Synthetic Football Events
                         |
                         v
              Synthetic Match Generator
                         |
                         v
                Structured Match Data
                         |
                         v
               Football Metrics Engine
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Match Statistics       Derived Indicators
      and Event Evidence     and Performance Index
             |                       |
             +-----------+-----------+
                         |
                         v
                Outcome Probability
                      Models
                         |
                         v
             Evidence and Metrics Tools
                         |
                         v
                Microsoft Foundry
              Agent and Tool Orchestration
                         |
                         v
             Explainable Match Intelligence
                         |
              +----------+----------+
              |          |          |
              v          v          v
           Match UI   AI Analyst   Match Recaps
