__all__ = ["functional_dict"]


class functional_dict(dict):
    """Functional.notation to access dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
