import torch
# from dataclasses import dataclass

__all__ = ['TensorCalculator']
# __all__ is a special variable that defines what's accessible when someone imports the module


# @dataclass
class TensorCalculator:
    def __init__(self, shape: tuple):
        shape = self.shape

    def zeros_tensor(self):
        return torch.zeros(self.shape)

    def ones_tensor(self):
        return torch.ones(self.shape)

    def random_tensor(self):
        return torch.rand(self.shape)

    @staticmethod
    def sum_tensor(tensor1, tensor2):
        if tensor1.size() != tensor2.size() and tensor2.size() != tensor1.size():
            raise ValueError("Tensors must have the same shape to perform the operation")
        return tensor1 + tensor2

    @staticmethod
    def mult_tensor(tensor1, tensor2):
        if tensor1.size() != tensor2.size() and tensor2.size() != tensor1.size():
            raise ValueError("Tensors must have the same shape to perform the operation")
        return tensor1 * tensor2

    @staticmethod
    def square_tensor(tensor: torch.Tensor):
        return tensor ** 2

    @staticmethod
    def ground_tensor(tensor: torch.Tensor, divisor: int):
        final_tensor = tensor // divisor
        return final_tensor

    @staticmethod
    def normalized_tensor(tensor: torch.Tensor):
        mean = torch.mean(tensor)
        std = torch.std(tensor)
        normalized = (tensor - mean) / std
        return normalized

    @staticmethod
    def reshape_tensor(tensor: torch.Tensor, new_shape: tuple):
        if torch.numel(tensor) != torch.numel(torch.empty(new_shape)):
            raise ValueError("New shape must have the same number of elements as the original tensor.")
        reshaped_tensor = tensor.view(new_shape)
        return reshaped_tensor


my_tensor = TensorCalculator((3, 4))
tensor_ex = my_tensor.random_tensor()
my_tensor.ground_tensor(tensor_ex, 0.1)
tensor_ex
tensor_ex_reshaped = my_tensor.reshape_tensor(tensor_ex, (4, 3))
tensor_ex_2 = my_tensor.random_tensor()
tensor_sum = my_tensor.sum_tensor(tensor_ex, tensor_ex_2)
tensor_sum


