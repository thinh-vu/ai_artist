# I. INTRODUCTION
`ai_artist` made generating images easy using the Stable Diffusion AI model.

<div id="badges" align="center">
<img src="https://img.shields.io/pypi/pyversions/ai_artist?logoColor=brown&style=plastic" alt= "Version"/>
<img src="https://img.shields.io/pypi/dm/ai_artist" alt="Download Badge"/>
<img src="https://img.shields.io/github/last-commit/thinh-vu/ai_artist" alt="Commit Badge"/>
<img src="https://img.shields.io/github/license/thinh-vu/ai_artist?color=red" alt="License Badge"/>
</div>

# II. HOW TO USE THIS PROJECT

## 2.1. Install this package

- Using pip to install the pre-built package on Pypip `pip install ai_artist`
- If you want to use the latest **ai_artist** version instead of the stable one, you can install it from the source with the following command:
`pip install git+https://github.com/thinh-vu/ai_artist.git@main`

_(*) You might need to insert a `!` before your command when running terminal commands on Google Colab._

## 2.2. Set up your project

1. Import the whole package to your project: `from ai_artist import *`
2. Install dependencies: `!pip install transformers`
3. Set up the environment: `initialize()`
4. Save Huggingface login info to use the pre-trained model: `login('YOUR_HUGGINGFACE_KEY')`
5. Set up the pipeline: `pipe = pipegen()`

## 2.3. Start generating images
6. Provide your image description to the prompt: `image_gen("YOUR_IMAGE_DESCRIPTION", pipe)`

# III. RERERENCES
## 3.1. Get HuggingFace API key

**Generate a token key** with **read** permission. Read the doc [here](https://huggingface.co/docs/hub/security-tokens)

**About Huggingface**

> [Huggingface](https://huggingface.co/about) is a community and data science platform that provides:
> - Tools that enable users to build, train and deploy ML models based on open source (OS) code and technologies.
> - A place where a broad community of data scientists, researchers, and ML engineers can come together and share ideas, get support and contribute to open source projects.

## 3.2. Google Colab and GPU runtime are highly recommended
Go to the Google Colab menu: Select `Runtime` > `Change runtime type` and make sure that `GPU` has been chosen. You can run this AI model way faster with GPU on Google Colab than the normal CPU or your personal computer.

![gpu_setting](https://raw.githubusercontent.com/thinh-vu/ur_audio_sub/main/src/Google%20Colab%20runtime%20GPU.png)

### Stable Diffusion & StabilityAI
- Stable Diffusion on Github: [here](https://github.com/CompVis/stable-diffusion)

- Stable Diffusion prompt guide and examples [here](https://strikingloo.github.io/stable-diffusion-vs-dalle-2)

# IV. 🙋‍♂️ CONTACT INFORMATION

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/thinh-vu">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.messenger.com/t/mr.thinh.ueh">
    <img src="https://img.shields.io/badge/Messenger-00B2FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Badge"/>
  <a href="https://www.youtube.com/channel/UCYgG-bmk92OhYsP20TS0MbQ">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  </a>
    <a href="https://github.com/thinh-vu">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github Badge"/>
  </a>
</div>

---

If you want to support my open-source projects, you can "buy me a coffee" via [Patreon](https://patreon.com/thinhvu?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator) or Momo e-wallet (VN). Your support will help to maintain my blog hosting fee & to develop high-quality content.

<details>
<summary> Momo QR </summary>

![momo-qr](https://github.com/thinh-vu/vnstock/blob/main/src/momo-qr-thinhvu.jpeg?raw=true)

</details>
