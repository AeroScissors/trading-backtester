# backtester/indicators/registry.py

import importlib.util
import os
from .base import IndicatorBase

_INDICATORS = {}

def register_indicator(cls):
    if not issubclass(cls, IndicatorBase):
        raise TypeError("Indicator must inherit from IndicatorBase.")
    _INDICATORS[cls.name] = cls

def get_indicator(name):
    return _INDICATORS.get(name)

def load_user_indicator(filepath):
    """
    Dynamically load a Python file and register any IndicatorBase subclass.
    Returns the indicator's name if registration is successful.
    """
    module_name = os.path.splitext(os.path.basename(filepath))[0]
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, type) and issubclass(obj, IndicatorBase) and obj is not IndicatorBase:
            register_indicator(obj)
            return obj.name
    raise ValueError("No valid IndicatorBase subclass found in user file.")
