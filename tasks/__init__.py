from invoke import task


@task
def clean(ctx):
    """Delete existing docker containers"""
    ctx.run("docker rm -f $(docker ps -a -q)", warn=True)


@task
def docker_build(ctx):
    """Build the resource node docker image"""
    ctx.run("docker build . -f docker/Dockerfile -t resource-node")


@task
def docker_compose_up(ctx):
    """Starts the docker compose """
    ctx.run("docker-compose -f docker/docker-compose.yml up -d")


@task
def test_unit(ctx):
    """Run unit tests"""
    ctx.run("py.test tests/unit")


@task
def test_integration(ctx):
    """Run integration tests"""
    ctx.run("py.test tests/integration")


@task
def test_component(ctx):
    """Run component tests"""
    ctx.run("py.test tests/component")


@task(pre=[clean, test_unit, docker_build, docker_compose_up, integration_test, component_test])
def test(ctx):
    """Runs all tests and prerequisites"""
    pass
