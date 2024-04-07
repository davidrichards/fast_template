from dataclasses import asdict
import json
import yaml
from rec_avro import to_rec_avro_destructive, from_rec_avro_destructive


def _get_dict(o):
    try:
        data = asdict(o)
    except:
        data = o.__dict__
    if hasattr(o, "_serialize_exclude"):
        for key in o._serialize_exclude:
            if key in data:
                del data[key]
    return data


def serialize(o, format="dict"):
    """Serializes a dataclass object to a given format."""
    if format == "dict":
        return _get_dict(o)
    elif format == "json":
        return json.dumps(_get_dict(o))
    elif format == "yaml":
        return yaml.dump(_get_dict(o))
    elif format == "avro":
        # NOTE: writing to a file requires rec_avro_schema, as well as fastavro
        return to_rec_avro_destructive(_get_dict(o))
    else:
        raise NotImplementedError(f"Format {format} is not supported.")


def deserialize(o, cls, format="dict"):
    """Deserializes a dataclass object prepared in a given format."""
    if isinstance(o, cls):
        return o
    elif format == "dict":
        return cls(**o)
    elif format == "json":
        return cls(**json.loads(o))
    elif format == "yaml":
        return cls(**yaml.load(o, Loader=yaml.FullLoader))
    elif format == "avro":
        return cls(**from_rec_avro_destructive(o))
    else:
        raise NotImplementedError(f"Format {format} is not supported.")


# __all__ = ["serialize", "deserialize"]
