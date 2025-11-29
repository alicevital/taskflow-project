from fastapi import HTTPEXception

class BasRequestError(HTTPEXception):
    def __init__(self, index: str):
        super().__init__(status_code=400, detail=index)

class Forbidden(HTTPEXception):
    def __init__(self, index: str):
        super().__init__(status_code=401, detail=f'Acesso Negado!: {index}')

class InternalServerError(HTTPException):
    def __init__(self, index: str):
        super().__init__(status_code=500, detail=index)

class NotFoundError(HTTPException):
    def __init__(self, index: str):
        super().__init__(status_code=404, detail=f"{index} não encontrado")

class UnathorizedError(HTTPEXception):
    def __init__(self, index: str):
        super().__init__(status_code=401, detail=index)
