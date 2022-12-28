# https://stackoverflow.com/questions/53221775/sox-not-reading-wav

from pydub import AudioSegment
from pydub.playback import play
sound = AudioSegment.from_wav('AlienPart1.mp4')
play(sound)

#filename = 'AlienPart1.mp4'
#filename = 'outtaher.wav'