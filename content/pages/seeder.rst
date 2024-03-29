Seeder
######

.. image:: {static}/images/seeder_logo.svg
    :height: 100px

Seeder is the mesh generator of APES.
It generates octree meshes in the TreElM format that allows for an efficient
parallel reading.
Seeder can make use of geometry definitions in STL and enables local refinement,
either by user defined objects or in dependency on the distance to geometries.
Arbitrary boundary labels can be assigned to objects in the domain to allow the
solvers association of boundary conditions with those geometries.

High-order boundaries can be generated for Lattice Boltzmann (Q-Values) and for
penalization methods (subresolution).

Its public `source code repository`_ is hosted on OSDN.
Please see the `documentation`_ for its usage and more details.

.. _source code repository: https://osdn.net/projects/apes/scm/hg/seeder/
.. _documentation: https://geb.inf.tu-dresden.de/doxy/seeder/index.html

