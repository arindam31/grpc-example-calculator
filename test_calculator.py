import time
import uuid

import grpc
from locust import task
from locust import User
from locust import TaskSet

from proto.calculator_pb2_grpc import CalculatorStub
from proto import calculator_pb2


class TesterClient:
    Number = calculator_pb2.Number

    def __init__(self):
        self.host = "localhost:8787"
        self.channel = grpc.insecure_channel('localhost:50051')

    def say_hello(self, request: calculator_pb2.Number) -> calculator_pb2.Number:
        stub = CalculatorStub(self.channel).Square

        #resp, call = stub.with_call(request=request, metadata=self.get_grpc_metadata())
        resp, call = stub.with_call(request=request, metadata=self.get_grpc_metadata())
        print(call)
        print(resp)

    @staticmethod
    def get_grpc_metadata():
        # request headers
        md = [
            ("authorization", "Bearer xxxxxxxxxxxxxxxx"),
            ("id", str(uuid.uuid4()))
        ]
        return md


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def say_hello(self):
        req_data = calculator_pb2.Number(value=16)
        self.locust_request_handler("say_hello", req_data)

    def locust_request_handler(self, grpc_name, req_data):
        req_func = self._get_request_function(grpc_name)
        start = time.time()
        result = None
        try:
            result = req_func(req_data)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_failure.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0, exception=e)
        else:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_success.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0)
        return result

    def _get_request_function(self, grpc_name):
        req_func_map = {
            "say_hello": self.client.say_hello,
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()