"""
FUTURE_DS_03: Marketing Funnel & Conversion Performance Analysis
Module: Funnel Analytics Engine & Conversion Metrics Aggregator
Author: Future Interns - Data Science & Analytics Track
"""

import os
import json
import pandas as pd
import numpy as np


class FunnelAnalyticsEngine:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)

    def compute_executive_kpis(self) -> dict:
        """Calculates macro-level marketing and sales funnel metrics."""
        total_visitors = int(len(self.df))
        leads = int(self.df['Lead_Captured'].sum())
        mqls = int(self.df['MQL'].sum())
        sqls = int(self.df['SQL'].sum())
        opps = int(self.df['Opportunity'].sum())
        closed_won = int(self.df['Closed_Won'].sum())

        total_spend = round(float(self.df['Ad_Spend'].sum()), 2)
        total_revenue = round(float(self.df['Revenue'].sum()), 2)
        blended_roas = round(total_revenue / total_spend, 2) if total_spend > 0 else 0.0
        blended_cac = round(total_spend / closed_won, 2) if closed_won > 0 else 0.0
        cost_per_lead = round(total_spend / leads, 2) if leads > 0 else 0.0

        overall_conv_rate = round((closed_won / total_visitors) * 100, 2)
        lead_to_customer_rate = round((closed_won / leads) * 100, 2) if leads > 0 else 0.0
        avg_deal_size = round(total_revenue / closed_won, 2) if closed_won > 0 else 0.0
        avg_sales_cycle = round(float(self.df[self.df['Closed_Won'] == 1]['Sales_Cycle_Days'].mean()), 1)

        return {
            "total_visitors": total_visitors,
            "leads_captured": leads,
            "mqls": mqls,
            "sqls": sqls,
            "opportunities": opps,
            "closed_won": closed_won,
            "total_marketing_spend": total_spend,
            "total_revenue_won": total_revenue,
            "blended_roas": blended_roas,
            "blended_cac": blended_cac,
            "cost_per_lead": cost_per_lead,
            "visitor_to_customer_conv_rate_pct": overall_conv_rate,
            "lead_to_customer_conv_rate_pct": lead_to_customer_rate,
            "avg_deal_size": avg_deal_size,
            "avg_sales_cycle_days": avg_sales_cycle
        }

    def compute_stage_conversion_funnel(self) -> pd.DataFrame:
        """Computes stage-by-stage progression and drop-off rates."""
        stages = [
            ("Website Visitors", len(self.df)),
            ("Leads Captured", self.df['Lead_Captured'].sum()),
            ("Marketing Qualified (MQL)", self.df['MQL'].sum()),
            ("Sales Qualified (SQL)", self.df['SQL'].sum()),
            ("Opportunities (Demo/Proposal)", self.df['Opportunity'].sum()),
            ("Closed Won Deals", self.df['Closed_Won'].sum())
        ]
        funnel_df = pd.DataFrame(stages, columns=['Stage', 'Count'])
        funnel_df['Share_of_Total_Pct'] = ((funnel_df['Count'] / len(self.df)) * 100).round(2)
        
        # Progression from previous stage
        step_conv = [100.0]
        drop_off = [0.0]
        for i in range(1, len(funnel_df)):
            prev = funnel_df.loc[i-1, 'Count']
            curr = funnel_df.loc[i, 'Count']
            conv = round((curr / prev) * 100, 2) if prev > 0 else 0.0
            step_conv.append(conv)
            drop_off.append(round(100.0 - conv, 2))

        funnel_df['Step_Conversion_Pct'] = step_conv
        funnel_df['Step_Drop_Off_Pct'] = drop_off
        return funnel_df

    def analyze_channel_performance(self) -> pd.DataFrame:
        """Evaluates volume, spend, revenue, CAC, and ROAS across channels."""
        ch = self.df.groupby('Channel').agg(
            Visitors=('Lead_ID', 'count'),
            Leads=('Lead_Captured', 'sum'),
            Customers=('Closed_Won', 'sum'),
            Spend=('Ad_Spend', 'sum'),
            Revenue=('Revenue', 'sum')
        ).reset_index()

        ch['Spend'] = ch['Spend'].round(2)
        ch['Revenue'] = ch['Revenue'].round(2)
        ch['Visitor_to_Customer_Pct'] = ((ch['Customers'] / ch['Visitors']) * 100).round(2)
        ch['Lead_to_Customer_Pct'] = ((ch['Customers'] / ch['Leads']) * 100).round(2)
        ch['CAC'] = np.where(ch['Customers'] > 0, (ch['Spend'] / ch['Customers']).round(2), 0.0)
        ch['ROAS'] = np.where(ch['Spend'] > 0, (ch['Revenue'] / ch['Spend']).round(2), 0.0)
        return ch.sort_values('Revenue', ascending=False)

    def analyze_loss_reasons(self) -> pd.DataFrame:
        """Audits loss reasons among lost opportunities."""
        opp_lost = self.df[(self.df['Opportunity'] == 1) & (self.df['Closed_Won'] == 0)]
        reasons = opp_lost['Lost_Reason'].value_counts().reset_index()
        reasons.columns = ['Reason', 'Count']
        reasons['Share_Pct'] = ((reasons['Count'] / len(opp_lost)) * 100).round(2)
        return reasons

    def export_metrics_json(self, output_path: str):
        """Exports funnel KPI metrics to JSON for web dashboards."""
        kpis = self.compute_executive_kpis()
        funnel_df = self.compute_stage_conversion_funnel()
        ch_df = self.analyze_channel_performance()
        loss_df = self.analyze_loss_reasons()

        data = {
            **kpis,
            "funnel_stages": funnel_df['Stage'].tolist(),
            "funnel_counts": funnel_df['Count'].tolist(),
            "funnel_step_conv": funnel_df['Step_Conversion_Pct'].tolist(),
            "funnel_drop_off": funnel_df['Step_Drop_Off_Pct'].tolist(),
            "channels": ch_df['Channel'].tolist(),
            "channel_spend": ch_df['Spend'].tolist(),
            "channel_revenue": ch_df['Revenue'].tolist(),
            "channel_cac": ch_df['CAC'].tolist(),
            "channel_roas": ch_df['ROAS'].tolist(),
            "channel_conv_rates": ch_df['Visitor_to_Customer_Pct'].tolist(),
            "loss_reasons": loss_df['Reason'].tolist(),
            "loss_counts": loss_df['Count'].tolist()
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"[+] Funnel metrics exported to: {output_path}")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    clean_csv = os.path.join(base_dir, 'data', 'cleaned_marketing_funnel_data.csv')
    json_path = os.path.join(base_dir, 'dashboards', 'funnel_metrics.json')
    engine = FunnelAnalyticsEngine(clean_csv)
    engine.export_metrics_json(json_path)
