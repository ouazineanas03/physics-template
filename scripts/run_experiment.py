"""Regenerate every figure of the project.

Replace the body of main() with your own experiment. The pattern to keep:
one script, no manual steps, figures written to figures/.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from physproj import exact_solution  # noqa: E402

FIGURES = Path(__file__).resolve().parent.parent / "figures"


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    t = np.linspace(0.0, 10.0, 500)
    x = exact_solution(t, x0=1.0, v0=0.0, omega=2.0)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(t, x)
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")
    ax.set_title("Placeholder: exact harmonic oscillator")
    fig.tight_layout()
    fig.savefig(FIGURES / "main_result.png", dpi=150)


if __name__ == "__main__":
    main()
