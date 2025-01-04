from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    target_redirect = os.getenv("TARGET_REDIRECT", "https://example.com")
    return redirect(target_redirect, code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
