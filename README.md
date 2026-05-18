# 🚀 Orbity

![Logo](./imgs/logo.png)

[![Version](https://img.shields.io/badge/version-1.0.0.1-blue.svg?style=for-the-badge)](https://github.com/rwvthrdev/orbity) [![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/rwvthrdev/orbity?style=for-the-badge&logo=github&color=yellow)](https://github.com/rwvthrdev/orbity/stargazers) [![GitHub issues](https://img.shields.io/github/issues/rwvthrdev/orbity?style=for-the-badge&logo=github&color=red)](https://github.com/rwvthrdev/orbity/issues) [![GitHub forks](https://img.shields.io/github/forks/rwvthrdev/orbity?style=for-the-badge&logo=github&color=blueviolet)](https://github.com/rwvthrdev/orbity/forks) 

## ⚙️ Description

Orbity is a program that performs theoretical numerical calculations, using formulas and concepts from classical thermodynamics and mechanics as a basis. In the context of experimental academic rocket launches, more is said about modeling and describing the rocket's trajectory, but something very important is left aside: the functioning of the launch pad.

At first glance, it seems like something to go unnoticed, however, within the base there are also physical phenomena, related mainly to thermodynamics: air expansion, pressure, efficiency. The rocket can be perfectly built, however, if the base delivers an unbalanced launch angle and very low efficiency, the rocket will not have its maximum result and will not reach its best speed and range.

That's what Orbity was created for! It will basically show you, through data, how the rocket and base must behave to achieve their best result. However, it is worth noting that Orbity disregards factors such as: climate and air resistance.

![Imagem1](./imgs/orbitygif.gif)

## ⬇️ Installation

### Requirements

- **Git**: To clone repositore. -> [Git Site](https://git-scm.com)
- **Python**: Version 3.8 or higher. ->  [Python Site](https://www.python.org/downloads/)

- Important! On Windows, During Python installation check the "Add Python to PATH" option!

## 🪟 Windows

1. Open the command prompt

2. Inside the command prompt (cmd), type

```bash

cd Documents

git clone https://github.com/rwvthrdev/Orbity.git
```

3. Go to the project folder

```bash
cd orbity
```

4. Create a virtual environment

```bash
python -m venv .venv
```

5. Activate the virtual environment

```bash
.venv\Scripts\activate
```

6. Install the dependencies

```bash
pip install -r requirements.txt
```

!If you encounter an error in NumPy and Matplotlib like I did, paste this command

```bash
pip install --only-binary :all: numpy
pip install --only-binary :all: matplotlib
```

7. Run the file

```bash
python orbity.py
```

## 🐧 Linux

1. Open bash

2. Inside the bash, type

```bash
cd ~/Documents

git clone https://github.com/rwvthrdev/Orbity.git
```

3. Go to the project folder

```bash
cd orbity
```

4. Create a virtual environment

```bash
python3 -m venv .venv
```

5. Activate

```bash
source .venv\bin\activate
```

6. Install the dependencies.

```bash
pip install -r requirements.txt
```

7. Run the project

```bash
python3 orbity.py
```

## Follow me

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/rwvthrdev) 


