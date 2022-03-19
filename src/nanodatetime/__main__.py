"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Nanodatetime."""


if __name__ == "__main__":
    main(prog_name="nanodatetime")  # pragma: no cover
