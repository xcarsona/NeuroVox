import pandas as pd

def clean_text_column(df, text_col):
    df = df.copy()
    df[text_col] = df[text_col].astype(str).str.lower()
    df = df.dropna(subset=[text_col])
    return df
