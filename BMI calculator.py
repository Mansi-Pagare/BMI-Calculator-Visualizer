import matplotlib.pyplot as plt

def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = weight / (height / 100) ** 2
    elif unit == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def plot_bmi_graph(bmi):
    categories = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
    values = [18.4, 22.0, 27.5, 35.0]  # Example BMI values for category edges

    plt.figure(figsize=(10, 5))
    plt.bar(categories, values, color=['blue', 'green', 'yellow', 'red'], alpha=0.6)
    plt.axhline(y=bmi, color='black', linestyle='--')
    plt.text(0.5, bmi + 0.5, f'Your BMI: {bmi:.2f}', color='black', fontsize=12, ha='center')
    plt.xlabel('BMI Categories')
    plt.ylabel('BMI Value')
    plt.title('BMI Categories and Your BMI')
    plt.ylim(0, 40)
    plt.show()

def main():
    unit = input("Choose unit system (metric/imperial): ").lower()
    if unit == 'metric':
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in cm: "))
    elif unit == 'imperial':
        weight = float(input("Enter weight in lb: "))
        height = float(input("Enter height in inches: "))
    else:
        print("Invalid unit system")
        return

    bmi = calculate_bmi(weight, height, unit)
    category = get_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

    # Provide health insights based on BMI category
    if category == "Underweight":
        print("You may need to gain weight. Consult with a healthcare provider for personalized advice.")
    elif category == "Normal weight":
        print("You are in a healthy weight range. Maintain a balanced diet and regular exercise.")
    elif category == "Overweight":
        print("Consider adopting a healthier lifestyle with a balanced diet and regular physical activity.")
    elif category == "Obesity":
        print("Seek guidance from a healthcare provider to develop a plan for weight management and overall health.")

    # Plot the BMI graph
    plot_bmi_graph(bmi)

if __name__ == "__main__":
    main()

