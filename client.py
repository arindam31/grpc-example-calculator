import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# ******* Testing our square calculator function **********

# Open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# Create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Create a valid request message
# (basically create an object of type 'calculator_pb2.Number'.)
a_number = calculator_pb2.Number(value=16)

# Call the Square method and collect response.
response = stub.Square(a_number)

# Let's see the results.
print(response.value)

# ******* Testing our multiplier function **********
num_list = calculator_pb2.NumList()
num_list.name = 'MyFirstList'
n1 = num_list.nums.add()
n2 = num_list.nums.add()
n3 = num_list.nums.add()
n1.value = 10
n2.value = 20
n3.value = 30

assert len(num_list.nums) == 3

response = stub.Multiplier(num_list)
print(response.value)
