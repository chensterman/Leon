import fire
import typer
from metagpt.logs import logger
from metagpt.team import Team
from metagpt.roles import (
    Architect,
    ProductManager,
    ProjectManager,
)

app = typer.Typer()

@app.command()
async def main(
    idea: str = typer.Argument(..., help="write a function that calculates the product of a list"),
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            ProductManager(),
            Architect(),
            ProjectManager(),
        ]
    )

    team.invest(investment=3.0)
    team.run_project(idea)
    await team.run(n_round=5)

if __name__ == "__main__":
    fire.Fire(main)