class InsecureProtocolException(Exception):
    pass


class Url:
    def __init__(self, protocol_handler, query_params):
        self.protocol_handler = protocol_handler
        self.query_params = query_params

    @classmethod
    def from_string(raw: str):
        url = Url()
        url.protocol_handler = url._parse_protocol_handler(raw)
        url.query_params = url._parse_query_params(raw)

    def raise_for_insecure_connnections(self):
        if self.protocol_handler != "https":
            raise InsecureProtocolException("It's not 1999 anymore. Use TLS")

    def _parse_protocol_handler(raw: str):
        return url.split("://")[0]

    def _parse_query_params(raw: str):
        query_params_str = raw.split("?")[1]
        query_params_raw = query_params_str.split("&")
        query_params = {}
        for param in query_params_raw:
            k, v = param.split("=")
            query_params[k] = v
        return query_params
        

def crawl_project_information(url: Url):
    url.raise_for_insecure_connnections()
    project = url.query_params["project"]
    do_stuff_with_project(project)


def crawl_user_information(url: Url):
    url.raise_for_insecure_connnections()
    # etc.

