# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import logging
import numpy

# Line below is not needed since engine's jet.py set it globally
# warnings.filterwarnings("error", category=UserWarning) # Coerce UserWarnings into erros

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


# modelop.init
def begin() -> None:
    pass


# modelop.score
def action(data: float) -> dict:
    """
    param: data: dict of the form {"input": x} for some number x
    """
    
    logger.info("Input to action(): %s", data)
    
    if data["input"]==0:
        # Cause rejection by output schema by yielding string value instead of float
        output = {"reciprocal": "N/A"}
    elif data["input"]==42:
        # Cause rejection by output schema by yielding array of dict instead of dict
        output = [{"reciprocal": 1/42}]
    elif data["input"]==3.14:
        # Cause rejection by JSON encoding on output by yielding numpy.nan (not serializable as null)
        output = {"reciprocal": numpy.nan}
    else:
        # No rejections
        output = {"reciprocal": 1/data["input"]}

    yield output