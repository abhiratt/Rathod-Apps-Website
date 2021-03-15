from flask import Flask, request, render_template
from urllib.parse import quote_plus

app = Flask(__name__)
app.jinja_env.filters['quote_plus'] = lambda u: quote_plus(u)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', title="Sorry :("), 404


@app.route('/<appName>/privacy-policy', methods=["GET"])
def privacyPolicy(appName):
    return render_template(
    'privacypolicy.html',
    title = "Privacy Policy",
    appName = appName), 200


@app.route('/<appName>/terms-and-conditions', methods=["GET"])
def termsAndConditions(appName):
    return render_template('terms.html', title="Terms and Conditions",appName = appName), 200


if __name__ == '__main__':
    app.run(debug=False)
