# EcoWatt ⚡

## AI-Powered Home Energy Advisor

EcoWatt is an intelligent energy management platform designed to help households analyze electricity consumption, reduce energy wastage, and encourage the adoption of renewable energy sources. The project supports **United Nations Sustainable Development Goal 7 (Affordable and Clean Energy)** by promoting energy efficiency and sustainable energy practices.

---

## SDG Alignment

### United Nations Sustainable Development Goal 7

**Affordable and Clean Energy**

EcoWatt helps users:

* Understand household electricity consumption.
* Identify high energy-consuming appliances.
* Reduce electricity bills through personalized recommendations.
* Estimate carbon footprint.
* Evaluate the feasibility of adopting rooftop solar energy.

---

## Problem Statement

Many households are unaware of how much electricity individual appliances consume, resulting in:

* High electricity bills
* Energy wastage
* Increased carbon emissions
* Low adoption of renewable energy solutions

There is a need for an intelligent system that can provide insights into energy consumption patterns and suggest practical ways to improve energy efficiency.

---

## Solution

EcoWatt provides a user-friendly dashboard where users can enter appliance usage details and receive:

* Monthly energy consumption estimates
* Electricity bill estimation
* Appliance-wise energy breakdown
* Carbon footprint analysis
* AI-generated energy-saving recommendations
* Solar panel recommendations with savings analysis

---

## Features

### ⚡ Energy Analysis

* Monthly electricity consumption calculation
* Estimated electricity bill
* Dynamic energy efficiency score

### 📊 Energy Breakdown

* Appliance-wise energy consumption analysis
* Interactive donut chart visualization
* Detailed consumption table

### 🤖 AI Energy Advisor

* Gemini-powered energy analysis
* Personalized recommendations
* Energy-saving suggestions
* Solar adoption recommendations

### 🌍 Carbon Footprint Calculator

* Monthly carbon emissions estimation
* Annual carbon emissions estimation

### ☀️ Solar Advisor

* Recommended solar capacity
* Installation cost estimation
* Annual savings prediction
* CO₂ reduction estimation
* Solar feasibility assessment
* Payback period calculation

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas

### Visualization

* Plotly

### Artificial Intelligence

* Google Gemini API

### Environment Management

* Python Dotenv

---

## Project Structure

```text
EcoWatt/
│
├── app.py
├── energy_calculator.py
├── ai_recommender.py
├── solar_advisor.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd EcoWatt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## How It Works

1. User enters appliance details and daily usage.
2. EcoWatt calculates monthly energy consumption.
3. Electricity bill and energy score are generated.
4. Carbon footprint is estimated.
5. Gemini AI analyzes usage patterns.
6. Personalized recommendations are provided.
7. Solar suitability and savings are calculated.

---

## Future Scope

* User authentication
* MongoDB integration
* Historical energy tracking
* PDF report generation
* Smart meter integration
* IoT-based real-time monitoring
* Mobile application support

---

## Impact

EcoWatt encourages responsible energy consumption and promotes renewable energy adoption. By helping users understand their energy usage patterns, the platform contributes towards a more sustainable and energy-efficient future.

---

## Author

**Tejas Dhatrak**

Electronics and Telecommunication Engineering (EXTC)

Veermata Jijabai Technological Institute (VJTI)
