import React, { useState } from "react";
import Card from "../components/Card";
import { FaCogs } from "react-icons/fa";
import "./IndicatorBuilder.css";

/**
 * Indicator Builder Panel
 * - Lets user select, configure, and add technical indicators.
 * - Ready for extensibility (add input fields/types as needed).
 */
const AVAILABLE_INDICATORS = [
  { key: "sma", label: "Simple Moving Average (SMA)" },
  { key: "ema", label: "Exponential Moving Average (EMA)" },
  { key: "rsi", label: "Relative Strength Index (RSI)" }
];

export default function IndicatorBuilder({ onAdd }) {
  const [indicator, setIndicator] = useState(AVAILABLE_INDICATORS[0].key);
  const [length, setLength] = useState(14);

  function handleAdd(e) {
    e.preventDefault();
    onAdd({ type: indicator, params: { length } });
  }

  return (
    <Card title="Indicator Builder" icon={<FaCogs />}>
      <form className="indicator-form" onSubmit={handleAdd}>
        <label>
          <span className="indicator-label">Indicator</span>
          <select
            value={indicator}
            onChange={e => setIndicator(e.target.value)}
            className="indicator-select"
          >
            {AVAILABLE_INDICATORS.map(i => (
              <option key={i.key} value={i.key}>{i.label}</option>
            ))}
          </select>
        </label>
        <label>
          <span className="indicator-label">Length/Period</span>
          <input
            type="number"
            min={2}
            max={200}
            value={length}
            onChange={e => setLength(Number(e.target.value))}
            className="indicator-input"
            required
          />
        </label>
        <button className="btn" type="submit">
          Add Indicator
        </button>
      </form>
    </Card>
  );
}
