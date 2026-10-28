import React, { useState, useEffect } from "react";
import { Activity, Cpu, RefreshCw } from "lucide-react";
import EventTicksDetails from "./EventTicksDetails";

export default function AchillesDashboard() {
  const [matchIndex, setMatchIndex] = useState(53.8);
  const [ticks, setTicks] = useState(1459);
  const [events, setEvents] = useState([
    { id: 1459, text: "Team A completed a sequential horizontal string of 8 short passes.", type: "pass" },
    { id: 1458, text: "Shot volume addition: Team B attempt from distance blocked safely.", type: "shot" },
    { id: 1457, text: "Match disruption: Tactical foul called against Team A midfielder.", type: "foul" },
  ]);
  const [history, setHistory] = useState([51.0, 52.5, 50.8, 53.0, 53.8]);

  // Derived or tracked counts for the metrics prop
  const [metrics, setMetrics] = useState({
    totalPasses: 1,
    totalShots: 1,
    totalFouls: 1,
    expectedGoalsXG: 0.35,
  });

  // Simulation loop to model incoming synthetic match data streams
  useEffect(() => {
    const interval = setInterval(() => {
      const eventRoll = Math.random();
      let eventText = "";
      let indexDelta = 0;
      let eventType = "pass";
      let xGDelta = 0;

      // 1. Calculate the upcoming Tick ID safely
      let currentTick;
      setTicks((prev) => {
        currentTick = prev + 1;
        return currentTick;
      });

      // 2. Compute metrics based on roll
      if (eventRoll > 0.6) {
        eventText = `Tick ${currentTick}: High-velocity successful pass completed in the middle third. (+0.5 CTIE Base)`;
        indexDelta = 0.4;
        eventType = "pass";
      } else if (eventRoll > 0.3) {
        eventText = `Tick ${currentTick}: Dangerous progressive shot volume entry on frame. (+2.0 CTIE Base)`;
        indexDelta = 1.2;
        eventType = "shot";
        xGDelta = parseFloat((Math.random() * 0.25).toFixed(2)); // Generate small incremental simulated xG
      } else {
        eventText = `Tick ${currentTick}: Tactical match disruption / Cynical foul committed. (-4.0 CTIE Penalty)`;
        indexDelta = -1.5;
        eventType = "foul";
      }

      // 3. Update events list
      setEvents((prevEvents) => [
        { id: currentTick, text: eventText, type: eventType },
        ...prevEvents.slice(0, 19)
      ]);

      // 4. Bounded Match Reality Index calculations
      setMatchIndex((prevIndex) => {
        const updated = Math.min(100, Math.max(0, parseFloat((prevIndex + indexDelta).toFixed(1))));
        setHistory((h) => [...h.slice(-14), updated]);
        return updated;
      });

      // 5. Keep metrics tab up-to-date
      setMetrics((prev) => ({
        totalPasses: prev.totalPasses + (eventType === "pass" ? 1 : 0),
        totalShots: prev.totalShots + (eventType === "shot" ? 1 : 0),
        totalFouls: prev.totalFouls + (eventType === "foul" ? 1 : 0),
        expectedGoalsXG: parseFloat((prev.expectedGoalsXG + xGDelta).toFixed(2)),
      }));

    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-slate-950 text-slate-100 min-height-screen p-4 sm:p-8 font-sans">
      <div className="max-w-7xl mx-auto space-y-6">
        
        {/* Top Header Row */}
        <header className="flex items-center gap-3 border-b border-slate-900 pb-4">
          <Activity className="text-teal-400 size-8 animate-pulse" />
          <div>
            <h1 className="text-xl font-bold tracking-tight">Achilles Live Arena Engine</h1>
            <p className="text-xs text-slate-500 font-mono">Status: Stream Processing Online</p>
          </div>
        </header>

        {/* Top Overview Metric Boxes */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="bg-slate-900/40 border border-slate-800/80 rounded-xl p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-mono font-medium text-slate-400 uppercase tracking-wider flex items-center gap-1.5 mb-1">
                <Cpu size={14} className="text-teal-500" /> Match Reality Index
              </p>
              <p className="text-3xl font-bold font-mono tracking-tight text-slate-100">{matchIndex}</p>
            </div>
            <div className="text-xs font-mono px-2 py-1 rounded bg-teal-500/10 text-teal-400 border border-teal-500/20">
              Live Core
            </div>
          </div>

          <div className="bg-slate-900/40 border border-slate-800/80 rounded-xl p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-mono font-medium text-slate-400 uppercase tracking-wider flex items-center gap-1.5 mb-1">
                <RefreshCw size={14} className="text-amber-500" /> Total Ticks
              </p>
              <p className="text-3xl font-bold font-mono tracking-tight text-slate-100">{ticks}</p>
            </div>
            <div className="text-xs font-mono px-2 py-1 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">
              Ingesting
            </div>
          </div>
        </div>

        {/* Nested Deep Inspector Panel */}
        <EventTicksDetails ticks={ticks} metrics={metrics} events={events} />
        
      </div>
    </div>
  );
}
