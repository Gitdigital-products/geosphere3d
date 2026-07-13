# Contributing to CipherForge

## Quick Start
```bash
git clone https://github.com/cipherforge/cipherforge.git
cd cipherforge
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Crypto Contributions

All cryptographic contributions require:
- Reference to NIST/industry standard
- Security review by a cryptography reviewer
- Test vectors from official sources
- No custom crypto primitives (use established algorithms)

## Guidelines
- Python 3.10+ with type hints
- Ruff for linting
- Conventional Commits for commit messages
- Sign off with `git commit -s` (DCO)
