"""Command-line interface for TurboJenkins POC."""
try:
    import typer
except Exception:  # pragma: no cover - fallback for test/runtime when typer isn't installed
    # Minimal fallback so modules can be imported during tests without optional deps
    class _DummyApp:
        def command(self, *a, **k):
            def _dec(f):
                return f
            return _dec

        def __call__(self, *a, **k):
            return None

    class _DummyOption:
        def __init__(self, *a, **k):
            pass

    typer = type("typer", (), {"Typer": _DummyApp, "Option": _DummyOption})

try:
    from rich.console import Console
except Exception:  # pragma: no cover - provide simple fallback for environments without rich
    class Console:  # very small subset used in CLI
        def print(self, *args, **kwargs):
            sep = kwargs.get("sep", " ")
            end = kwargs.get("end", "\n")
            text = sep.join(str(a) for a in args)
            # strip rich markup if present
            import re

            text = re.sub(r"\[/?[a-zA-Z0-9#,-_.]+\]", "", text)
            print(text, end=end)


from turbojenkins.jenkins_client import JenkinsClient
from turbojenkins.ai_engine import ask_optimization

app = typer.Typer()
console = Console()


@app.command()
def analyze(job: str = typer.Option(..., help="Jenkins job name to analyze"),
            builds: int = typer.Option(10, help="Number of recent builds to sample")):
    """
    Connect to Jenkins, fetch Jenkinsfile + build times, ask Gemini for optimizations.
    """
    try:
        jc = JenkinsClient()
    except Exception as e:
        console.print(f"[red]Jenkins connection error:[/red] {e}")
        raise typer.Exit(code=1)

    console.print(f"[bold]Fetching job:[/bold] {job}")
    try:
        config_xml = jc.get_job_config(job)
        avg = jc.get_avg_build_time_minutes(job, builds)
    except Exception as e:
        console.print(f"[red]Error fetching job data:[/red] {e}")
        raise typer.Exit(code=2)

    console.print(f"[bold]Average build time (min):[/bold] {avg:.2f}")
    console.print("[bold]Requesting AI recommendations...[/bold]")
    recommendations = ask_optimization(job, config_xml, avg)
    console.rule("[green]Recommendations")
    console.print(recommendations)
