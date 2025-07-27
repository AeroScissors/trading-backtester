import React, { useState, useEffect } from 'react';
import EquityCurve from '../components/EquityCurve';
import TradeMarksChart from '../components/TradeMarksChart';
import ResultsTable from '../components/ResultsTable';

export default function ResultsViewer() {
  const [equityData, setEquityData] = useState(null);
  const [tradeData, setTradeData] = useState(null);
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetch('/api/results/equity-curve').then(r => r.json()).then(setEquityData);
    fetch('/api/results/trades').then(r => r.json()).then(setTradeData);
    fetch('/api/results/metrics').then(r => r.json()).then(setMetrics);
  }, []);

  if (!equityData || !tradeData || !metrics) return <div>Loading...</div>;

  return (
    <div>
      <h1>Backtest Results</h1>
      <ResultsTable metrics={metrics} />
      <EquityCurve data={equityData} />
      <TradeMarksChart priceData={tradeData.price} trades={tradeData.trades} />
      <div style={{ marginTop: "16px" }}>
        <a href="/api/results/metrics/csv" download>Download CSV</a> | 
        <a href="/api/results/report/pdf" download>Download PDF</a>
      </div>
    </div>
  );
}
