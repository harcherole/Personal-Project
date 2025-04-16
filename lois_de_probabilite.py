import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from PIL import Image
import io

# Dictionnaire des lois avec générateurs de données
distributions = {
    "Bernoulli": lambda: np.random.binomial(1, 0.3, 1000),
    "Binomiale B(n, p)": lambda: np.random.binomial(n=10, p=0.5, size=1000),
    "Poisson P(λ)": lambda: np.random.poisson(lam=3, size=1000),
    "Géométrique G(p)": lambda: np.random.geometric(p=0.3, size=1000),
    "Hypergéométrique H(N, n, p)": lambda: np.random.hypergeometric(ngood=30, nbad=70, nsample=20, size=1000),
    "Binomiale négative": lambda: np.random.negative_binomial(n=5, p=0.4, size=1000),
    "Pascal": lambda: np.random.negative_binomial(n=10, p=0.4, size=1000),
    "Uniforme U(a, b)": lambda: np.random.uniform(low=0, high=1, size=1000),
    "Exponentielle E(λ)": lambda: np.random.exponential(scale=1.0, size=1000),
    "Normale N(m, σ²)": lambda: np.random.normal(loc=0, scale=1, size=1000),
    "Weibull W(λ, a)": lambda: np.random.weibull(a=1.5, size=1000),
    "Cauchy C(a, b)": lambda: stats.cauchy(loc=0, scale=1).rvs(1000),
    "Gamma Γ(a, λ)": lambda: np.random.gamma(shape=2.0, scale=1.0, size=1000),
    "Bêta B(a, b)": lambda: np.random.beta(a=2.0, b=5.0, size=1000),
    "Khi-Deux χ²(n)": lambda: np.random.chisquare(df=3, size=1000),
    "Student T(n)": lambda: np.random.standard_t(df=10, size=1000),
    "Fisher F(m, n)": lambda: np.random.f(dfnum=5, dfden=10, size=1000)
}

# Créer les images matplotlib pour chaque loi
frames = []

for name, generator in distributions.items():
    data = generator()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(data, bins=30, density=True, color='skyblue', edgecolor='black')
    ax.set_title(name)
    ax.set_ylabel("Densité")
    ax.set_xlabel("Valeurs")
    fig.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf)
    frames.append(img)

# Créer le GIF
gif_path = "animations_lois.gif"
frames[0].save(
    gif_path,
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=1000,
    loop=0
)

print(f"GIF créé avec succès : {gif_path}")
