"""
FUTURE_DS_03: Marketing Funnel & Conversion Performance Analysis
Module: Data Preprocessing & Funnel Feature Engineering
Author: Future Interns - Data Science & Analytics Track
"""

import os
import pandas as pd
import numpy as np


def clean_and_prepare_funnel_data(raw_path: str, clean_path: str = None) -> pd.DataFrame:
    """
    Ingests raw marketing funnel records, sanitizes data fields,
    derives temporal features, highest funnel stage achieved,
    and calculates attribution metrics.
    """
    print(f"[*] Ingesting raw funnel data from: {raw_path}")
    df = pd.read_csv(raw_path)

    # 1. Clean strings
    text_cols = ['Channel', 'Campaign', 'Device_Type', 'Drop_Off_Stage', 'Lost_Reason']
    for c in text_cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()

    # 2. Date parsing and temporal dimensions
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['YearMonth'] = df['Date'].dt.strftime('%Y-%m')
    df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

    # 3. Numeric validation
    numeric_cols = ['Ad_Spend', 'Revenue', 'Sales_Cycle_Days']
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0).round(2)

    # 4. Highest Funnel Stage Achieved
    def get_highest_stage(r):
        if r['Closed_Won'] == 1:
            return 'Closed Won'
        elif r['Opportunity'] == 1:
            return 'Opportunity'
        elif r['SQL'] == 1:
            return 'SQL'
        elif r['MQL'] == 1:
            return 'MQL'
        elif r['Lead_Captured'] == 1:
            return 'Lead Captured'
        else:
            return 'Visitor (Bounced)'

    df['Highest_Stage'] = df.apply(get_highest_stage, axis=1)

    # 5. Funnel Stage Index (1 to 6)
    stage_idx_map = {
        'Visitor (Bounced)': 1,
        'Lead Captured': 2,
        'MQL': 3,
        'SQL': 4,
        'Opportunity': 5,
        'Closed Won': 6
    }
    df['Stage_Index'] = df['Highest_Stage'].map(stage_idx_map)

    # Sort chronologically
    df = df.sort_values('Date').reset_index(drop=True)

    if clean_path:
        os.makedirs(os.path.dirname(clean_path), exist_ok=True)
        df.to_csv(clean_path, index=False)
        print(f"[+] Cleaned marketing funnel dataset exported to: {clean_path} ({len(df):,} records)")

    return df


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_csv = os.path.join(base_dir, 'data', 'raw_marketing_funnel_data.csv')
    clean_csv = os.path.join(base_dir, 'data', 'cleaned_marketing_funnel_data.csv')
    clean_and_prepare_funnel_data(raw_csv, clean_csv)
