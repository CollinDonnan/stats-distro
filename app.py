from flask import Flask, render_template, request, redirect
from ThereomGrimiore.discreate_distros import bernoulli_distro
from flask import jsonify
import ThereomGrimiore.discreate_distros.integer_distrobution as integer_distrobution
#from ThereomGrimiore.discreate_distros.binomial_distro import BinomialDistro

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/<distro>/<float:n>', methods=['GET', 'POST'])
def stats(distro, n):
    if distro == "bernoulli":
        dist = bernoulli_distro.bernoulli_distribution(n)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    elif distro == "integer":
        dist = integer_distrobution.integer_distribution(n)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "cdf": dist.cdf()})
    return 

if __name__ == "__main__":
    app.run(debug=True)