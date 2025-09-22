from pyscript import display, document

def adding_numbers(e):
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)

    average = (num1 + num2) / 2

    result_div = document.getElementById("output1")
    result_div.innerHTML = f"<div>Average: {average:.2f}</div>"

    if average >= 75:
        result_div.innerHTML += "<div style='color: green;'>Passed✅</div>"
    else:
        result_div.innerHTML += "<div style='color: red;'>Failed❌</div>"