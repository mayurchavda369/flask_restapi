from app import app


@app.route("/product")
def pro():
    return "hello its product"