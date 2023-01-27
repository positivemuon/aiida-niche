#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-

# © 2023-2023 University of Parma
# Author: Pietro Bonfà
"""
Example add H impurities to InSb
"""

from pymatgen.core import Structure

from aiida.orm.nodes.data.str import Str
from aiida.orm.nodes.data.float import Float
from aiida.orm.nodes.data.list import List
from aiida.orm import StructureData
from aiida.engine.launch import run

from aiida_niche import GenerateStructures


def get_niche_input(  # pylint: disable=missing-docstring
    niche_atom='H',
):
    structure = StructureData()
    structure.set_pymatgen(Structure.from_file('POSCAR'))

    return dict(
        structure=structure,
        niche_atom=Str(niche_atom),
        niche_density=Float(1.0)
    )


if __name__ == '__main__':
    print(run(GenerateStructures, **get_niche_input()))
