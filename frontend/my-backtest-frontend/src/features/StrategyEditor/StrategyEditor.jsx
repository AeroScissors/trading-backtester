import React, { useState } from "react";
import Card from "../../components/Card";
import { FaCode } from "react-icons/fa";

/**
 * Strategy Editor Panel
 * - Allows user to enter or paste strategy logic.
 * - Modern, comfortable code textarea.
 * - Save button with feedback.
 */
export default function StrategyEditor({ onSave }) {
  const [code, setCode] = useState("// Write your entry/exit logic...");
  const [message, setMessage] = useState("");

  return (
    <Card title="Strategy Editor" icon={<FaCode />}>
      <textarea
        value={code}
        rows={13}
        style={{
          width: "100%",
          background: "#191927",
          color: "#f3f6f8",
          borderRadius: "7px",
          border: "1.5px solid #22223c",
          fontSize: "1.06rem",
          padding: "1rem",
          fontFamily: "Inconsolata, Menlo, monospace"
        }}
        onChange={e => setCode(e.target.value)}
        spellCheck={false}
        autoCorrect="off"
        autoComplete="off"
      />
      <div style={{ marginTop: "1rem" }}>
        <button
          className="btn code"
          onClick={() => {
            onSave(code);
            setMessage("Saved!");
            setTimeout(() => setMessage(""), 1300);
          }}
        >
          Save Strategy
        </button>
        {message && (
          <span style={{ color: "#00d2b8", marginLeft: 16 }}>{message}</span>
        )}
      </div>
    </Card>
  );
}
