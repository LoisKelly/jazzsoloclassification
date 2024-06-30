from timidity import Parser, play_notes
from scipy.signal import square, sawtooth
import numpy as np
from scipy.io import wavfile

ps = Parser("bach_850.mid")

audio, player = play_notes(*ps.parse(), np.sin, wait_done=False)

wavfile.write("example_output.wav", 44100, audio)

player.wait_done()
