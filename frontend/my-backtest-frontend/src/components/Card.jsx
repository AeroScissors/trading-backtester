import React from "react";
import "./Card.css";

/**
 * Reusable, stylized card container for UI sections.
 * - Optional title, icon, and footer.
 * - Ensures visual consistency and polished spacing.
 */
const Card = ({ title, icon, children, footer }) => (
  <section className="card">
    {title && (
      <header className="card-title">
        {icon && <span className="card-icon">{icon}</span>}
        <span>{title}</span>
      </header>
    )}
    <div className="card-content">{children}</div>
    {footer && <footer className="card-footer">{footer}</footer>}
  </section>
);

export default Card;
