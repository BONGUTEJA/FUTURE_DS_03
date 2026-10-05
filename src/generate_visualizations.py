"""
FUTURE_DS_03: Marketing Funnel & Conversion Performance Analysis
Module: Visualization Generator for Funnel & CRO Analytics
Author: Future Interns - Data Science & Analytics Track
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8


def generate_all_figures(clean_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(clean_path)

    # 1. Overall Funnel Stage Conversion
    plt.figure(figsize=(11, 6))
    stages = [
        "1. Visitors", "2. Leads Captured", "3. MQL",
        "4. SQL", "5. Opportunities", "6. Closed Won"
    ]
    counts = [
        len(df),
        df['Lead_Captured'].sum(),
        df['MQL'].sum(),
        df['SQL'].sum(),
        df['Opportunity'].sum(),
        df['Closed_Won'].sum()
    ]
    colors = ['#3B82F6', '#60A5FA', '#818CF8', '#A78BFA', '#C084FC', '#10B981']
    bars = plt.barh(stages[::-1], counts[::-1], color=colors[::-1], edgecolor='#1E293B', height=0.55)
    plt.title('Enterprise Marketing & Sales Funnel Progression', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Volume (Count of Prospects)', fontsize=11)
    for i, bar in enumerate(bars):
        w = bar.get_width()
        pct_of_total = (w / len(df)) * 100
        plt.text(w + 120, bar.get_y() + bar.get_height() / 2, f'{w:,} ({pct_of_total:.1f}%)', va='center', fontweight='bold', fontsize=10)
    plt.xlim(0, max(counts) * 1.15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_overall_funnel_stage_conversion.png'), dpi=300)
    plt.close()

    # 2. Channel Conversion Rate Comparison
    plt.figure(figsize=(10, 5))
    ch_conv = df.groupby('Channel').apply(
        lambda g: (g['Closed_Won'].sum() / len(g)) * 100
    ).sort_values(ascending=False)
    bars = plt.bar(ch_conv.index, ch_conv.values, color='#3B82F6', edgecolor='#1D4ED8', width=0.55)
    plt.xticks(rotation=25, ha='right', fontsize=10)
    plt.title('Visitor-to-Customer Conversion Rate by Channel (%)', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Conversion Rate (%)', fontsize=11)
    plt.ylim(0, max(ch_conv.values) * 1.25)
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, h + 0.15, f'{h:.2f}%', ha='center', fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_channel_conversion_comparison.png'), dpi=300)
    plt.close()

    # 3. ROAS & CAC by Channel
    plt.figure(figsize=(11, 5))
    ch_fin = df.groupby('Channel').agg({'Ad_Spend': 'sum', 'Revenue': 'sum', 'Closed_Won': 'sum'}).reset_index()
    ch_fin['ROAS'] = ch_fin['Revenue'] / ch_fin['Ad_Spend']
    ch_fin = ch_fin.sort_values('ROAS', ascending=False)
    bars = plt.bar(ch_fin['Channel'], ch_fin['ROAS'], color=['#10B981' if r >= 3.0 else '#F59E0B' for r in ch_fin['ROAS']], edgecolor='#333333', width=0.55)
    plt.axhline(3.0, color='red', linestyle='--', label='Target ROAS Benchmark (3.0x)')
    plt.xticks(rotation=25, ha='right', fontsize=10)
    plt.title('Return on Ad Spend (ROAS) Across Marketing Channels', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('ROAS Multiplier (Revenue / Ad Spend)', fontsize=11)
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, h + 0.15, f'{h:.2f}x', ha='center', fontweight='bold', fontsize=10)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_roas_and_cac_by_channel.png'), dpi=300)
    plt.close()

    # 4. Monthly Funnel Revenue Trajectory
    plt.figure(figsize=(12, 5))
    monthly = df.groupby('YearMonth').agg({'Closed_Won': 'sum', 'Revenue': 'sum'}).reset_index()
    x = range(len(monthly))
    plt.plot(x, monthly['Revenue'] / 1e3, marker='o', color='#2563EB', linewidth=2.5, label='Closed Revenue ($k)')
    plt.bar(x, monthly['Closed_Won'], alpha=0.3, color='#10B981', label='Deals Won')
    plt.xticks(ticks=x, labels=monthly['YearMonth'], rotation=45, ha='right', fontsize=9)
    plt.title('Monthly Sales Pipeline Velocity & Revenue (2024 - 2025)', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Revenue ($k USD) / Deals Won', fontsize=11)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_monthly_funnel_velocity_trend.png'), dpi=300)
    plt.close()

    # 5. Opportunity Loss Reasons (Pareto)
    plt.figure(figsize=(11, 5))
    lost_opps = df[(df['Opportunity'] == 1) & (df['Closed_Won'] == 0)]
    reasons = lost_opps['Lost_Reason'].value_counts()
    bars = plt.barh(reasons.index[::-1], reasons.values[::-1], color='#F87171', edgecolor='#991B1B')
    plt.title('Primary Reasons for Lost Sales Opportunities (Bottlenecks)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Count of Lost Opportunities', fontsize=11)
    for bar in bars:
        w = bar.get_width()
        plt.text(w + 2, bar.get_y() + bar.get_height() / 2, f'{w}', va='center', fontweight='bold', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_deal_loss_reasons_breakdown.png'), dpi=300)
    plt.close()

    # 6. Device Type Conversion Performance
    plt.figure(figsize=(9, 5))
    dev = df.groupby('Device_Type').agg(
        Visitors=('Lead_ID', 'count'),
        Won=('Closed_Won', 'sum')
    ).reset_index()
    dev['Conv_Rate'] = (dev['Won'] / dev['Visitors']) * 100
    bars = plt.bar(dev['Device_Type'], dev['Conv_Rate'], color=['#3B82F6', '#8B5CF6', '#EC4899'], width=0.45)
    plt.title('Conversion Rate by Device Type (%)', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Visitor-to-Customer Conversion (%)', fontsize=11)
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, h + 0.1, f'{h:.2f}%', ha='center', fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '06_device_conversion_performance.png'), dpi=300)
    plt.close()

    print(f"[+] All 6 figures generated successfully in: {output_dir}")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    clean_csv = os.path.join(base_dir, 'data', 'cleaned_marketing_funnel_data.csv')
    fig_dir = os.path.join(base_dir, 'reports', 'figures')
    generate_all_figures(clean_csv, fig_dir)
