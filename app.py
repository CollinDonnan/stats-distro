from flask import Flask, render_template, jsonify
from ThereomGrimiore.discreate_distros import bernoulli_distro
import ThereomGrimiore.discreate_distros.integer_distrobution as integer_distrobution
from ThereomGrimiore.discreate_distros.binomial_distro import binomial_distribution
from ThereomGrimiore.discreate_distros.geometric_distro import geometric_distribution
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/integer/<int:trials>', methods=['GET', 'POST'])
def integer(trials):
    try: 
            idx = int(trials)
            dist = integer_distrobution.integer_distribution(idx)
            return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "cdf": dist.cdf(), "mgf": dist.mgf()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/geometric/<float:n>/<int:trials>', methods=['GET', 'POST'])
def geometric(n, trials):
    n = round(n,5)
    try:
            dist = geometric_distribution(trials, n)
            return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/binomial/<float:n>/<int:trials>', methods=['GET', 'POST'])
def binomial(n, trials):
    n = round(n,5)
    try:
            dist  = binomial_distribution(trials, n)
            return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/bernoulli/<float:n>', methods=['GET', 'POST'])
def bernoulli(n):
    n = round(n,5)
    try:
            dist = bernoulli_distro.bernoulli_distribution(n)
            return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cmf": dist.cdf()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    


if __name__ == "__main__":
    app.run(debug=True)