def analyze_heart_rate(data):
    average = sum(data) / len(data)
    print(f"Average BPM: {average:.1f}")
    if average < 60:
        print("Status: Low - Possible Bradycardia")
    elif 60 <= average <= 100:
        print("Status: Normal")
    elif 100 < average <= 120:
        print("Status: Caution - Slightly Elevated")
    else:
        print("Status: High Risk - Consult a doctor immediately")

if __name__ == "__main__":
    heart_rates = [98, 102, 105, 110, 108]
    analyze_heart_rate(heart_rates)