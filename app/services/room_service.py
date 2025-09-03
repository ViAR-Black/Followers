class MixInRoomService:
    def __init__(self, room_repo):
        pass

class PostRoomService(MixInRoomService):
    def __init__(self, room_repo):
        super().__init__(room_repo)

    async def __call__(self):
        '''
        Валидация названия
        Не больше 50 комнат у создателя
        '''
        pass

class GetRoomService(MixInRoomService):
    def __init__(self, room_repo):
        super().__init__(room_repo)

    async def __call__(self):
        pass

class DeleteRoomService(MixInRoomService):
    def __init__(self, room_repo):
        super().__init__(room_repo)


    async def __call__(self):
        '''
        Проверка что комната существует
        Проверка прав на удаление
        '''

class PatchRoomService(MixInRoomService):
    def __init__(self, room_repo):
        super().__init__(room_repo)

    async def __call__(self):
            '''
            Валидация названия
            Проверка прав на изменение/добавление
            Проверка наличия изменений
            '''

