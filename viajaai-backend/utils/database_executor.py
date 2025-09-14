from .database import DatabaseManager
from typing import List, Dict, Any, Optional, Union

class DataBaseExecutor:
    def __init__(self,db_manager : DatabaseManager):
        self.db_manager = db_manager

    def execute_select(self,query: str, params : Optional[Union[tuple, list, dict]]=None) -> List[Dict]:
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            
                result = cursor.fetchall()
                return result
            
            except Exception as e:
                raise Exception(f"Select error: {e}")

    def execute_insert(self,query: str, params: Optional[Union[tuple, list, dict]] = None) -> int:
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            
                return cursor.lastrowid
            
            except Exception as e:
                raise Exception(f"Insert error: {str(e)}")

    def execute_delete(self, query: str, params: Optional[Union[tuple, list, dict]] = None) -> int:
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            
                return cursor.rowcount
            
            except Exception as e:
                raise Exception(f"Delete error: {str(e)}")

    def execute_update(self, query: str, params: Optional[Union[tuple, list, dict]] = None) -> int:
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            
                return cursor.rowcount
            except Exception as e:
                raise Exception(f"Update error: {str(e)}")


# Singletons
db_manager = DatabaseManager()
db_executor = DataBaseExecutor(db_manager)