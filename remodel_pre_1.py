from __future__ import annotations
from dataclasses import dataclass
from typing import List

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


import pyrosetta

@dataclass
class GapData:
    chain: str
    start: int # PDB index of first missing residue
    previous: int # PDB index of the preceeding present residue
    pose_i: int # pose index of residue after the cutpoint (will become first was-missing)
    end: int # PDB index of last missing residue
    sequence: str = ''
        
    def fill_sequence(self, data: List[dict]) -> None:
        #print(data)
        #print(self.chain)
        for peptide in data:
        	#print(data)
            if self.chain in peptide['chains']:
                msg = f"Chain {self.chain} peptide ({len(peptide['sequence'])}) is shorter than the span ({self.start}:{self.end})"
                assert len(peptide['sequence']) >= self.start - 1, msg
                #print(len(peptide['sequence']))
                assert len(peptide['sequence']) >= self.end - 1, msg
                self.sequence = peptide['sequence'][self.start-1:self.end]
                assert self.sequence, 'Empty??!'
                return 
        else:
            raise ValueError(f'Unknown chain in pose {chain}')
            
    def get_pose(self) -> pyrosetta.Pose:
        # not used.
        pose = pyrosetta.pose_from_sequence(self.sequence)
        for i in range(1, pose.total_residue() + 1):
            pose.pdb_info().chain(i, self.chain)
            pose.pdb_info().number(i, i+self.start - 1)
        return pose
    
    def add_to_pose(self, pose: pyrosetta.Pose):
        # by extension
        chm = pyrosetta.rosetta.core.chemical.ChemicalManager.get_instance()
        rts = chm.residue_type_set( 'fa_standard' )
        #previous = self.pose_i - 1 #this may have changed!
        previous = pose.pdb_info().pdb2pose(res=self.previous, chain=self.chain)
        # self.pose_i is the pos of the one after the gap
        # it will become the new first added residue
        rm_upper = pyrosetta.rosetta.core.conformation.remove_upper_terminus_type_from_conformation_residue
        rm_lower = pyrosetta.rosetta.core.conformation.remove_lower_terminus_type_from_conformation_residue
        rm_upper(pose.conformation(), previous)
        rm_lower(pose.conformation(), previous)
        rm_lower(pose.conformation(), previous + 1)
        rm_upper(pose.conformation(), previous + 1)
        # LOWER_CONNECT N
        # UPPER_CONNECT C
        for i, r in enumerate(self.sequence):
            res_type = rts.get_representative_type_name1(r)
            residue = pyrosetta.rosetta.core.conformation.ResidueFactory.create_residue(res_type)
            pose.append_polymer_residue_after_seqpos(residue, previous + i, True)
            npos = previous + i + 1
            # pose.pdb_info().chain(npos, 'A')
            # pose.pdb_info().number(npos, self.previous + i + 1)
            rm_lower(pose.conformation(), npos)
            rm_upper(pose.conformation(), npos)
        # close loop
        lm = pyrosetta.rosetta.protocols.loop_modeler.LoopModeler()
        loops = pyrosetta.rosetta.protocols.loops.Loops()
        loop = pyrosetta.rosetta.protocols.loops.Loop(previous - 1,
                                                      npos + 2, 
                                                      npos) #cutpoint
        #loop.auto_choose_cutpoint(pose)
        loops.add_loop(loop)
        lm.set_loops(loops)
        # these are enabled by default. here for quick changing.
        lm.enable_centroid_stage()
        lm.enable_fullatom_stage()
        lm.enable_build_stage()
        lm.apply(pose)
        
    @classmethod
    def get_gaps(cls, pose: pyrosetta.Pose) -> List[GapData]:
        gaps = []
        pose2pdb = pose.pdb_info().pose2pdb
        previous_resi, previous_chain = (-1, '') # forbidden kanji is deffo not a chain name.
        for residue in pose.residues:
            resi, chain = map(lambda x: int(x) if x.isdigit() else x, pose2pdb(residue.seqpos()).split())
            if residue.is_ligand() or residue.is_metal(): # so why are ligands is_protein?
                previous_resi, previous_chain = (-1, '')
            elif chain != previous_chain:
                pass # reset!
            elif resi <= previous_resi:
                raise ValueError(f'PDB ordering error: {previous_resi, previous_chain, resi, chain}')
            elif resi != previous_resi + 1:
                gaps.append(cls(chain=chain, 
                                start= previous_resi + 1, 
                                end= resi - 1, 
                                pose_i = residue.seqpos(),
                                previous = previous_resi
                             ))
            else:
                pass # countinous.
            previous_resi, previous_chain = resi, chain
        return gaps
    
    @classmethod
    def fix_pose(cls, pose: pyrosetta.Pose, data: List[dict]) -> None:
        gaps = cls.get_gaps(pose)
        for gap in reversed(gaps):
            gap.fill_sequence(data)
            print(gap)
            gap_pose = gap.add_to_pose(pose)
            pose.dump_pdb('gap_filled_new_3-1.pdb')

init()

pose = pose_from_pdb('7t3d_new_design_version_fixed1.pdb')
from pyrosetta_help import Blueprinter
X=GapData('G', 47, 113, 114, 113, '')
X.fix_pose(pose, [{"chains":"G","sequence":'FIEGGWTGMVDGWYGYHHQNEQGSGYAADLKSTQNAIDTFEATGNLVVPRYAFAMERNVKNLYEKVRSQLKNNAKEIGNGCFEFYHKCDNTCMESVKNGTYDYPKYSEEAKLNRE'}])
#FIEGGWTGMVDGWYGYHHQNEQGSGYAADLKSTQNAIDTFEATGNLVVPRYAFAMERNAGSGIIISDTPVHDCNTTCQTPKGAINTSLPFQNIHPITIGKCPKYVKNVKNLYEKVRSQLKNNAKEIGNGCFEFYHKCDNTCMESVKNGTYDYPKYSEEAKLNRE
#chain: str
#start: int # PDB index of first missing residue
#previous: int # PDB index of the preceeding present residue
#pose_i: int # pose index of residue after the cutpoint (will become first was-missing)
#end: int # PDB index of last missing residue
#sequence: str = 'PIKAA'