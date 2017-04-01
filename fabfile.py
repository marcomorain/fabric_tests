from fabric.api import env, run, task, warn_only, roles, get, put, execute
from fabric.operations import local

@task
def task():
    local("xcversion simulators --install='iOS 8.1'")
