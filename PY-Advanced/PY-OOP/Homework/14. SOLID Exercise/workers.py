from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker: BaseWorker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f'`worker` must be of type {BaseWorker.__class__.__name__}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
