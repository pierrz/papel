from typing import List, Union

import numpy as np
from src.db.database import close_db_connection, init_db_connection
from worker import celery, logger


@celery.task(name="init_check_task")
def init_check_task(*args):
    logger.info(f"This comes in : {args}")
    return args[0], args[1]


@celery.task(name="dummy_task")
def dummy_task(input_int: int) -> List[int]:

    result = int(np.multiply(input_int, input_int))
    logger.info(f"=> Calculated: {result}")

    conn, cur = init_db_connection()
    cur.execute(
        "CREATE TABLE test_celery (id serial PRIMARY KEY, input integer, result integer);"
    )
    cur.execute(
        f"INSERT INTO test_celery (input, result) VALUES ({input_int}, {result});"
    )
    conn.commit()

    logger.info(f"=> Database loaded: {result}")
    close_db_connection(cur, conn)

    return [input_int, result]


@celery.task(name="check_db")
def check_db_task(io_pack: List[int]) -> Union[List[Union[str, int]], bool]:

    input_int, result = io_pack

    conn, cur = init_db_connection()
    cur.execute("SELECT * FROM test_celery;")
    db_input, db_result = cur.fetchone()[1:]

    # drop celery test table
    cur.execute("DROP TABLE test_celery;")
    conn.commit()

    close_db_connection(cur, conn)
    logger.info(f"=> Retrieved from DB: [{db_input}, {db_result}]")

    if (db_input, db_result) == (input_int, result):
        return ["success", input_int, result]
    else:
        return False
