from prefect import flow, task

@task(name="say_hello", log_prints=True)
def say_hello():
    print("Hello, I'm a Task!")

@flow(name="hello-flow", log_prints=True)
def flow_hello():
    print("Hello, I'm a Flow!")
    print("I'm about to call a Task...")
    say_hello()

if __name__ == "__main__":
    flow_hello()
