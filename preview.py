from flask import Flask, send_from_directory

# Serve /assets/* as static files
app = Flask(__name__, static_folder="assets", static_url_path="/assets")

# Serve the landing page
@app.get("/")
def home():
    return send_from_directory(".", "index.html")

# Optional: serve any other file in root (e.g., CNAME, robots.txt)
@app.get("/<path:path>")
def static_proxy(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
