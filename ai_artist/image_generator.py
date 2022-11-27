# I. Transcribe Youtube Videos
from .util import *
import os
import torch
from diffusers import StableDiffusionPipeline

def initialize():
  command_ls = "nvidia-smi| pip install git+https://github.com/huggingface/huggingface_hub.git | pip install diffusers | pip install transformers | pip install scipy | pip install ftfy | pip install accelerate"
  os.system(command_ls)

def login(token):
  """Login to HuggingFace using your token
  Args:
      token (:obj:`str`, required): Huggingface token, you can get one at https://huggingface.co/settings/tokens
  """
  from huggingface_hub.hf_api import HfFolder
  HfFolder.save_token(token)
  return "Your token has been saved to /root/.huggingface/token"

def pipegen(model="stabilityai/stable-diffusion-2"):
  """
  Set up the pipeline to get ready for generating images. 
  Args:
      model (:obj:`str`, optional): Pre-trained stable diffusion model from StabilityAI: https://huggingface.co/stabilityai
  """
  pipe = StableDiffusionPipeline.from_pretrained(model, revision="fp16", torch_dtype=torch.float16)  
  pipe = pipe.to("cuda")
  return pipe

def image_gen(image_description, pipe, height=600, width=800):
  """Prompt to generate images from text description. See the prompt guide at: https://prompthero.com/stable-diffusion-prompt-guide
  Args:
      image_description (:obj:`str`, required): Text description for your target image
      pipe (:obj:`str`, required): the output of the `pipegen()` function
      height (:obj:`str`, optional): Target image height
      width (:obj:`str`, optional): Target image width
  """
  prompt = image_description
  image = pipe(prompt, height=height, width=width).images[0]
  return image