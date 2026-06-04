from dotenv import load_dotenv
import google.generativeai as genai
import os
# Load environment variables
load_dotenv()
# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
# Load Gemini model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
def generate_recommendations(result):
    prompt = f"""
    You are an expert Home Energy Consultant.
    Analyze the following household energy data:
    Monthly Consumption:
    {result['Total']} kWh
    Estimated Monthly Bill:
    ₹{result['Bill']}
    Appliance Breakdown:
    AC:
    {result['AC']} kWh
    Fans:
    {result['Fans']} kWh
    Refrigerator:
    {result['Fridge']} kWh
    TV:
    {result['TV']} kWh
    LEDs:
    {result['LEDs']} kWh
    Provide:
    1. A short analysis of the household's energy usage.
    2. The top energy-consuming appliances.
    3. 5 personalized energy-saving recommendations.
    4. Estimated monthly savings.
    5. Whether solar panels are recommended
    Keep the response concise and user-friendly.
    """
    try:
        response = model.generate_content(
            prompt
        )
        return response.text
    except Exception as e:
        return f"""
        Unable to generate recommendations.
        Error:
        {str(e)}
        """