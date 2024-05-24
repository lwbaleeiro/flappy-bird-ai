# Flappy Bird - NEAT
## NEAT - NeuroEvolution of Augmenting Topologies

You can find more about NEAT in this paper [here](https://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf).

## How to Execute

Download and install [Graphviz](https://graphviz.org/download/)

```bash
    - choco install graphviz
```
- Then, you need to install the requirements found in the `requirements.txt` file:

  ```bash
    pip install -r requirements.txt

- **If you wants to play** single player, simply execute the `play_game.py` file in the project folder:

  ```bash
    cd your/folder/path/flappy-bird-ai
    python play_game.py

- **If you need to train the AI**, you need to execute the `train_ai.py` once you have the best player (`best.pickle` file) you are done with training.

  ```bash
    cd your/folder/path/flappy-bird-ai
    python train_ai.py