// src/components/PipelineRunner.jsx

import React, { useState } from "react";
import { useRunPipeline } from "../hooks/useRunPipeline";

function PipelineRunner() {
  const [input, setInput] = useState("");
  const { data, loading, error, triggerPipeline } = useRunPipeline();

  const handleRun = () => {
    triggerPipeline({ value: input });
  };

  return (
    <div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter input for pipeline"
      />
      <button onClick={handleRun} disabled={loading}>Run Pipeline</button>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error.toString()}</p>}
      {data && (
        <div>
          <h4>Pipeline Output:</h4>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default PipelineRunner;
