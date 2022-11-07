# I. Transcribe Youtube Videos
from .util import *
import os

def env_setup():
  command_ls = "nvidia-smi| pip install git+https://github.com/huggingface/huggingface_hub.git | pip install diffusers | pip install transformers scipy ftfy | pip install accelerate"
  os.system(command_ls)

def login(token):
  """Login to HuggingFace using your token at https://huggingface.co/settings/tokens"""
  env_setup()
  from huggingface_hub.hf_api import HfFolder
  HfFolder.save_token(token)
  return "Your token has been saved to /root/.huggingface/token"

def pipe_gen(token):
  login(token)
  import torch
  from diffusers import StableDiffusionPipeline
  pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)  
  pipe = pipe.to("cuda")
  return pipe

def image_gen(image_description, pipe, height=600, width=800):
  prompt = image_description
  image = pipe(prompt, height=height, width=width).images[0]
  return image