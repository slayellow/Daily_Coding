import torch

# Pytorch GPU 버전 사용을 위해선 mps 입력 필요
print(torch.device('mps'))
