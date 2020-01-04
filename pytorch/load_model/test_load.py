import torch
import torchvision.models as models

# step1: load model arch
net = models.AlexNet()

# step2: load model weight
filepth = "alexnet-owt-4df8aa71.pth"
model = torch.load(filepth)

# step3: match arch with weight
# net = net.load_state_dict(model)
# 上述赋值，会导致_IncompatibleKeys object is not callable
# net.load_state_dict不可以用作返回
net.load_state_dict(model)

# step4: ignore backward features
net.eval().float()

# step5: start run
example_in = torch.ones(1,3,224,224)
example_out = net(example_in)

print(example_in)
