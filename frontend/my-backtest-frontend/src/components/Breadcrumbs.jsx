import React from "react";
import "./Breadcrumbs.css";

// Simple breadcrumbs accepting an array of {label, onClick?, active} items
export default function Breadcrumbs({ items }) {
  return (
    <nav className="breadcrumbs" aria-label="breadcrumb">
      {items.map((item, i) => (
        <span key={i} className={item.active ? "breadcrumb-active" : "breadcrumb"} onClick={item.onClick}>
          {item.label}
          {i !== items.length - 1 && <span className="breadcrumb-sep">{'>'}</span>}
        </span>
      ))}
    </nav>
  );
}
