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


def main() -> None:
    out_dir = ensure_dir(project_root() / "figures" / "generated")
    build_normal_density(out_dir)
    build_poisson_pmf(out_dir)


if __name__ == "__main__":
    main()
