from nameko.exceptions import registry

def remote_error(exc_path):
    
    def wrapper(exc_type):
        registry[exc_path] = exc_type
        return exc_type
    
    return wrapper

@remote_error('airline.exception.NotFound')
class AirlineNotFound(Exception):
    pass