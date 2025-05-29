import sys
import time

sys.path.append('./Checkpoints')
sys.path.append('./Traps')
sys.path.append('./Core')
sys.path.append('./Ground')
sys.path.append('./Object')
sys.path.append('./Levels')
sys.path.append('./Utils')




from Objects import Object

from Traps.Bullet import Bullet
from Traps.Dar import Dar
from Traps.Bee import Bee
from Player import Player
from Traps.Plant import Plant
from Ground.Block import Block
from Traps.Fire import Fire
from Ground.Particules import Particules
from Object.Fan import Fan
from Object.PlatformsBrown import PlatformsBrown
from Traps.SpikeHead import SpikeHead
from Object.PlatformsGrey import PlatformsGrey
from Object.Trampoline import Trampoline
from Checkpoints.Checkpoint import Checkpoint
from Checkpoints.Start import Start
from Checkpoints.End import End
from Traps.Spikes import Spikes
from Traps.FallingPlatform import FallingPlatform
from Traps.SpikedBall import SpikedBall
from Traps.Saw import Saw
from Ground.Button import Button
from Ground.Text import Text
from Object.Fruits import Fruit
from Object.Cube import Cube