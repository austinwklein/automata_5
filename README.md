# Game Setup:  

---

#### Assumptions

---
- Input validation is out of scope for this assignment

## Running JumpIt

---

> JumpIt uses the `uv` package manager for virtual environments.  

> uv workflow: 
>   - Install uv:
>     - [MacOS & Linux](https://docs.astral.sh/uv/getting-started/installation/)
>     - [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)
>       - Scoop via ```scoop install main/uv```
>       - Choco via ```choco install uv```
>     - Bash - Via cURL
>       ```bash
>       curl -LsSf https://astral.sh/uv/install.sh | sh
>       ```
>   - Use uv:
>     - ```uv sync``` - Creates a virtual environment with the included toml file
>     - ```uv run python main.py``` - Runs the program in the virtual environment

Python version will be automatic via uv pyproject.toml file