// src/hooks/useRunPipeline.js

import { useState } from "react";
import { runPipeline } from "../api/apiClient";

export function useRunPipeline() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const triggerPipeline = async (inputData) => {
    setLoading(true);
    setError(null);
    try {
      const result = await runPipeline(inputData);
      setData(result);
    } catch (err) {
      setError(err);
    }
    setLoading(false);
  };

  return { data, loading, error, triggerPipeline };
}
