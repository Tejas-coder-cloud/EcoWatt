# ai_recommender.py

from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

# Configure Gemini
genai.configure(
    api_key=api_key
)

# Create model
model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_recommendations(result):

    prompt = f"""
You are an expert Home Energy Consultant.

Analyze the following household energy usage data and provide concise recommendations.

Monthly Consumption:
{result['Total']} kWh

Estimated Monthly Bill:
₹{result['Bill']}

Appliance Breakdown:

AC:
{result['AC']} kWh

Fans:
{result['Fans']} kWh

Fridge:
{result['Fridge']} kWh

TV:
{result['TV']} kWh

LEDs:
{result['LEDs']} kWh

Provide your response in Markdown format using:

# Analysis

# Top Energy Consumers

# Recommendations

# Estimated Savings

# Solar Advice

Keep the response concise and practical.
"""

    try:

        print("Sending request to Gemini...")

        response = model.generate_content(
            prompt
        )

        print("Response received!")

        return response.text

    except Exception as e:

        print("ERROR:", e)

        return f"""
# Error

Unable to generate recommendations.

Details:

{str(e)}
"""