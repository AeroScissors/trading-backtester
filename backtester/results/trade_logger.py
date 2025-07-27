import csv

class TradeLogger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, trades):
        with open(self.log_path, 'w', newline='') as csvfile:
            fieldnames = ['date', 'action', 'price', 'quantity', 'cash', 'position']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for trade in trades:
                writer.writerow(trade)
