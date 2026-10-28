
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bracket Checker</title>

    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="min-h-screen flex items-center justify-center
bg-gradient-to-br from-slate-950 via-purple-950 to-indigo-900 p-5">

    <div class="w-full max-w-2xl bg-white/10 backdrop-blur-xl
    border border-white/20 rounded-3xl p-8 shadow-2xl
    transition duration-300 hover:shadow-purple-500/20">

        <!-- Heading -->
        <div class="text-center mb-8">
            <div class="text-5xl mb-4">🧩</div>

            <h1 class="text-3xl md:text-4xl font-bold text-white">
                Bracket Checker
            </h1>

            <p class="text-purple-200 mt-3">
                Check your parentheses with one click
            </p>
        </div>

        <!-- Text area -->
        <label class="block text-white font-semibold mb-3">
            Enter your expression
        </label>

        <textarea id="expression" rows="5"
        placeholder="Example: { [ ( ) ] }"
        class="w-full p-5 rounded-2xl bg-slate-900/70
        border border-purple-400/40 text-white text-lg
        placeholder-gray-400 outline-none resize-y
        focus:border-purple-400 focus:ring-2
        focus:ring-purple-500/30 transition"></textarea>

        <!-- Buttons -->
        <div class="flex flex-wrap gap-4 mt-5">

            <button type="button" onclick="checkBrackets()"
            class="flex-1 min-w-36 bg-purple-600 hover:bg-purple-500
            text-white font-bold py-3 rounded-xl
            transition duration-300 hover:-translate-y-1">
                Check Brackets
            </button>

            <button type="button" onclick="clearAll()"
            class="flex-1 min-w-36 bg-slate-700 hover:bg-slate-600
            text-white font-bold py-3 rounded-xl transition">
                Clear
            </button>

        </div>

        <!-- Result -->
        <div id="result"
        class="mt-6 p-5 rounded-2xl bg-slate-900/60
        border border-white/10 text-center text-purple-200
        font-semibold transition duration-300">
            Your result will appear here
        </div>

        <p class="text-center text-gray-400 text-sm mt-7">
            Python • Stack Algorithm
        </p>

    </div>

    <script>
        // Check balanced parentheses
        function checkBrackets() {
            let expression = document.getElementById("expression").value;
            let stack = [];
            let pairs = { ')': '(', ']': '[', '}': '{' };
            let balanced = true;

            for (let char of expression) {
                if ("([{".includes(char)) {
                    stack.push(char);
                }
                else if (")]}".includes(char)) {
                    if (stack.length === 0 ||
                        stack[stack.length - 1] !== pairs[char]) {
                        balanced = false;
                        break;
                    }
                    stack.pop();
                }
            }

            if (stack.length !== 0) {
                balanced = false;
            }

            let result = document.getElementById("result");

            if (balanced) {
                result.innerText = "✓ Balanced Parentheses";
                result.className =
                    "mt-6 p-5 rounded-2xl bg-green-500/15 border " +
                    "border-green-400/40 text-center text-green-300 " +
                    "font-bold transition duration-300";
            } else {
                result.innerText = "✗ Not Balanced Parentheses";
                result.className =
                    "mt-6 p-5 rounded-2xl bg-red-500/15 border " +
                    "border-red-400/40 text-center text-red-300 " +
                    "font-bold transition duration-300";
            }
        }

        // Clear input and result
        function clearAll() {
            document.getElementById("expression").value = "";

            let result = document.getElementById("result");
            result.innerText = "Your result will appear here";
            result.className =
                "mt-6 p-5 rounded-2xl bg-slate-900/60 border " +
                "border-white/10 text-center text-purple-200 " +
                "font-semibold transition duration-300";
        }
    </script>

</body>
</html>