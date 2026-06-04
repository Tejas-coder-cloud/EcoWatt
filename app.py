import streamlit as st
import pandas as pd
import plotly.express as px
from energy_calculator import calculate_energy
from ai_recommender import generate_recommendations
from solar_advisor import recommend_solar
# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="EcoWatt AI",
    page_icon="⚡",
    layout="wide"
)
# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>
.main {
    background-color: #0A0F1F;
}
.metric-card {
    background: linear-gradient(
        135deg,
        #00F5FF,
        #0088FF
    );
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    transition: 0.3s;
    box-shadow:
    0px 0px 15px rgba(
        0,245,255,0.4
    );
}
.metric-card:hover {
    transform: scale(1.05);
}
.big-number {
    font-size: 36px;
    font-weight: bold;
}
.small-text {
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)
# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("⚡ EcoWatt AI")
menu = st.sidebar.radio(
    "Navigation",
    [
        "Energy Analysis",
        "Energy Breakdown",
        "Solar Advisor",
        "AI Advisor"
    ]
)
st.sidebar.markdown("---")
st.sidebar.subheader("Household Inputs")
fans = st.sidebar.number_input(
    "Fans",
    min_value=0,
    value=4
)
fan_hours = st.sidebar.slider(
    "Fan Usage (hrs/day)",
    0,
    24,
    10
)
leds = st.sidebar.number_input(
    "LED Bulbs",
    min_value=0,
    value=8
)
led_hours = st.sidebar.slider(
    "LED Usage (hrs/day)",
    0,
    24,
    6
)
acs = st.sidebar.number_input(
    "ACs",
    min_value=0,
    value=1
)
ac_hours = st.sidebar.slider(
    "AC Usage (hrs/day)",
    0,
    24,
    8
)
tvs = st.sidebar.number_input(
    "TVs",
    min_value=0,
    value=1
)
tv_hours = st.sidebar.slider(
    "TV Usage (hrs/day)",
    0,
    24,
    4
)
fridges = st.sidebar.number_input(
    "Refrigerators",
    min_value=0,
    value=1
)
# -----------------------------------
# CALCULATIONS
# -----------------------------------
result = calculate_energy(
    fans,
    fan_hours,
    leds,
    led_hours,
    acs,
    ac_hours,
    tvs,
    tv_hours,
    fridges
)
total = result["Total"]
bill = result["Bill"]
# -----------------------------------
# SCORE
# -----------------------------------
score=max(0,round(100-(total/10)))
# -----------------------------------
# ENERGY ANALYSIS PAGE
# -----------------------------------
if menu == "Energy Analysis":
    st.title("⚡ EcoWatt ")
    st.markdown(
        "### Smart Home Energy Advisor"
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="small-text">
            Monthly Consumption
            </div>
            <div class="big-number">
            {total}
            </div>
            <div class="small-text">
            kWh
            </div>
        </div>
        """,
        unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="small-text">
            Estimated Bill
            </div>
            <div class="big-number">
            ₹{bill}
            </div>
        </div>
        """,
        unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="small-text">
            Energy Score
            </div>
            <div class="big-number">
            {score}/100
            </div>
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown("---")
    st.info(
        "Use the Energy Breakdown section to see which appliances consume the most electricity."
    )
# -----------------------------------
# ENERGY BREAKDOWN PAGE
# -----------------------------------
elif menu == "Energy Breakdown":
    st.title("📊 Energy Breakdown")
    chart_data = pd.DataFrame({
        "Appliance": [
            "Fans",
            "LEDs",
            "AC",
            "TV",
            "Fridge"
        ],
        "Units": [
            result["Fans"],
            result["LEDs"],
            result["AC"],
            result["TV"],
            result["Fridge"]
        ]
    })
    fig = px.pie(
        chart_data,
        values="Units",
        names="Appliance",
        hole=0.55,
        title="Monthly Energy Consumption"
    )
    fig.update_layout(
        paper_bgcolor="#0A0F1F",
        font_color="white"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.subheader("Detailed Consumption")
    st.dataframe(
        chart_data,
        use_container_width=True
    )
# -----------------------------------
# SOLAR ADVISOR PAGE
# -----------------------------------
elif menu == "Solar Advisor":
    st.title("☀️ Solar Advisor")
    solar = recommend_solar(total)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "☀️ Solar Capacity",
            f"{solar['solar_kw']} kW"
        )
        st.metric(
            "💰 Installation Cost",
            f"₹{solar['installation_cost']:,.0f}"
        )
        st.metric(
            "📉 Payback Period",
            f"{solar['payback_years']} Years"
        )
    with col2:
        st.metric(
            "💵 Annual Savings",
            f"₹{solar['annual_savings']:,.0f}"
        )
        st.metric(
            "🌍 CO₂ Reduction",
            f"{solar['carbon_reduction']} tonnes/year"
        )
    st.markdown("---")
    if total > 500:
        st.success(
            "Excellent candidate for rooftop solar installation."
        )
    elif total > 250:
        st.info(
            "Solar installation is recommended."
        )
    else:
        st.warning(
            "Solar installation may not provide maximum financial benefit yet."
        )
    st.info(f"""
    ☀ Recommended System: {solar['solar_kw']} kW

    💰 Installation Cost: ₹{solar['installation_cost']:,.0f}

    📉 Estimated Annual Savings: ₹{solar['annual_savings']:,.0f}

    🌍 Carbon Reduction: {solar['carbon_reduction']} tonnes/year

    ⏳ Payback Period: {solar['payback_years']} years
    """)
# -----------------------------------
# AI ADVISOR PAGE
# -----------------------------------
elif menu == "AI Advisor":
    st.title("🤖 AI Energy Advisor")
    col1,col2=st.columns(2)
    carbon=round(total*0.82,2)
    with col1:
        st.metric(" 🌍  Monthly carbon footprint",f"{carbon} kg CO₂")
    with col2:
        st.metric(" 🌍  Yearly carbon footprint",f"{round(carbon*12,2)} kg CO₂")
    with st.container():
        if st.button("⚡ Analyze My Home"):
            try:
                with st.spinner(
                "Analyzing your energy consumption..."
            ):
                    recommendations = generate_recommendations(
                    result
                )
                st.markdown("### 📋 AI Analysis")
                st.markdown(recommendations)
            except Exception as e:
                st.error(
                f"Error: {str(e)}"
            )



    