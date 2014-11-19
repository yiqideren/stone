import pprint

# language by language regex for finding what functions have already been defined

from babelapi.lang.lang import TargetLanguage
from babelapi.data_type import (
    Boolean,
    Float32,
    Float64,
    Int32,
    Int64,
    List,
    String,
    Timestamp,
    UInt32,
    UInt64,
)

class PythonTargetLanguage(TargetLanguage):

    _language_short_name = 'py'

    def get_supported_extensions(self):
        return ('.py', )

    _type_table = {
        Boolean: 'bool',
        Float32: 'float',
        Float64: 'float',
        Int32: 'int',
        Int64: 'long',
        List: 'list',
        String: 'str',
        UInt32: 'long',
        UInt64: 'long',
        Timestamp: 'datetime',
    }

    def format_type(self, data_type):
        return PythonTargetLanguage._type_table.get(data_type.__class__,
                                                    self.format_class(data_type.name))

    def format_obj(self, o):
        return pprint.pformat(o, width=1)

    def format_variable(self, name):
        return '_'.join([word.lower() for word in self.split_words(name)])

    def format_class(self, name):
        return ''.join([word.capitalize() for word in self.split_words(name)])

    def format_method(self, name):
        return '_'.join([word.lower() for word in self.split_words(name)])