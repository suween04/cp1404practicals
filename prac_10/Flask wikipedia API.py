from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        try:
            page = wikipedia.page(query, autosuggest=True)
            return render_template(
                "result.html", title=page.title, summary=page.summary, url=page.url
            )
        except wikipedia.DisambiguationError as e:
            return render_template("error.html", message="Disambiguation required.", options=e.options)
        except wikipedia.PageError:
            return render_template("error.html", message="Page not found.")
        except Exception as e:
            return render_template("error.html", message=f"An unexpected error occurred: {e}")
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
