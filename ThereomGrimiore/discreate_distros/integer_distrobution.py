class integer_distribution:
    def __init__(self, k):
        self.k = k  # number of equally likely outcomes

    def pmf(self):
        return {i: 1 / self.k for i in range(self.k)}

    def cdf(self):
        cdf = {}
        cumulative = 0
        for i in range(self.k):
            cumulative += 1 / self.k
            cdf[i] = cumulative
        return cdf

    def mgf(self):
        return f"(1/{self.k}) * ((1 - e^({self.k}*t)) / (1 - e^t))"

    def mean(self):
        return (self.k - 1) / 2

    def variance(self):
        return (self.k**2 - 1) / 12

    def stddev(self):
        return self.variance() ** 0.5
