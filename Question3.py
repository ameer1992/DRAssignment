def chunks(l, n):
	for i in range(0, len(l), n):
        yield l[i:i + n]


MAX_ITEMS_IN_COLUMN_FILTER = 2

def check_if_data_one_chunk(kwargs):
    for x, y in kwargs.items():
        if len(y) > MAX_ITEMS_IN_COLUMN_FILTER:
            return False
    return True


def db_query(table_name, **kwargs):

    db_queires = []

    if check_if_data_one_chunk(kwargs):
        where_clause = ' and '.join([
          f'{x} in ({ ",". join([t for t in y])})' for x, y in kwargs.items()])
        statement=  f'SELECT * from {table_name} where {where_clause};'
        return [statement]

    for x, y in kwargs.items():
        if len(y) > MAX_ITEMS_IN_COLUMN_FILTER:
            for _chunk in chunks(y, MAX_ITEMS_IN_COLUMN_FILTER):
                kwargs[x] = _chunk
                db_queires = db_queires + db_query(table_name, **kwargs)
            break

    return db_queires    
