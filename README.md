# FUTURE_DS_03: Marketing Funnel & Conversion Performance Analysis

[![Track: Data Science & Analytics](https://img.shields.io/badge/Track-Data%20Science%20%26%20Analytics-blue.svg)](https://futureinterns.com/)
[![Project: Task 03](https://img.shields.io/badge/Task-03%20Funnel%20%26%20Conversion-purple.svg)](https://futureinterns.com/data-science-analytics-task-3-2026/)
[![Internship: Future Interns](https://img.shields.io/badge/Organization-Future%20Interns-orange.svg)](https://futureinterns.com/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

---

## 📌 Executive Overview
Understanding lead progression across the customer acquisition lifecycle is fundamental to scaling growth efficiently. In this commercial marketing analytics project, a multi-channel campaign dataset of **12,500 inbound prospects** was analyzed to audit stage conversion drop-offs, quantify acquisition costs (CAC), model return on marketing spend (ROAS), isolate sales pipeline bottlenecks, and deliver an actionable Conversion Rate Optimization (CRO) roadmap.

---

## 📊 Core Performance Metrics (Executive Scorecard)

| Key Metric | Audited Figure | Business Diagnostic |
| :--- | :--- | :--- |
| **Total Inbound Visitors** | **12,500 Prospects** | Audited top-of-funnel traffic |
| **Leads Captured (Form Submissions)**| **4,724 Leads** | 37.79% Inbound Capture Rate |
| **Marketing Qualified Leads (MQL)** | **2,794 MQLs** | 59.14% Quality Qualification Rate |
| **Sales Qualified Leads (SQL)** | **1,434 SQLs** | 51.32% SDR Acceptance Rate |
| **Opportunities / Demos** | **855 Opportunities** | 59.62% Discovery-to-Demo Conversion |
| **Closed-Won Customer Deals** | **347 Accounts** | 40.58% Closing Rate |
| **Overall Visitor-to-Customer Rate** | **2.78%** | Exceeded 2.50% industry standard |
| **Total Marketing Ad Spend** | **\$488,772.36** | Controlled cross-channel budget |
| **Attributed Pipeline Revenue Won** | **\$1,545,787.17** | **3.16x Blended ROAS** |
| **Customer Acquisition Cost (CAC)** | **\$1,408.57 / won deal** | Under \$1,600.00 ceiling target |
| **Cost per Captured Lead (CPL)** | **\$103.47 / lead** | Healthy acquisition unit economics |

---

## 🔍 Key Findings & Analytical Highlights

1. **Stage-by-Stage Attrition Points:**
   - **The Visitor Bounce Gap:** 62.21% of inbound visitors exit without submitting an inquiry, representing the greatest raw volume leakage in the commercial funnel.
   - **The Deal Closing Gap:** 59.42% of qualified sales opportunities fail to close into won contracts, primarily due to budget constraints and competitor displacement.

2. **Channel Efficiency Divergence (ROAS & CAC):**
   - **Referral & Partner Channels:** Deliver the highest conversion efficiency (**5.20%**) with an outstanding **6.83x ROAS** and low CAC (\$673.08).
   - **Organic Search (SEO):** Outstanding organic efficiency generating \$365.4k in closed revenue at a **27.07x return on investment**.
   - **Paid Social (Meta/LinkedIn):** Severe performance drag, absorbing \$158k with only a **1.24x ROAS** and an inflated **\$3,440.70 CAC**.

3. **Device Disparities:**
   - Desktop visitors convert at **3.82%**, compared to only **1.64% on Mobile devices**, pinpointing critical UX and form length friction on handheld devices.

---

## 📁 Repository Structure

```text
FUTURE_DS_03/
├── dashboards/
│   ├── interactive_dashboard.html          # Executive web dashboard with interactive Chart.js
│   ├── marketing_funnel_workbook.xlsx      # Multi-tab styled Excel financial & conversion model
│   └── funnel_metrics.json                 # Aggregated funnel & CRO metrics payload
├── data/
│   ├── raw_marketing_funnel_data.csv       # Raw multi-touch marketing log (12,500 leads)
│   └── cleaned_marketing_funnel_data.csv   # Cleaned, categorized & attributed dataset
├── notebooks/
│   └── marketing_funnel_analysis.ipynb     # Exploratory data analysis & statistical modeling
├── reports/
│   ├── marketing_funnel_analysis_report.md # Comprehensive C-level growth analytics report
│   └── figures/
│       ├── 01_overall_funnel_stage_conversion.png
│       ├── 02_channel_conversion_comparison.png
│       ├── 03_roas_and_cac_by_channel.png
│       ├── 04_monthly_funnel_velocity_trend.png
│       ├── 05_deal_loss_reasons_breakdown.png
│       └── 06_device_conversion_performance.png
├── src/
│   ├── data_preprocessing.py               # Ingestion, validation & attribution pipeline
│   ├── funnel_analytics.py                 # Funnel progression & ROAS/CAC engine
│   ├── generate_visualizations.py          # Publication-ready visualizations
│   └── build_excel_dashboard.py            # Openpyxl multi-tab workbook builder
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation & execution guide
```

---

## 🚀 Setup & Reproduction Guide

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/<your-username>/FUTURE_DS_03.git
cd FUTURE_DS_03
pip install -r requirements.txt
```

### 2. Run Data Cleaning & Analytics Pipeline
```bash
python src/data_preprocessing.py
python src/funnel_analytics.py
python src/generate_visualizations.py
python src/build_excel_dashboard.py
```

### 3. View the Interactive Dashboard
Open `dashboards/interactive_dashboard.html` in any web browser to view interactive conversion funnel charts, channel ROAS comparisons, and conversion playbooks.

---

## 🎯 4-Pillar CRO Growth Recommendations
1. **Reallocate Paid Marketing Budget:** Shift \$50,000 from low-return Paid Social campaigns into high-converting Partner Referral co-marketing and Search SEO.
2. **Streamline Mobile Inbound Funnel:** Reduce mobile inquiry forms from 7 fields to 3 fields with instant social sign-in to address the 1.64% mobile conversion bottleneck.
3. **Speed-to-Lead Response SLA:** Implement automated SDR routing within 5 minutes of form completion to capture decaying prospect interest.
4. **Phased Pricing Options:** Mitigate late-stage opportunity losses by introducing entry-level starter packages.

---
**Future Interns Data Science & Analytics Internship (2026)**  
Official Submission for Task 3: Marketing Funnel & Conversion Performance Analysis
