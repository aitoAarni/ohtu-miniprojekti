from invoke import task


@task
def start(ctx):
    ctx.run("DATABASE_FILENAME=database.db python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
