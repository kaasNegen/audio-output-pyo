from __future__ import division
from pyo import *

server = Server(audio='portaudio', sr=44100, nchnls=2, duplex=0).boot()
server.start()

maximumDistance = 1000
sweepTime = 2

#index represents angle to some extent
observations = [
    200,
    200,
    200,
    200,
    200,
    500,
    500,
    500,
    500,
    500,
    200,
    200,
    200,
    200,
    200,
]

def determineFrequency(distance):
    return 100 + distance / maximumDistance * 500


lfo = LFO(
    freq=0
)

pan = Pan(
    lfo,
    spread=0
)

def visualizeObservation(idx, observation):
    lfo.setFreq(determineFrequency(observation))
    pan.setPan(idx / (len(observations) - 1))

    pan.out()
    time.sleep(sweepTime / len(observations))
    pan.stop()

while True:

    #TODO: Update observations to be up to date with current sensor readings

    for idx, observation in enumerate(observations):
        visualizeObservation(idx, observation)

