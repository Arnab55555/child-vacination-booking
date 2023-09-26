document.addEventListener("DOMContentLoaded", function () {
    // BMI Calculator
    const heightInput = document.getElementById("height");
    const weightInput = document.getElementById("weight");
    const calculateBMIBtn = document.getElementById("calculate-bmi-btn");
    const bmiValue = document.getElementById("bmi-value");
    const bmiCategory = document.getElementById("bmi-category");

    calculateBMIBtn.addEventListener("click", calculateBMI);

    function calculateBMI() {
        const height = parseFloat(heightInput.value);
        const weight = parseFloat(weightInput.value);

        if (!isNaN(height) && !isNaN(weight) && height > 0 && weight > 0) {
            const bmi = weight / ((height / 100) * (height / 100));
            bmiValue.textContent = bmi.toFixed(2);

            if (bmi < 18.5) {
                bmiCategory.textContent = "Underweight";
                bmiCategory.style.color = "#FF9800";
            } else if (bmi < 24.9) {
                bmiCategory.textContent = "Normal weight";
                bmiCategory.style.color = "#4CAF50";
            } else if (bmi < 29.9) {
                bmiCategory.textContent = "Overweight";
                bmiCategory.style.color = "#FFC107";
            } else {
                bmiCategory.textContent = "Obese";
                bmiCategory.style.color = "#F44336";
            }
        } else {
            alert("Please enter valid height and weight.");
        }
    }

    // Additional JavaScript for other features can be added here
});
