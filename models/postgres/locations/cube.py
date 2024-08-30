from sqlalchemy.sql.type_api import UserDefinedType


class Cube(UserDefinedType):
    def get_col_spec(self):
        return "CUBE"

    def bind_expression(self, _):
        return _

    def column_expression(self, col):
        return col

    def bind_processor(self, _):
        def process(value):
            if isinstance(value, (list, tuple)):
                return f"({','.join(map(str, value))})"
            return value
        return process

    def result_processor(self, _, __):
        def process(value):
            if value is not None:
                return eval(value)
            return value
        return process
