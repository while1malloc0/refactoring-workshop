def crawl_project_information(url: str):
    protocol_handler = url.split("://")[0]
    if protocol_handler != "https":
        raise Excpetion("Non-TLS connections not allowed")
    
    query_params_str = url.split("?")[1]
    query_params_raw = query_params_str.split("&")
    query_params = {}
    for param in query_params_raw:
        k, v = param.split("=")
        query_params[k] = v
    
    project = query_params[project]
    do_stuff_with_project(project, query_params)


def crawl_user_information(url: str):
    protocol_handler = url.split("://")[0]
    if protocol_handler != "https":
        raise Excpetion("Non-TLS connections not allowed")

    # etc.

