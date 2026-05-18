# Orbity

## Description

Orbity is a program that performs theoretical numerical calculations, using formulas and concepts from classical thermodynamics and mechanics as a basis. In the context of experimental academic rocket launches, more is said about modeling and describing the rocket's trajectory, but something very important is left aside: the functioning of the launch pad.

At first glance, it seems like something to go unnoticed, however, within the base there are also physical phenomena, related mainly to thermodynamics: air expansion, pressure, efficiency. The rocket can be perfectly built, however, if the base delivers an unbalanced launch angle and very low efficiency, the rocket will not have its maximum result and will not reach its best speed and range.

That's what Orbity was created for! It will basically show you, through data, how the rocket and base must behave to achieve their best result. However, it is worth noting that Orbity disregards factors such as: climate and air resistance.

![Imagem1](./imgs/orbitygif.gif)

## Installation

### Requirements

- **Git**: To clone repositore. -> [Git Site](https://git-scm.com)
- **Python**: Version 3.8 or higher. ->  [Python Site](https://www.python.org/downloads/)

- Important! On Windows, During Python installation check the "Add Python to PATH" option!

### 🪟 Windows

1. Open the command prompt.

2. Inside the command prompt (cmd), type:

```bash
#Go to the documents folder.
cd Documents

#Clone the repository
git clone https://github.com/rwvthrdev/Orbity.git
```

3. Go to the project folder:

```bash
cd orbity
```

4. Create a virtual environment:

```bash
python -m venv .venv
```

5. Activate the virtual environment:

```bash
.venv\Scripts\activate
```