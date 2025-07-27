// src/features/ResultsViewer/ResultsViewer.jsx
import React from "react";
import Card from "../../components/Card";
import EquityCurve from "../../components/EquityCurve";
import ResultsTable from "../../components/ResultsTable";
import TradeMarksChart from "../../components/TradeMarksChart";

export default function ResultsViewer() {
  return (
    <div>
      <h2>Results Viewer</h2>

      <div className="results-grid">
        <Card title="Equity Curve">
          <EquityCurve />
        </Card>

        <Card title="Trade Marks Chart">
          <TradeMarksChart />
        </Card>

        <Card title="Results Table">
          <ResultsTable />
        </Card>
      </div>
    </div>
  );
}
