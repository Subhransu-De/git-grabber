from pydantic import BaseModel, field_validator


class Repository(BaseModel):
    name: str
    ssh: str

    @field_validator('ssh')
    def validate_ssh_url(cls, value):
        if not value.startswith('git@'):
            raise ValueError('Must start with git@')
        if ':' not in value:
            raise ValueError('Must contain a colon')
        if not value.endswith('.git'):
            raise ValueError('Must end with .git')
        return value
