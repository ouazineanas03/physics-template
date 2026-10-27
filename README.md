# Project title

[![CI](https://github.com/ouazineanas03/physics-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ouazineanas03/physics-template/actions/workflows/ci.yml)

One sentence: what physical question does this project answer, and what is the main result?

## Question

State the problem precisely. Which system, which quantity, which regime?

## Method

Describe the numerical method or model in a few lines. Give the equations that
matter and say why you chose this approach over alternatives.

## Results

![Main result](figures/main_result.png)

State the key number with its uncertainty, for example:
*convergence order of RK4 measured as 4.01 ± 0.03 (expected: 4).*

## Validation

How do you know the result is correct? Compare with an analytic solution, a
known limit, or a published value, and report the agreement.

## Reproduce

```bash
git clone https://github.com/ouazineanas03/REPO.git
cd REPO
python -m venv .venv && source .venv/bin/activate
make install
make test
python scripts/run_experiment.py   # regenerates every figure in figures/
```

Everything in `figures/` must be reproducible with the commands above in
under 10 minutes.

## Project structure

```
src/physproj/   library code
tests/          unit tests (run by CI on every push)
figures/        generated figures
```

## Limitations

What does the method not do well? Where does it break down?

## References

List textbooks, papers, or datasets used.

## License

MIT, see [LICENSE](LICENSE).
