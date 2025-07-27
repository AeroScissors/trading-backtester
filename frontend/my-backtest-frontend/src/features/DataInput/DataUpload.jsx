import React, { useRef, useState } from "react";
import Card from "../../components/Card";
import { FaCloudUploadAlt } from "react-icons/fa";

/**
 * Market Data Upload Panel
 * - Drag-and-drop or click to select CSV files for backtesting.
 * - Shows uploaded file name or error if invalid.
 */
export default function DataUpload({ onUpload }) {
  const fileRef = useRef();
  const [dragging, setDragging] = useState(false);
  const [fileName, setFileName] = useState("");
  const [error, setError] = useState("");

  function handleFile(file) {
    setFileName(file.name);
    setError("");
    onUpload(file); // pass back up to parent app
  }

  function onDrop(e) {
    e.preventDefault();
    setDragging(false);
    const files = e.dataTransfer.files;
    if (files && files.length) {
      if (!files[0].name.endsWith(".csv")) {
        setError("Please upload a CSV file.");
      } else {
        handleFile(files[0]);
      }
    }
  }

  return (
    <Card
      title="Upload Market Data"
      icon={<FaCloudUploadAlt />}
    >
      <div
        className={`upload-box${dragging ? " drag-active" : ""}`}
        onDragEnter={() => setDragging(true)}
        onDragLeave={() => setDragging(false)}
        onDragOver={e => e.preventDefault()}
        onDrop={onDrop}
        style={{
          border: "2px dashed #00d2b8",
          borderRadius: "8px",
          padding: "2rem",
          textAlign: "center",
          background: dragging ? "#1a2731" : "#181926",
          marginBottom: "1rem"
        }}
      >
        <input
          type="file"
          ref={fileRef}
          style={{ display: "none" }}
          accept=".csv"
          onChange={e => {
            const file = e.target.files[0];
            if (file) handleFile(file);
          }}
        />
        <button
          className="btn"
          onClick={() => fileRef.current.click()}
          type="button"
        >
          Select CSV File
        </button>
        <p style={{ margin: "14px 0 0 0", color: "#bbb" }}>
          or drag & drop here
        </p>
        {fileName && <div className="file-msg">Uploaded: {fileName}</div>}
        {error && <div className="error-msg">{error}</div>}
      </div>
    </Card>
  );
}
