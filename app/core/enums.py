from enum import Enum


class ResortName(str, Enum):
    """
    Fixed, known set of resorts. Using `str, Enum` means FastAPI:
      - validates incoming path values against these exact members
        (invalid value -> automatic 422, your route function never runs)
      - renders a real dropdown for this parameter in Swagger UI (/docs)
      - serializes cleanly to a plain string in JSON

    Adding a new resort means editing this file + redeploying. That's an
    accepted trade-off for a small, rarely-changing set of resorts. If this
    ever needs to change without a deploy, that's the signal to extract a
    real `resorts` dimension table and switch to a DB-backed lookup instead.
    """

    bansko = "Bansko"
    pamporovo = "Pamporovo"
    borovets = "Borovets"