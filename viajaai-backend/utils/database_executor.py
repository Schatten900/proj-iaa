from typing import List, Dict, Any, Optional, Union
from .database import DatabaseManager


class DataBaseExecutor:
    """
    Classe responsável por executar operações no banco de dados (SELECT, INSERT, UPDATE, DELETE)
    de forma segura e padronizada, utilizando o DatabaseManager para gerenciar conexões.

    Essa camada abstrai o uso direto de cursores e conexões,
    facilitando o reuso e o tratamento de erros.
    """

    def __init__(self, db_manager: DatabaseManager):
        """
        Inicializa o executor com uma instância de DatabaseManager.

        :param db_manager: Gerenciador de conexões com o banco de dados.
        """
        self.db_manager = db_manager

    # ------------------------- MÉTODOS DE EXECUÇÃO -------------------------

    def execute_select(
        self,
        query: str,
        params: Optional[Union[tuple, list, dict]] = None
    ) -> List[Dict[str, Any]]:
        """
        Executa uma consulta SELECT no banco de dados.

        :param query: Query SQL a ser executada.
        :param params: Parâmetros opcionais para a query.
        :return: Lista de dicionários contendo os registros retornados.
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute(query, params or ())
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise Exception(f"Erro ao executar SELECT: {e}")

    def execute_insert(
        self,
        query: str,
        params: Optional[Union[tuple, list, dict]] = None
    ) -> int:
        """
        Executa uma operação INSERT e retorna o ID do último registro inserido.

        :param query: Query SQL de inserção.
        :param params: Parâmetros opcionais para a query.
        :return: ID do registro recém-inserido.
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.lastrowid
            except Exception as e:
                raise Exception(f"Erro ao executar INSERT: {e}")

    def execute_delete(
        self,
        query: str,
        params: Optional[Union[tuple, list, dict]] = None
    ) -> int:
        """
        Executa uma operação DELETE e retorna o número de linhas afetadas.

        :param query: Query SQL de exclusão.
        :param params: Parâmetros opcionais para a query.
        :return: Quantidade de linhas removidas.
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.rowcount
            except Exception as e:
                raise Exception(f"Erro ao executar DELETE: {e}")

    def execute_update(
        self,
        query: str,
        params: Optional[Union[tuple, list, dict]] = None
    ) -> int:
        """
        Executa uma operação UPDATE e retorna o número de linhas afetadas.

        :param query: Query SQL de atualização.
        :param params: Parâmetros opcionais para a query.
        :return: Quantidade de linhas alteradas.
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.rowcount
            except Exception as e:
                raise Exception(f"Erro ao executar UPDATE: {e}")


# ------------------------- SINGLETONS GLOBAIS -------------------------

# Instâncias únicas (singleton) para uso compartilhado em toda a aplicação.
# Garantem que haja apenas uma conexão e um executor ativos por vez.
db_manager = DatabaseManager()
db_executor = DataBaseExecutor(db_manager)
