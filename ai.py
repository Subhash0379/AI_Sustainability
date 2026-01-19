# AI-Based Air Quality Monitoring & Health Awareness Assistant
# Student Name : Gurrampati Subhash Reddy
# College Name : Alliance University
# Internship   : 1M1B – IBM SkillsBuild AI for Sustainability
# SDG          : SDG 11, SDG 3

# List to store AQI history
aqi_history = []

# Function: Classify Air Quality
def classify_air_quality(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Function: Health Advisory Based on AQI
def get_health_advice(aqi):
    if aqi <= 50:
        return (
            "Air quality is good.\n"
            "• Safe for outdoor activities\n"
            "• Ideal conditions for exercise"
        )
    elif aqi <= 100:
        return (
            "Air quality is moderate.\n"
            "• Sensitive individuals should limit prolonged outdoor activities"
        )
    elif aqi <= 150:
        return (
            "Unhealthy for sensitive groups.\n"
            "• Children and elderly should stay indoors\n"
            "• Avoid heavy outdoor exercise"
        )
    elif aqi <= 200:
        return (
            "Air quality is unhealthy.\n"
            "• Avoid outdoor activities\n"
            "• Wear mask if going outside"
        )
    elif aqi <= 300:
        return (
            "Air quality is very unhealthy.\n"
            "• Stay indoors\n"
            "• Use air purifiers if available"
        )
    else:
        return (
            "Hazardous air quality!\n"
            "• Health emergency conditions\n"
            "• Avoid all outdoor exposure"
        )

# Function: Pollution Risk Explanation
def explain_risk(category):
    risks = {
        "Good": "Minimal health risk.",
        "Moderate": "Minor breathing discomfort for sensitive people.",
        "Unhealthy for Sensitive Groups": "May cause respiratory issues.",
        "Unhealthy": "Increased risk of heart and lung diseases.",
        "Very Unhealthy": "Serious health effects for everyone.",
        "Hazardous": "Emergency condition affecting entire population."
    }
    return risks.get(category, "No data available.")

# Function: Generate Daily AQI Report
def generate_report(aqi):
    category = classify_air_quality(aqi)
    advice = get_health_advice(aqi)
    risk = explain_risk(category)

    report = f"""
---------------- AIR QUALITY REPORT ----------------
AQI Value           : {aqi}
Air Quality Level   : {category}
Health Risk         : {risk}

Health Advisory:
{advice}

Sustainability Tip:
• Use public transport
• Reduce vehicle usage
• Plant more trees
"""
    return report

# Function: Save AQI History
def save_history(aqi):
    aqi_history.append(aqi)

# Function: Display AQI History
def show_history():
    if not aqi_history:
        print("No AQI data recorded yet.")
    else:
        print("\nAQI History:")
        for i, value in enumerate(aqi_history, start=1):
            print(f"Day {i}: AQI = {value}")

# Main Menu-Driven Program
def air_quality_system():
    while True:
        print("\n====================================")
        print(" AI-Based Air Quality Monitoring System ")
        print("====================================")
        print("1. Enter AQI Value")
        print("2. View AQI History")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                aqi = int(input("Enter AQI value: "))
                save_history(aqi)
                report = generate_report(aqi)
                print(report)

            except ValueError:
                print("Invalid input! Please enter a numeric AQI value.")

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Thank you for using the Air Quality Assistant.")
            print("Stay safe and support a sustainable environment 🌱")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the Program
air_quality_system()
