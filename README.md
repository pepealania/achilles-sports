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
