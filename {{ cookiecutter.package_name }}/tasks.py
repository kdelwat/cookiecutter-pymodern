from invoke import task


@task
def clean(context):
    context.run('rm -rf build/')
    context.run('rm -rf dist/')
    context.run('rm -rf *.egg-info/')


@task
def build(context, clean=False):
    context.run('python setup.py sdist')
    context.run('python setup.py bdist_wheel')
