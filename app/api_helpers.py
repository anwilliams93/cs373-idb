def filter_query_parameters(allowed_parameters, request_parameters):
	filtered_parameters = {}
	for k in allowed_parameters:
		if k in request_parameters:
			filtered_parameters[k] = request_parameters[k]
	return filtered_parameters

def select(table, predicate):
	return filter(predicate, table)