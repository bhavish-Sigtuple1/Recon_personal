from .wbc_executor import WBC_Executor
from .rbc_executor import RBC_Executor
from .platelet_executor import Platelet_Executor



def Executor_Factory(type='RBC', **kwargs):
    """
    Factory function to create an executor object based on the given type.

    Args:
        type (str): The type of executor to create. Defaults to 'RBC'.
        **kwargs: Additional keyword arguments to pass to the executor constructor.

    Returns:
        An instance of the executor object of the given type.
    """
    executor = {
        "RBC": RBC_Executor,
        "WBC": WBC_Executor,
        "Platelet": Platelet_Executor,
        "Hb": Hb_Executor
    }
 
    return executor[type](**kwargs)