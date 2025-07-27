import React from 'react';
import BestParamsTable from './BestParamsTable';
import ParamSurfaceChart from './ParamSurfaceChart';

const ResultsViewer = () => (
  <div>
    <h2>Parameter Optimization Results</h2>
    <BestParamsTable />
    <ParamSurfaceChart />
  </div>
);

export default ResultsViewer;
