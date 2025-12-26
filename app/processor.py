import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.loader import fetch_dataset
from analyzer.rules import assess_risk

def process():
    df = fetch_dataset(size=500)
    df = assess_risk(df)
    return df