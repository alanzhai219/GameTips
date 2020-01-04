import torch
import torch.nn as nn

class TestForHook(nn.Module):
	def __init__(self):
		super().__init__()
		self.linear_1 = nn.Linear(in_features=2, out_features=2)
		self.linear_2 = nn.Linear(in_features=2, out_features=1)
		self.relu = nn.ReLU()
		self.relu6 = nn.ReLU6()
		self.initialize()

	def forward(self, x):
		linear_1 = self.linear_1(x)
		linear_2 = self.linear_2(linear_1)
		relu = self.relu(linear_2)
		relu_6 = self.relu6(relu)
		layers_in = (x, linear_1, linear_2)
		layers_out = (linear_1, linear_2, relu)
		return relu_6, layers_in, layers_out

	def initialize(self):
		'''
		initialization parameters
		'''
		self.linear_1.weight = torch.nn.Parameter(torch.FloatTensor([[1,1], [1,1]]))
		self.linear_1.bias = torch.nn.Parameter(torch.FloatTensor([1,1]))
		self.linear_2.weight = torch.nn.Parameter(torch.FloatTensor([[1,1]]))
		self.linear_2.bias = torch.nn.Parameter(torch.FloatTensor([1]))
		return True

# 1. define containers for hook
module_name = []
features_in_hook = []
features_out_hook = []

# 2. define hook function
def hook(module, fea_in, fea_out):
	print("hooker working")
	module_name.append(module.__class__)
	features_in_hook.append(fea_in)
	features_out_hook.append(fea_out)
	return None

# 3. define input
x = torch.FloatTensor([[0.1, 0.1], [0.1, 0.1]])

# 4. register hook for a specific layer
net = TestForHook()
net_children = net.children()
for child in net_children:
	if not isinstance(child, nn.ReLU6):
		child.register_forward_hook(hook=hook)

# 5. test net output
out, features_in_forward, features_out_forward = net(x)
print("*"*5+"forward return features"+"*"*5)
print(features_in_forward)
print(features_out_forward)
print("*"*5+"forward return features"+"*"*5)

# 6. test hook 
print("*"*5+"hook record features"+"*"*5)
print(features_in_hook)
print(features_out_hook)
print("*"*5+"hook record features"+"*"*5)

# 7. compare feature_out with hook
print("sub result")
for forward_return, hook_record in zip(features_in_forward, features_in_hook):
	print(forward_return - hook_record[0])
