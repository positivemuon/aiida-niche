# -*- coding: utf-8 -*-

"""
Defines a workchain to insert impurities to a structure.
"""

from aiida import orm
from aiida.engine import WorkChain, calcfunction
from aiida.common.utils import get_object_from_string
from aiida_tools import check_workchain_step


class GenerateStructures(WorkChain):
    """
    Workchain to create structures containing impurities from a given input structure.
    """

    @classmethod
    def define(cls, spec):
        super(GenerateStructures, cls).define(spec)

        spec.input("structure", valid_type=orm.StructureData)
        spec.input("niche_atom", valid_type=orm.Str)
        spec.input("niche_spacing", valid_type=orm.Float)
        spec.input("niche_distance", valid_type=orm.Float)

        spec.outputs.dynamic = True
        spec.outline(cls.generate_structures)

    @check_workchain_step
    def generate_structures(self):  # pylint: disable=missing-docstring

        new_structure_data = _add_impurities(
            structure=self.inputs.structure,
            niche_atom=self.inputs.niche_atom,
            niche_spacing=self.inputs.niche_spacing,
            niche_distance=self.inputs.niche_distance,
        )

        self.out("Impurities", new_structure_data)


@calcfunction
def _add_impurities(
    structure: orm.StructureData,
    niche_atom: orm.Str,
    niche_spacing: orm.Float,
    niche_distance: orm.Float,
) -> orm.StructureData:
    """
    Applies impurities to the given structure, and returns a list of structures.
    """

    niche_class = get_object_from_string("niche.Niche")

    pmg_structure = structure.get_pymatgen_structure()
    niche_instance = niche_class(pmg_structure, niche_atom.value)

    new_pmg_structure = niche_instance.apply(niche_spacing.value, niche_distance.value)
    new_structure_data = orm.StructureData()
    new_structure_data.set_pymatgen(new_pmg_structure)

    return new_structure_data
