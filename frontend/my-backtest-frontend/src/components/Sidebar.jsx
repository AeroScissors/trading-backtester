// src/components/Sidebar.jsx

import React from "react";
import { FaDatabase, FaCode, FaCogs, FaChartLine } from "react-icons/fa";
import "./Sidebar.css";

const NAV_LINKS = [
  { key: "data", label: "Data Upload", icon: <FaDatabase /> },
  { key: "strategy", label: "Strategy Editor", icon: <FaCode /> },
  { key: "indicator", label: "Indicator Builder", icon: <FaCogs /> },
  { key: "results", label: "Results Viewer", icon: <FaChartLine /> }
];

export default function Sidebar({ currentPage, setPage }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <img
          src="/assets/logo.svg" // Update path as needed for your asset
          className="sidebar-logo"
          alt="App Logo"
        />
        <span className="sidebar-title">TradeBacktest</span>
      </div>
      <nav className="sidebar-nav">
        {NAV_LINKS.map(link => (
          <button
            key={link.key}
            className={`nav-link${currentPage === link.key ? " active" : ""}`}
            onClick={() => setPage(link.key)}
            type="button"
            aria-current={currentPage === link.key ? "page" : undefined}
          >
            <span className="nav-icon">{link.icon}</span>
            <span>{link.label}</span>
          </button>
        ))}
      </nav>
      <div className="sidebar-footer">©2025</div>
    </aside>
  );
}
