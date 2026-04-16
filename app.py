from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Azure Web Hosting</h1>
    <p>This website is hosted on Microsoft Azure App Service.</p>
    """

@app.route("/about")
def about():
    return "<h2>This is About Page hosted on Azure</h2>"

if __name__ == "__main__":
    app.run()
