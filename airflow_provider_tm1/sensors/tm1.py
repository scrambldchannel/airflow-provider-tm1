# from operator import eq, ge, gt, le, lt, ne
# from typing import Dict, Union

# from airflow.sensors.base import BaseSensorOperator
# from airflow.utils.decorators import apply_defaults
# from TM1py import TM1Service

# from airflow_provider_tm1.hooks.tm1 import TM1Hook

# class TM1CellValueSensor(BaseSensorOperator):
#     """
#     Checks the value of a single cell in a TM1 cube.
#     """

#     template_fields = ("cube", "elements")
#     ui_color = "#f0eee4"

#     @apply_defaults
#     def __init__(
#         self,
#         cube: str,
#         elements: str,
#         tm1_conn_id: str = "tm1_default",
#         value: Union[str, float],
#         op=eq,
#         *args,
#         **kwargs,
#     ) -> None:

#         super().__init__(*args, **kwargs)
#         self.tm1_conn_id = tm1_conn_id
#         self.cube = cube
#         self.elements = elements
#         self.op = op
#         self.value = value

#     def poke(self, context: Dict) -> bool:

#         tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

#         tm1:TM1Service = tm1_hook.get_conn()


#         return self.op(tm1.data.get_value(cube_name=self.cube, element_string=self.elements), self.value)


# class TM1ElementSensor(BaseSensorOperator):
#     """
#     Checks for the existence of an element in a dimension.
#     """

#     template_fields = ("dimension", "element")
#     ui_color = "#f0eee4"

#     @apply_defaults
#     def __init__(
#         self,
#         dimension: str,
#         element: str,
#         tm1_conn_id: str,
#         hierarchy: Optional[str] = None,
#         *args,
#         **kwargs,
#     ) -> None:
#         super().__init__(*args, **kwargs)
#         self.tm1_conn_id = tm1_conn_id
#         self.dimension = dimension
#         self.element = element
#         self.hierarchy = hierarchy

#     def poke(self, context: Dict) -> bool:

#         tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

#         tm1 = tm1_hook.get_conn()

#         print(
#             f"Sensor checks for existence of element {self.element} in dimension {self.dimension} on server {tm1_hook.db}."  # noqa
#         )

#         if not tm1.dimensions.exists(self.dimension):
#             raise Exception(f"Dimension {self.dimension} not found on TM1 server {tm1_hook.db}.")

#         if self.hierarchy:
#             if self.hierarchy not in tm1.dimensions.get(self.dimension).hierarchies():
#                 raise Exception(
#                     f"Dimension {self.dimension} has no hierarchy {self.hierarchy} on server {tm1_hook.db}."
#                 )

#             return tm1.dimensions.get(self.dimension).get_hierarchy(self.hierarchy).contains_element(self.element)
#         else:
#             for h in tm1.dimensions.get(self.dimension).hierarchies:
#                 return h.contains_element(self.element)
#             return False
