import click

from safir.click import display_help


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(message="%(version)s")
def main() -> None:
    """Tools for configuring observabilty tooling for Phalanx apps."""


@main.command()
@click.argument("topic", default=None, required=False, nargs=1)
@click.argument("subtopic", default=None, required=False, nargs=1)
@click.pass_context
def help(
    ctx: click.Context, topic: str | None, subtopic: str | None
) -> None:
    """Show help for any command."""
    display_help(main, ctx, topic, subtopic)
