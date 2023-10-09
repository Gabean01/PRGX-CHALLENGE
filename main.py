from fastapi import FastAPI

# Application Environment Configuration
#env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    #title=env.APP_NAME,
    #version=env.API_VERSION
)