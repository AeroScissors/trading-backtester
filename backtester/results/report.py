import csv
import os
from fpdf import FPDF
from datetime import datetime

def export_metrics_csv(metrics, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Metric', 'Value'])
        for key, value in metrics.items():
            writer.writerow([key, value])

def export_charts_png(chart_paths, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for chart_path in chart_paths:
        # Assume charts are already saved as images by visualizer.py
        # Here, possibly copy/move to output_dir if necessary
        pass

def generate_summary_pdf(metrics, chart_files, out_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.cell(200, 10, "Backtest Summary Report", ln=1, align='C')
    pdf.ln(10)
    
    # Table of Metrics
    pdf.cell(0, 10, "Performance Metrics:", ln=1)
    for k, v in metrics.items():
        pdf.cell(0, 10, f"{k} : {v}", ln=1)
    pdf.ln(5)
    
    # Charts
    for chart_img in chart_files:
        pdf.image(chart_img, w=180)
        pdf.ln(5)
    
    pdf.output(out_path)

# Example usage:
# export_metrics_csv(metrics_dict, "metrics.csv")
# generate_summary_pdf(metrics_dict, ["equity_curve.png", "trades.png"], "report.pdf")
