import React, { useEffect, useState } from 'react';

const BestParamsTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    fetch('/api/results/outputs/best_params.csv')
      .then((r) => r.text())
      .then((csvText) => {
        const lines = csvText.trim().split('\n');
        const headers = lines[0].split(',');
        const data = lines.slice(1).map(
          line => Object.fromEntries(line.split(',').map((val, i) => [headers[i], val]))
        );
        setRows(data);
      });
  }, []);

  if (rows.length === 0) return <div>Loading...</div>;
  return (
    <table>
      <thead>
        <tr>
          {Object.keys(rows[0]).map((col) => <th key={col}>{col}</th>)}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, idx) => (
          <tr key={idx}>
            {Object.values(row).map((val, j) => <td key={j}>{val}</td>)}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default BestParamsTable;
