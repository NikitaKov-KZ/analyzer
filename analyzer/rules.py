import pandas as pd
import sys
import os
import streamlit as st
import pandas as pd

def flag_high_price(df, threshold=1.5, absolute_limit=100_000_000):
    avg = df.groupby("item")["price"].transform("mean")
    return (df["price"] > avg * threshold) | (df["price"] > absolute_limit)

def flag_repeat_winner(df, count=3):
    return df.groupby(["customer", "supplier"]).cumcount() >= count

def flag_fragmentation(df, max_price=100000, min_lots=3):
    group_counts = df.groupby(["customer", "date"]).size().reset_index(name="lot_count")
    df_merged = df.merge(group_counts, on=["customer", "date"], how="left")
    return (df_merged["lot_count"] >= min_lots) & (df_merged["price"] < max_price)

def flag_low_competition(df):
    return df["num_participants"] <= 1

def assess_risk(df: pd.DataFrame) -> pd.DataFrame:
    df["high_price"] = flag_high_price(df)
    df["repeat_winner"] = flag_repeat_winner(df)
    df["fragmentation"] = flag_fragmentation(df)
    df["low_competition"] = flag_low_competition(df)
    df["risk_score"] = df[["high_price", "repeat_winner", "fragmentation", "low_competition"]].sum(axis=1)
    df["risk_level"] = pd.cut(df["risk_score"], bins=[-1,0,1,3,4], labels=["green","yellow","orange","red"])
    return df