from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from helpers import ensure_dir, project_root


def build_normal_density(out_dir: Path) -> None:
    x = np.linspace(-4.0, 4.0, 400)
    y = np.exp(-0.5 * x**2) / math.sqrt(2.0 * math.pi)

    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.plot(x, y, color="#1f5f8b", linewidth=2.2)
    ax.set_xlabel("x")
    ax.set_ylabel("density")
    ax.set_title("Standard normal density")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_dir / "normal_density.png", dpi=160)
    plt.close(fig)


def build_poisson_pmf(out_dir: Path, lam: float = 4.0) -> None:
    k = np.arange(0, 15)
    pmf = np.exp(-lam) * lam**k / np.array([math.factorial(int(v)) for v in k])

    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.vlines(k, 0.0, pmf, color="#c44536", linewidth=2.0)
    ax.scatter(k, pmf, color="#c44536", s=28)
    ax.set_xlabel("k")
    ax.set_ylabel("P(X = k)")
    ax.set_title(f"Poisson PMF, lambda = {lam:g}")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_dir / "poisson_pmf.png", dpi=160)
    plt.close(fig)


def build_poisson_pmf_profiles(out_dir: Path) -> None:
    configs = [(1, "#1f3db8"), (4, "#2e8b57"), (10, "#d62728")]

    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    k = np.arange(0, 26)
    factorials = np.array([math.factorial(int(i)) for i in k], dtype=float)
    for lam, color in configs:
        pmf = np.exp(-lam) * lam**k / factorials
        ax.plot(
            k,
            pmf,
            marker="o",
            markersize=5.2,
            linewidth=1.3,
            color=color,
            markeredgecolor="black",
            markeredgewidth=0.4,
            label=rf"$\lambda$={lam}",
        )

    ax.set_xlim(0, 25)
    ax.set_ylim(0, 0.40)
    ax.set_xlabel("k")
    ax.set_ylabel("P(k)")
    ax.set_title("Распределение Пуассона")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper right", framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "poisson_pmf_profiles.png", dpi=180)
    plt.close(fig)


def build_binomial_pmf_profiles(out_dir: Path, p: float = 0.3) -> None:
    configs = [(5, "#1f3db8"), (20, "#2e8b57"), (100, "#d62728")]

    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    for n, color in configs:
        k = np.arange(0, n + 1)
        pmf = np.array(
            [math.comb(n, int(i)) * p**i * (1.0 - p) ** (n - i) for i in k],
            dtype=float,
        )
        ax.plot(
            k,
            pmf,
            marker="o",
            markersize=5.2,
            linewidth=1.3,
            color=color,
            markeredgecolor="black",
            markeredgewidth=0.4,
            label=f"n={n}\np={p:g}",
        )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 0.40)
    ax.set_xlabel("k")
    ax.set_ylabel("P(k)")
    ax.set_title("Биномиальное распределение")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper right", framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "binomial_pmf_profiles.png", dpi=180)
    plt.close(fig)


def build_normal_density_profiles(out_dir: Path) -> None:
    configs = [
        (0, 1, "#1f3db8"),
        (0, 2, "#2e8b57"),
        (2, 1, "#d62728"),
    ]
    x = np.linspace(-6.0, 6.0, 500)

    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    for mu, sigma, color in configs:
        density = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (
            sigma * math.sqrt(2.0 * math.pi)
        )
        ax.plot(
            x,
            density,
            linewidth=1.8,
            color=color,
            label=rf"$\mu$={mu}, $\sigma$={sigma}",
        )

    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 0.45)
    ax.set_xlabel("x")
    ax.set_ylabel("density")
    ax.set_title("Нормальное распределение")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper right", framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "normal_density_profiles.png", dpi=180)
    plt.close(fig)


def normal_pdf(x: np.ndarray, mu: float = 0.0, sigma: float = 1.0) -> np.ndarray:
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (
        sigma * math.sqrt(2.0 * math.pi)
    )


