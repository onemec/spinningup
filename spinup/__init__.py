# Disable TF deprecation warnings.
# Syntax from tf1 is not expected to be compatible with tf2.
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Algorithms
from spinup.algos.pytorch.ddpg.ddpg import ddpg as ddpg_pytorch
from spinup.algos.pytorch.ppo.ppo import ppo as ppo_pytorch
from spinup.algos.pytorch.sac.sac import sac as sac_pytorch
from spinup.algos.pytorch.td3.td3 import td3 as td3_pytorch
from spinup.algos.pytorch.trpo.trpo import trpo as trpo_pytorch
from spinup.algos.pytorch.vpg.vpg import vpg as vpg_pytorch
from spinup.algos.tf1.ddpg.ddpg import ddpg as ddpg_tf1
from spinup.algos.tf1.ppo.ppo import ppo as ppo_tf1
from spinup.algos.tf1.sac.sac import sac as sac_tf1
from spinup.algos.tf1.td3.td3 import td3 as td3_tf1
from spinup.algos.tf1.trpo.trpo import trpo as trpo_tf1
from spinup.algos.tf1.vpg.vpg import vpg as vpg_tf1

# Loggers
from spinup.utils.logx import EpochLogger, Logger

# Version
from spinup.version import __version__

__version__ = __version__
__all__ = [
    "ddpg_tf1",
    "ppo_tf1",
    "sac_tf1",
    "td3_tf1",
    "trpo_tf1",
    "vpg_tf1",
    "ddpg_pytorch",
    "ppo_pytorch",
    "sac_pytorch",
    "td3_pytorch",
    "trpo_pytorch",
    "vpg_pytorch",
    "Logger",
    "EpochLogger",
]
