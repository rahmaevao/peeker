import subprocess

import click


@click.command()
@click.option(
    "--path",
    default="~",
    help="The path to the image file or folder containing the images.",
)
def run_peeker_from_streamlit(path):
    subprocess.call(["streamlit", "run", "src/main.py", "--", path])


if __name__ == "__main__":
    run_peeker_from_streamlit()