def build_numpy_sampling_demos(out_dir: Path) -> None:
    rng = np.random.default_rng(20260423)
    sample_size = 20_000

    x = rng.uniform(-1.0, 1.0, sample_size)
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.hist(x, bins=50, density=True, color="#4ea1ff", alpha=0.72, edgecolor="white")
    ax.hlines(0.5, -1, 1, color="#ffb347", linewidth=2.4, label="плотность")
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(0, 0.7)
    ax.set_xlabel("x")
    ax.set_ylabel("density")
    ax.set_title("Равномерное распределение из выборки")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "numpy_uniform_sample.png", dpi=180)
    plt.close(fig)

    n, p = 20, 0.3
    k_sample = rng.binomial(n=n, p=p, size=sample_size)
    k = np.arange(0, n + 1)
    freq = np.bincount(k_sample, minlength=n + 1) / sample_size
    pmf = np.array(
        [math.comb(n, int(i)) * p**i * (1.0 - p) ** (n - i) for i in k],
        dtype=float,
    )
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.bar(k, freq, color="#4ea1ff", alpha=0.72, edgecolor="white", label="частоты")
    ax.plot(k, pmf, color="#ffb347", marker="o", linewidth=2.0, label="PMF")
    ax.set_xlim(-0.8, 20.8)
    ax.set_ylim(0, 0.22)
    ax.set_xlabel("k")
    ax.set_ylabel("P(k)")
    ax.set_title("Биномиальное распределение из выборки")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "numpy_binomial_sample.png", dpi=180)
    plt.close(fig)

    lam = 4.0
    k_sample = rng.poisson(lam=lam, size=sample_size)
    k = np.arange(0, 16)
    freq = np.bincount(k_sample, minlength=len(k))[: len(k)] / sample_size
    pmf = np.exp(-lam) * lam**k / np.array([math.factorial(int(i)) for i in k])
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.bar(k, freq, color="#4ea1ff", alpha=0.72, edgecolor="white", label="частоты")
    ax.plot(k, pmf, color="#ffb347", marker="o", linewidth=2.0, label="PMF")
    ax.set_xlim(-0.8, 15.8)
    ax.set_ylim(0, 0.23)
    ax.set_xlabel("k")
    ax.set_ylabel("P(k)")
    ax.set_title("Распределение Пуассона из выборки")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "numpy_poisson_sample.png", dpi=180)
    plt.close(fig)

    mu, sigma = 0.0, 1.0
    x = rng.normal(loc=mu, scale=sigma, size=sample_size)
    grid = np.linspace(-4.0, 4.0, 500)
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.hist(x, bins=70, density=True, color="#4ea1ff", alpha=0.72, edgecolor="white")
    ax.plot(grid, normal_pdf(grid, mu, sigma), color="#ffb347", linewidth=2.4, label="PDF")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.46)
    ax.set_xlabel("x")
    ax.set_ylabel("density")
    ax.set_title("Нормальное распределение из выборки")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(framealpha=1.0, edgecolor="black")
    fig.tight_layout()
    fig.savefig(out_dir / "numpy_normal_sample.png", dpi=180)
    plt.close(fig)


def build_clt_uniform_sums(out_dir: Path) -> None:
    rng = np.random.default_rng(20260424)
    sample_size = 80_000
    grid = np.linspace(-4.2, 4.2, 500)

    for m in [1, 2, 5, 10]:
        x = rng.uniform(-1.0, 1.0, size=(sample_size, m))
        z = x.sum(axis=1) / math.sqrt(m / 3.0)

        fig, ax = plt.subplots(figsize=(9.2, 5.2))
        ax.hist(
            z,
            bins=80,
            range=(-4.2, 4.2),
            density=True,
            color="#4ea1ff",
            alpha=0.72,
            edgecolor="white",
        )
        ax.plot(
            grid,
            normal_pdf(grid),
            color="#ffb347",
            linewidth=2.6,
            label=r"$\mathrm{N}(0,1)$",
        )
        ax.set_xlim(-4.2, 4.2)
        ax.set_ylim(0, 0.55)
        ax.set_xlabel(r"$z$")
        ax.set_ylabel("density")
        ax.set_title(rf"ЦПТ: сумма {m} равномерных случайных величин")
        ax.text(
            0.03,
            0.92,
            rf"$z=(X_1+\cdots+X_m)/\sqrt{{m/3}},\quad m={m}$",
            transform=ax.transAxes,
            fontsize=12,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.9},
        )
        ax.grid(axis="y", alpha=0.25)
        ax.legend(loc="upper right", framealpha=1.0, edgecolor="black")
        fig.tight_layout()
        fig.savefig(out_dir / f"clt_uniform_sum_m{m}.png", dpi=180)
        plt.close(fig)


def main() -> None:
    out_dir = ensure_dir(project_root() / "shared" / "figures" / "generated")
    build_normal_density(out_dir)
    build_poisson_pmf(out_dir)
    build_poisson_pmf_profiles(out_dir)
    build_binomial_pmf_profiles(out_dir)
    build_normal_density_profiles(out_dir)
    build_numpy_sampling_demos(out_dir)
    build_clt_uniform_sums(out_dir)


if __name__ == "__main__":
    main()
