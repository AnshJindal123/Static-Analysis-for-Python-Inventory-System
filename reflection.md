# Reflection — Static Code Analysis Lab


1. Which issues were the easiest to fix, and which were the hardest? Why?


- Easiest: Unused imports, formatting/PEP8 issues, and missing docstrings were straightforward because they are mechanical changes and have no functional impact. Tools give direct hints.
- Hardest: Refactoring away the global variable and removing `eval()` were harder because they required redesigning code flow (migrating to a class), ensuring behavior remained the same, and adding appropriate input validation.


2. Did the static analysis tools report any false positives? If so, describe one example.


- No critical false positives were encountered. Some stylistic warnings (e.g., overly strict docstring requirements or naming conventions) are guidance rather than actual bugs. For example, Pylint initially flagged global usage and naming conventions — these were design choices but still worth addressing for best practices.


3. How would you integrate static analysis tools into your actual software development workflow?


- Locally: Install pre-commit hooks that run Flake8 and Pylint on staged files to catch issues before commits.
- CI/CD: Add pipeline steps (GitHub Actions / GitLab CI) to run Pylint, Flake8, and Bandit on pull requests. Configure thresholds (e.g., prevent merge on High severity Bandit issues or Pylint score < 8.0).
- Developer onboarding: Include tool configuration files (`.pylintrc`, `.flake8`, `bandit.yml`) and documentation so team members can run checks locally.


4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?


- The code is more maintainable and modular after refactoring into a class.
- File operations are safer (using `with` and explicit encodings), reducing I/O-related bugs.
- Security: removing `eval()` eliminated a high-risk vulnerability reported by Bandit.
- Readability: PEP8-compliant names and docstrings make the code easier to understand and extend.