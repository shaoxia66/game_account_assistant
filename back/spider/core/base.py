from abc import ABC, abstractmethod
from database.Cmongo import DBOperation
import logging
import os
class Spider_base(ABC):

    def __init__(self, db:DBOperation):
        self._db = db
        self._logger = logging
    @abstractmethod
    async def get_all_transaction_records(self):
        pass

    @abstractmethod
    async def get_search(self):
        pass