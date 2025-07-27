// src/api/apiClient.js

export const runPipeline = async (inputData) => {
  const res = await fetch("http://localhost:8000/api/run-pipeline", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(inputData),
  });
  return res.json();
};
