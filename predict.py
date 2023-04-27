import numpy as np
import tensorflow as tf
from download_tora_with_teamim import get_data
from split_teamim import split_teamim

tora_with_teamim = get_data()
print(len(tora_with_teamim))

[words, teamim] = split_teamim(tora_with_teamim[0])
print(words)
print(teamim)
