#Python
from pyrosetta import *
from pyrosetta.rosetta import * ##to bring the function that are under rosetta but not in pyrosetta
from pyrosetta.teaching import *

#Core Includes
from rosetta.core.kinematics import MoveMap
from rosetta.core.kinematics import FoldTree
from rosetta.core.pack.task import TaskFactory
from rosetta.core.pack.task import operation
from rosetta.core.simple_metrics import metrics
from rosetta.core.select import residue_selector as selections
from rosetta.core import select
from rosetta.core.select.movemap import *

#Protocol Includes
from rosetta.protocols import minimization_packing as pack_min
from rosetta.protocols import relax as rel
from rosetta.protocols.antibody.residue_selector import CDRResidueSelector
from rosetta.protocols.antibody import *
from rosetta.protocols.loops import *
from rosetta.protocols.relax import FastRelax

init()


##cleaning the pdb
#from pyrosetta.toolbox import cleanATOM
#cleanATOM("xxxx.pdb")



##relax the structure
#from pyrosetta.rosetta.protocols.relax import FastRelax
##next six lines are common for all relax
relax = pyrosetta.rosetta.protocols.relax.FastRelax()
scorefxn = get_fa_scorefxn()
relax.set_scorefxn(scorefxn)
relax.constrain_relax_to_start_coords(True) ##setting constrains to bb so that the original structure remains
print(relax)

pose = pose_from_pdb('complex_alpha.pdb') ##creating the pose for the relax structure
#PoseRelax = Pose() ##creating class
#PoseRelax.assign(pose_relax) ##assigning the structure in the empty class
#print(PoseRelax)

score_before = scorefxn(pose) ##score before relax
relax.apply(pose)
pose.dump_pdb('complex_alpha_relaxed.pdb')
score_after = scorefxn(pose) ##score after relax
print("relaxed!")
print("////")
print(score_before)
print("////")
print(score_after)
print("////")
print("done!")
