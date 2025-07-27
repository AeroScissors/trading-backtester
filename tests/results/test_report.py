from backtester.results import report

def test_export_metrics_csv(tmp_path):
    metrics = {'sharpe': 1.5, 'drawdown': -0.12}
    file = tmp_path / "metrics.csv"
    report.export_metrics_csv(metrics, str(file))
    assert file.exists()

def test_generate_summary_pdf(tmp_path):
    metrics = {'sharpe': 1.5, 'drawdown': -0.12}
    file = tmp_path / "report.pdf"
    # Use dummy chart; empty white PNG or similar can be substituted if needed in actual run
    report.generate_summary_pdf(metrics, [], str(file))
    assert file.exists()
