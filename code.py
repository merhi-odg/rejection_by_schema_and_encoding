# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import logging
import warnings

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

    if not isinstance(data, dict):
        raise UserWarning("Bad Input: input data should be a dictionary")
    if not "input" in data:
        warnings.warn("Key 'input' missing from input data", category=UserWarning)
    if data["input"]==0:    
        raise UserWarning("Bad Input: DivisionByZero Expected!")
    
    output = {"reciprocal": 1/data["input"]}

    yield output