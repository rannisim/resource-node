from invoke import task


@task
def clean(ctx):
    ctx.run("docker rm -f $(docker ps -a -q)", warn=True)

@task
def docker_build(ctx):
    ctx.run("docker build . -f docker/Dockerfile -t resource-node")

@task
def docker_compose_up(ctx):
    ctx.run("docker-compose -f docker/docker-compose.yml up -d")

@task
def unit_test(ctx):
    ctx.run("py.test tests/unit")

@task
def integration_test(ctx):
    ctx.run("py.test tests/integration")

@task
def component_test(ctx):
    ctx.run("py.test tests/component")

@task(pre=[clean, unit_test, docker_build, docker_compose_up, integration_test, component_test])
def test(ctx):
    pass


