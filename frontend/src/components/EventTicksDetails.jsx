import React, { useState } from "react";
import { BarChart2, List, Search, Filter, Trophy, HelpCircle, Activity } from "lucide-react";

export default function EventTicksDetails({ ticks, metrics, events }) {
  const [activeTab, setActiveTab] = useState("logs");
  const [searchTerm, setSearchTerm] = useState("");
  const [filterType, setFilterType] = useState("all");

  // Filter logic for the audit log
  const filteredEvents = events.filter((evt) => {
    const matchesSearch = evt.text.toLowerCase().includes(searchTerm.toLowerCase()) || evt.id.toString().includes(searchTerm);
    const matchesFilter = filterType === "all" || evt.type === filterType;
    return matchesSearch && matchesFilter;
  });

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-6 shadow-xl">
      {/* Component Header & Tab Switcher */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-slate-800 pb-4 mb-6">
        <div>
          <h2 className="text-lg font-bold text-teal-400 flex items-center gap-2">
            <Activity size={20} /> Event Stream Deep Inspector
          </h2>
          <p className="text-xs text-slate-400 font-mono mt-0.5">Telemetry grounding: {ticks} sequential match ticks processed</p>
        </div>
        
        {/* Navigation Tabs */}
        <div className="flex bg-slate-950 p-1 rounded-lg border border-slate-800 self-stretch sm:self-auto">
          <button
            onClick={() => setActiveTab("logs")}
            className={`flex items-center justify-center gap-1.5 px-4 py-1.5 text-xs font-medium rounded-md transition-all ${
              activeTab === "logs" ? "bg-teal-500 text-slate-950 font-semibold shadow-md" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            <List size={14} /> Audit Log
          </button>
          <button
            onClick={() => setActiveTab("metrics")}
            className={`flex items-center justify-center gap-1.5 px-4 py-1.5 text-xs font-medium rounded-md transition-all ${
              activeTab === "metrics" ? "bg-amber-500 text-slate-950 font-semibold shadow-md" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            <BarChart2 size={14} /> Metric Analytics
          </button>
        </div>
      </div>

      {/* TAB 1: DETAILED AUDIT LOG VIEW */}
      {activeTab === "logs" && (
        <div className="space-y-4">
          {/* Search & Filter Controls Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="relative sm:col-span-2">
              <Search className="absolute left-3 top-2.5 size-4 text-slate-500" />
              <input
                type="text"
                placeholder="Search tick ID or tactical pattern description..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-xs font-mono focus:outline-none focus:border-teal-500 text-slate-200"
              />
            </div>
            <div className="relative">
              <Filter className="absolute left-3 top-2.5 size-4 text-slate-500" />
              <select
                value={filterType}
                onChange={(e) => setFilterType(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-3 py-2 text-xs font-mono focus:outline-none focus:border-teal-500 text-slate-300 appearance-none cursor-pointer"
              >
                <option value="all">All Events</option>
                <option value="pass">Passes Only</option>
                <option value="shot">Shots Only</option>
                <option value="foul">Match Fouls</option>
              </select>
            </div>
          </div>

          {/* Scrollable Logs Grid Container */}
          <div className="border border-slate-800/60 rounded-lg overflow-hidden bg-slate-950/40">
            <div className="max-h-[300px] overflow-y-auto divide-y divide-slate-900 font-mono text-xs pr-1">
              {filteredEvents.length > 0 ? (
                filteredEvents.map((evt) => (
                  <div
                    key={evt.id}
                    className={`p-3 transition-colors flex items-start gap-4 ${
                      evt.type === "pass" ? "hover:bg-emerald-950/10" :
                      evt.type === "shot" ? "hover:bg-sky-950/10" : "hover:bg-rose-950/10"
                    }`}
                  >
                    <span className="text-slate-500 font-bold shrink-0">#{evt.id}</span>
                    <div className="flex-1">
                      <div className="flex justify-between items-center mb-1">
                        <span className={`text-[10px] px-2 py-0.5 rounded-full border uppercase tracking-wider font-semibold ${
                          evt.type === "pass" ? "bg-emerald-950/40 border-emerald-800/40 text-emerald-400" :
                          evt.type === "shot" ? "bg-sky-950/40 border-sky-800/40 text-sky-400" :
                          "bg-rose-950/40 border-rose-800/40 text-rose-400"
                        }`}>
                          {evt.type}
                        </span>
                        <span className="text-[10px] text-slate-600">Verified Payload</span>
                      </div>
                      <p className="text-slate-300 leading-relaxed text-[11px]">{evt.text}</p>
                    </div>
                  </div>
                ))
              ) : (
                <div className="p-8 text-center text-slate-500 text-xs italic">
                  No synthetic ticks found matching active filtering constraints.
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: ADVANCED STATISTICAL METRICS BREAKDOWN */}
      {activeTab === "metrics" && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Traditional Ingestion Volume Logs */}
          <div className="space-y-3">
            <h3 className="text-xs uppercase font-bold text-slate-400 tracking-wider mb-2">Deterministic Count Matrices</h3>
            <div className="bg-slate-950 border border-slate-800/60 p-3 rounded-lg flex justify-between items-center font-mono text-xs">
              <span className="text-slate-400">Total Completed Passes</span>
              <span className="text-emerald-400 font-bold text-sm">{metrics.totalPasses}</span>
            </div>
            <div className="bg-slate-950 border border-slate-800/60 p-3 rounded-lg flex justify-between items-center font-mono text-xs">
              <span className="text-slate-400">Shot Volume Multipliers</span>
              <span className="text-sky-400 font-bold text-sm">{metrics.totalShots}</span>
            </div>
            <div className="bg-slate-950 border border-slate-800/60 p-3 rounded-lg flex justify-between items-center font-mono text-xs">
              <span className="text-slate-400">Cynical Disruptions</span>
              <span className="text-rose-400 font-bold text-sm">{metrics.totalFouls}</span>
            </div>
            <div className="bg-slate-950 border border-slate-800/60 p-3 rounded-lg flex justify-between items-center font-mono text-xs">
              <span className="text-slate-400">Aggregated Probability Model</span>
              <span className="text-purple-400 font-bold text-sm">{metrics.expectedGoalsXG} xG</span>
            </div>
          </div>

          {/* Hackathon Highlight Feature Box: CTIE Mathematical Formula Audit */}
          <div className="bg-amber-950/10 border border-amber-900/30 rounded-lg p-4 flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-xs uppercase font-bold text-amber-400 tracking-wider flex items-center gap-1.5">
                  <Trophy size={14} /> CTIE Award Logic Blueprint
                </h3>
                <span className="bg-amber-950 text-amber-400 text-[10px] font-mono px-2 py-0.5 rounded border border-amber-800/40">
                  Tool: engine.py
                </span>
              </div>
              <p className="text-[11px] text-amber-200/70 font-mono leading-relaxed mb-4">
                Calculated dynamically via Python tool binding:
                <br />
                <span className="text-slate-400">Base Plane:</span> 50.0 
                <br />
                <span className="text-emerald-400">Bonuses:</span> +0.5 per Pass / +2.0 per Shot 
                <br />
                <span className="text-rose-400">Penalties:</span> -4.0 per Foul / -12.0 per Card
              </p>
            </div>

            <div className="bg-slate-950/80 border border-slate-800 p-3 rounded-md flex justify-between items-center mt-auto font-mono">
              <div className="flex items-center gap-1.5 text-xs text-amber-300">
                <HelpCircle size={13} className="text-amber-400" />
                <span>Computed Score</span>
              </div>
              <span className="text-amber-400 text-lg font-bold">{metrics.ctieAwardScore}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
