# stats-distro

A full stack flask web application that analyizes and visualizes probability distributions. Users can enter a success rate, number of trials and select a distribution. The app will calculate the mean, variance, standard deveation, and the moment generating function, and graph the probability mass function and the cumulative mass function.

# Tech Stack

Backend - Flask

Frontend - CSS, HTML, JavaScipt, Jinja, Chart.js

Build System - uv

CI - Github Actions, uv, ty, ruff

# Dependancies

- Python 3.12+
- Pip 25.2+

# Installation

1. git clone https://github.com/CollinDonnan/stats-distro.git

2. pip install uv

3. uv sync

4. cd stas-distro

5. python3 app.py


# Supports

Currently this app supports the Bernoulli and intetger distributions

# Features

- Computes mean, variance, standard deveation, and moment generating functions

- Plots pmfs and cdfs
