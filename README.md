# Tensor Calculator

TensorCalculator is a Python module for performing some calculations and operations with tensors.

## Features

- Basic tensor operations (sum, multiplication, square).
- All zeros, all ones, and random numbers tensors given a shape size
- Tensor reshaping.
- Tensor normalizing.
- Tensor ground division.

## Installation

You can install TensorCalculator using `pip`:

```bash
pip install -U git+https://github.com/alfonsinacl/TensorCalculator.git
```
## Usage

import TensorCalculator

## Create a tensor
A = TensorCalculator((3, 2))
### Create a random tensor
tensor_ex = my_tensor.random_tensor() 
### Reshape the random tensor
my_tensor.reshape_tensor(tensor_ex, (4, 3))
### Sum it with another tensor
tensor_ex_2 = my_tensor.random_tensor() 
tensor_sum = my_tensor.sum_tensor(tensor_ex, tensor_ex_2)
tensor_sum

### Print the result
print(result)


