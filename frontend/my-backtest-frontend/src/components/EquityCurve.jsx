// src/components/EquityCurve.jsx

import React from "react";
import { Line } from "react-chartjs-2";
import { FaChartLine } from "react-icons/fa";
import Card from "./Card";
import { Chart, TimeScale, LinearScale, LineElement, PointElement, Tooltip, Legend, Title } from "chart.js";
import "chartjs-adapter-date-fns";

// Chart.js registration: only needs to be done once in the app; safe if repeated.
Chart.register(TimeScale, LinearScale, LineElement, PointElement, Tooltip, Legend, Title);

/**
 * Equity Curve Panel
 * - Renders backtest equity using Chart.js (via react-chartjs-2).
 * - Professional, clean, branded look.
 * - Empty-state message when no curve data is available.
 */
export default function EquityCurve({ curveData }) {
  const data = {
    labels: curveData.dates,
    datasets: [
      {
        label: "Equity Curve",
        data: curveData.values,
        fill: false,
        borderColor: "#00d2b8",
        backgroundColor: "#242d37",
        pointRadius: 2.5,
        tension: 0.22
      }
    ]
  };
  const options = {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: { mode: "index", intersect: false }
    },
    scales: {
      x: {
        type: "time",
        time: {
          unit: "week"
        },
        ticks: { color: "#bbb" },
        grid: { color: "#39393c" }
      },
      y: {
        beginAtZero: false,
        ticks: { color: "#bbb" },
        grid: { color: "#39393c" }
      }
    }
  };

  return (
    <Card title="Equity Curve" icon={<FaChartLine />}>
      {curveData.values && curveData.values.length === 0 ? (
        <div style={{ color: "#a1a1a8", padding: "1rem 0" }}>
          No curve data yet.
        </div>
      ) : (
        <Line data={data} options={options} height={240} />
      )}
    </Card>
  );
}
