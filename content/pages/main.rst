Adaptable Poly-Engineering Simulator (APES)
###########################################

:save_as: index.html
:url:
:hide_navbar_brand: True

APES is a suite of mesh based simulation tools built around an octree mesh
infrastructure.
It provides various steps required for the simulation on large scale
parallel computing facilities from the mesh generation to post-processing.

.. image:: {static}/images/apes_schematic.svg

The applications are MPI parallel and scale well to many thousands of
processes. There are currently two solvers developed in the suite and available
under permissive open-source licenses:

* `Ateles`_ is a high-order Discontinuous Galerkin solver that employs
  Legendre polynomials in cubical elements as basis functions.
* `Musubi`_ is a multi-level Lattice-Boltzmann solver that implements
  efficient kernels and the possibility to simulate multiple species with the
  Maxwell-Stefan model.

The mesh generator `Seeder`_ produces octree meshes and reads STL data to
describe geometries. The resulting mesh data is simple and designed for
efficient parallel reading on distributed memory systems.
The core library implementing the handling of these octree meshes is
implemented in `TreElM`_.

The solvers write their data in a native format on disk with MPI-IO, and
come with dedicated tools to post-process this data further into VTK files.
All tools are using Lua scripts as user interfaces, which enables a great
flexibility in the definition of simulation setups.
This functionality is provided by `Aotus`_.

Apes, or more generally `simians`_ [extern] are:

* adapting to given tasks
* living in trees
* relatively independent
* working in teams
* smart

.. _Ateles: {filename}/pages/ateles.rst
.. _Musubi: {filename}/pages/musubi.rst
.. _Seeder: {filename}/pages/seeder.rst
.. _TreElM: {filename}/pages/treelm.rst
.. _Aotus: {filename}/pages/aotus.rst
.. _simians: https://en.wikipedia.org/wiki/Simian
