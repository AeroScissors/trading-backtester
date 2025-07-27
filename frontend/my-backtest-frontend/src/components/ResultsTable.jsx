// src/components/ResultsTable.jsx

import React from "react";
import Card from "./Card";
import { FaTable } from "react-icons/fa";

/**
 * Results Table Panel
 * - Displays key metrics for each completed backtest.
 * - Uses Card layout, smart empty-state, and a table for professionalism.
 */
export default function ResultsTable({ results }) {
  return (
    <Card title="Backtest Results" icon={<FaTable />}>
      {!results || Object.keys(results).length === 0 ? (
        <div style={{ color: "#a1a1a8", padding: "1rem 0" }}>
          No results to display yet.
        </div>
      ) : (
        <table className="results-table">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(results).map(([metric, value]) => (
              <tr key={metric}>
                <td>{metric}</td>
                <td>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </Card>
  );
}
