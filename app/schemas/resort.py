from pydantic import BaseModel


class ResortOut(BaseModel):
    """Minimal resort representation — just enough for a dropdown/widget list."""

    resort_name: str

    model_config = {"from_attributes": True}
