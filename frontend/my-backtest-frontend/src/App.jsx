// src/App.jsx

import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import DataUpload from "./features/DataInput/DataUpload";
import StrategyEditor from "./features/StrategyEditor/StrategyEditor";
import ResultsTable from "./components/ResultsTable";
import EquityCurve from "./components/EquityCurve";
import "./App.css";

/**
 * Main App Shell — routes and composes all feature sections.
 * File paths now fully reflect your actual management for maximum clarity and zero import errors.
 */
export default function App() {
  // Which main page/view is active (dashboard, data, strategy, results, etc)
  const [page, setPage] = useState("dashboard");

  // States for data and results (integrate with backend as needed)
  const [dataFile, setDataFile] = useState(null);
  const [strategy, setStrategy] = useState("");
  const [results, setResults] = useState({});
  const [equityCurve, setEquityCurve] = useState({ dates: [], values: [] });

  // Main render function for current page
  function renderMainContent() {
    switch (page) {
      case "data":
        return (
          <DataUpload
            onUpload={(file) => {
              setDataFile(file);
              // ...backend-upload/file-relay logic goes here
            }}
          />
        );
      case "strategy":
        return (
          <StrategyEditor
            onSave={(code) => {
              setStrategy(code);
              // ...backend-save/update logic goes here
            }}
          />
        );
      case "results":
        return (
          <>
            <ResultsTable results={results} />
            <br />
            <EquityCurve curveData={equityCurve} />
          </>
        );
      case "dashboard":
      default:
        return (
          <section style={{ padding: "2rem" }}>
            <h2>
              Welcome to{" "}
              <span style={{ color: "#00d2b8" }}>TradeBacktest</span>!
            </h2>
            <p style={{ color: "#ccc", maxWidth: 600 }}>
              Upload your historical data and try out your first trading strategy backtest. Results will appear here when you run a test. Use the sidebar to navigate between key tools.
            </p>
          </section>
        );
    }
  }

  return (
    <div className="app-shell">
      <Sidebar currentPage={page} setPage={setPage} />
      <main className="main-content">{renderMainContent()}</main>
    </div>
  );
}
