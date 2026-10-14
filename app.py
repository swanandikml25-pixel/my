
from flask import Flask, request, render_template

app = Flask(__name__)

# Check balanced parentheses
def is_balanced(expression):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


# Connect Python with HTML
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")

        if is_balanced(expression):
            result = "Balanced Parentheses"
        else:
            result = "Not Balanced Parentheses"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)