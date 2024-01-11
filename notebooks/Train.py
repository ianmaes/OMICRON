import os
import torch
import torch.nn as nn 
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"  
os.environ["CUDA_VISIBLE_DEVICES"]="0" # GPU index

device = torch.device('cuda:0') if torch.cuda.is_available() else 'cpu'
print(device)