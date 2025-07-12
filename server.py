from flask import Flask, request, jsonify
from handler.chatgpt_selenium_automation import ChatGPTAutomation

app = Flask(__name__)

chrome_path = "/usr/bin/google-chrome"           # Adjust if on Windows or Mac
chromedriver_path = "/usr/local/bin/chromedriver"

chat = ChatGPTAutomation(chrome_path, chromedriver_path)
input("🔓 Log in via the Chrome window and press Enter here...")

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("text", "")
    chat.send_prompt_to_chatgpt(prompt)
    response = chat.return_last_response()
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
