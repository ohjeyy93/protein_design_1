from pyrosetta_help import Blueprinter
# Import necessary modules
from pyrosetta import *
from pyrosetta.rosetta import *

# Initialize PyRosetta
init()
pose = pose_from_pdb("7t3d_new_design_version_fixed1.pdb")
blue = Blueprinter.from_pose(pose)
blue.wobble_span(47,113)
#blue[20:22] = 'PIKAA G' # change residues 20, 21 and 22 (inclusive) to Glycine
#blue.wobble_span(20,25) # remodel keeping original amino acid
#del blue[15:20] # requires preceeding and suceeding residues to be 'wobbled' though.
#blue.del_span(15, 20) # same as above, but wobbles the preceeding and suceeding 1 residues
#blue[22] = 'PIKAA W'
#blue.pick_native(21)
#blue.pick_native(23)
#blue.mutate(22, 'W') # same as above, but wobbling adjecent residues.
#blue.expand_loop_wobble()
blue.set('mutant.blu')
rm = blue.get_remodelmover(dr_cycles=5, max_linear_chainbreak=0.1)
rm.apply(pose)
blue.show_aligned(pose)   # jupyter notebook (requires Biopython)
# if all goes wrong there is `blue.correct_and_relax(pose)`

rm = pyrosetta.rosetta.protocols.forge.remodel.RemodelMover()
# ...
rm.register_options()
rm.apply(pose)

#pyrosetta.rosetta.basic.options.set_boolean_option('remodel:design:find_neighbors', value)
#pyrosetta.rosetta.basic.options.set_file_option('remodel:blueprint', filename)
#pyrosetta.rosetta.basic.options.set_string_option('remodel:generic_aa', value)

#rm = pyrosetta.rosetta.protocols.forge.remodel.RemodelMover()
#pyrosetta.rosetta.basic.options.set_file_option('remodel:blueprint', filename)
#rm.register_options()

blue = Blueprinter.from_pose(pose)
blue.blueprint = 'mutant.blu'
blue.find_neighbors = True
blue.quick_and_dirty = True

#pdb_mover = pyrosetta.rosetta.protocols.simple_moves.AddPDBInfoMover()
#pdb_mover.apply(pose)

#with open('mut.blu', 'w') as w:
#    w.write(blue.to_pdb_str(pose))
#blue.blueprint = 'mut.blu'

#mutant = original_pose.clone()
#pdb_mover = pyrosetta.rosetta.protocols.simple_moves.AddPDBInfoMover()
#pdb_mover.apply(mutant)
#remodel_mover = blue.get_remodelmover()
#remodel_mover.apply(mutant)
#blue.copy_pdb_info(original_pose, mutant)
pose.dump_pdb("blue_loop_modeler_1.pdb")