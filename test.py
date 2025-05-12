import yfinance as yf
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from datetime import datetime


# Data fetching function supporting Yahoo Finance and CSV files
def fetch_data(
    source: str, ticker: str, start_date: str = None, file_path: str = None
) -> pd.DataFrame:
    if source == "Yahoo Finance":
        if not ticker or not start_date:
            raise ValueError("Ticker and start date are required for Yahoo Finance")
        df = yf.download(ticker, start=start_date)
    elif source == "CSV":
        if not file_path:
            raise ValueError("File path is required for CSV source")
        df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    else:
        raise ValueError(f"Unsupported data source: {source}")

    if df.empty:
        raise ValueError("No data returned. Check ticker or file contents.")
    return df


# Compute simple moving averages (50-day and 200-day by default)
def compute_moving_averages(
    df: pd.DataFrame, short_window: int = 50, long_window: int = 200
) -> pd.DataFrame:
    df["MA50"] = df["Close"].rolling(window=short_window).mean()
    df["MA200"] = df["Close"].rolling(window=long_window).mean()
    return df


# Compute the slope (price change per day) for the Gann 1x1 angle
def compute_gann_slope(df: pd.DataFrame) -> float:
    start_price = df["Close"].iloc[0]
    start_date = df.index[0]
    end_price = df["Close"].iloc[-1]
    end_date = df.index[-1]
    days = max((end_date - start_date).days, 1)
    slope = (end_price - start_price) / days
    return slope


# Overlay a Gann 1x1 line across the dataset
def compute_gann_line(df: pd.DataFrame) -> pd.DataFrame:
    start_price = df["Close"].iloc[0]
    start_date = df.index[0]
    slope = compute_gann_slope(df)
    df["GannLine"] = df.index.map(
        lambda d: start_price + slope * ((d - start_date).days)
    )
    return df


# Combined analysis: check price vs moving averages and Gann slope
def analyze_trend(df: pd.DataFrame) -> str:
    current_price = df["Close"].iloc[-1]
    ma50 = df["MA50"].iloc[-1]
    ma200 = df["MA200"].iloc[-1]
    slope = compute_gann_slope(df)

    if pd.notna(ma50) and pd.notna(ma200):
        if current_price > ma50 and ma50 > ma200 and slope > 0:
            return "Positive Trend"
        if current_price < ma50 and ma50 < ma200 and slope < 0:
            return "Negative Trend"
    return "Neutral/No Clear Trend"


# GUI setup
class StockAnalyzerApp:
    def __init__(self, root):
        self.root = root
        root.title("ניתוח מניות לפי גאן וממוצעים נעים")
        root.option_add("*font", "Arial 12")
        root.tk.call("tk", "scaling", 1.5)
        root.tk.call("tk", "useinputmethods", True)
        root.tk_setPalette(background="#f0f0f0")

        # Widgets for input (Right to Left)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        ttk.Label(root, text="מקור הנתונים:", anchor="e").grid(
            row=0, column=1, sticky=tk.E
        )
        self.source_var = tk.StringVar(value="Yahoo Finance")
        self.source_menu = ttk.Combobox(
            root,
            textvariable=self.source_var,
            values=["Yahoo Finance", "CSV"],
            state="readonly",
            justify="right",
        )
        self.source_menu.grid(row=0, column=0, sticky=tk.E)
        self.source_menu.bind("<<ComboboxSelected>>", self._on_source_change)

        ttk.Label(root, text="סימול/טיקר:", anchor="e").grid(
            row=1, column=1, sticky=tk.E
        )
        self.ticker_entry = ttk.Entry(root, justify="right")
        self.ticker_entry.grid(row=1, column=0, sticky=tk.E)

        ttk.Label(root, text="תאריך התחלה (YYYY-MM-DD):", anchor="e").grid(
            row=2, column=1, sticky=tk.E
        )
        self.start_entry = ttk.Entry(root, justify="right")
        self.start_entry.grid(row=2, column=0, sticky=tk.E)

        # CSV file selector (hidden by default)
        self.csv_button = ttk.Button(
            root, text="בחר קובץ CSV...", command=self._browse_csv
        )
        self.csv_path = None

        # Analyze button
        self.analyze_button = ttk.Button(root, text="נתח", command=self._on_analyze)
        self.analyze_button.grid(row=4, column=0, columnspan=2, pady=10)

    def _on_source_change(self, event=None):
        source = self.source_var.get()
        if source == "CSV":
            self.ticker_entry.config(state=tk.DISABLED)
            self.start_entry.config(state=tk.DISABLED)
            self.csv_button.grid(row=1, column=2)
        else:
            self.csv_button.grid_remove()
            self.ticker_entry.config(state=tk.NORMAL)
            self.start_entry.config(state=tk.NORMAL)

    def _browse_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.csv_path = path

    def _on_analyze(self):
        try:
            source = self.source_var.get()
            ticker = self.ticker_entry.get().strip()
            start_date = self.start_entry.get().strip()
            df = fetch_data(source, ticker, start_date, self.csv_path)
            df = compute_moving_averages(df)
            df = compute_gann_line(df)
            trend = analyze_trend(df)

            # Display recommendation
            messagebox.showinfo("תוצאת ניתוח", f"המלצה על סמך הניתוח: {trend}")

            # Plot results
            plt.figure(figsize=(12, 6))
            plt.plot(df["Close"], label="מחיר סגירה")
            plt.plot(df["MA50"], label="ממוצע נע 50")
            plt.plot(df["MA200"], label="ממוצע נע 200")
            plt.plot(df["GannLine"], label="קו גאן 1x1")
            plt.title(
                f"{ticker if source=='Yahoo Finance' else 'נתוני CSV'} - ניתוח מגמה"
            )
            plt.legend()
            plt.show()

        except Exception as e:
            messagebox.showerror("שגיאה", str(e))


# Run the GUI
def main():
    root = tk.Tk()
    app = StockAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
