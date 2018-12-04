from abc import ABCMeta, abstractmethod

### Abstract Base Class Property 


    class AbstractSQLSaver(metaclass=ABCMeta):
    SERVER = 'AWS'
    DB = 'SoE'

    @property
    def table_name(self):
        return self._table_name

    @property
    @abstractmethod
    def _table_name(self):
        pass
        
    # Ensure that the subclass has `_table_name` - else errors if instantiated
    
    class ConcreteSQLSaver(AbstractSQLSaver):
        _table_name = 'GAS'
        
    class ConcreteSQLSaver2(AbstractSQLSaver): pass
        
    # Ensure that the table name's setter/getter is of correct type
    
    class ConcreteSQLSaver3(AbstractSQLSaver):
        _table_name = None
        
        def __init__(self, table_name):
            self.table_name = table_name
        
        @property
        def table_name(self):
            return super().table_name

        @table_name.setter
        def table_name(self, value):
            if issubclass(str, type(value)):
                self._table_name = value
                return
            raise ValueError(f'Cannot set table_name. {value} must be type str')
            
            
## Usage:
>>> x = ConcreteSQLSaver() # works fine, as _table_name is defined
>>> y = ConcreteSQLSaver2() # Errors
>>> z = ConcreteSQLSaver3('gas_table') # works fine
>>> a = ConcreteSQLSaver3(123) # errors - not correct type
