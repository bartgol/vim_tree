import os
import ycm_core

BASE_FLAGS = [
        '-x',
        'c++',
        '-Wall',
        '-Wextra',
        '-Wshadow',
        '--pedantic',
        '-fopenmp',
        '-ferror-limit=10000',
        '-std=c++14',
        '-isystem','/ascldap/users/lbertag/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clang/lib/clang/13.0.0/include',
        '-isystem','/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include', # for mpi.h
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/9.2.0/base/include', # for omp.h
]

E3SM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/share/',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/utilities',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/vector',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/theta-l_kokkos/cxx',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/src/preqx_kokkos/cxx',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/components/homme/test/unit_tests/catch2/include',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-build/gcc/opt/branch/',
        '-I/ascldap/users/lbertag/workdir/e3sm/e3sm-src/branch/cime/src/share/timing',
        '-DPLEV=72',
        '-DNP=4',
        '-DQSIZE_D=4',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/OpenMP',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/impl',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/HIP',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/Cuda',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/Threads',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/algorithms/src/',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-src/master/externals/kokkos/containers/src/',
        '-isystem', '/ascldap/users/lbertag/workdir/e3sm/e3sm-build/homme/gcc/debug/branch-pack-8/kokkos/build/',
]

SCREAM_EKAT_FLAGS = [
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/ekat-branch/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/ekat-branch/tests',
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/branch-dp/externals/ekat/src',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/catch2/include/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/src/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/branch-dp/externals/kokkos/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/impl',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/OpenMP',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/Serial',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/algorithms/src',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/containers/src/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/ekat/extern/spdlog/include/',
]

EKAT_FLAGS = [
        '-DEKAT_TEST_DOUBLE_PRECISION',
        '-I/ascldap/users/lbertag/workdir/libs/ekat/ekat-build/gcc/debug/branch/src',
        '-I/ascldap/users/lbertag/workdir/libs/ekat/ekat-build/gcc/debug/branch/tests',
        '-I/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/src/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/catch2/include/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-build/gcc/debug/branch/externals/kokkos',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/algorithms/src',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/containers/src',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Cuda/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/OpenMP/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Serial/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/yaml-cpp/src/',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/yaml-cpp/src/contrib',
        '-isystem','/ascldap/users/lbertag/workdir/libs/ekat/ekat-src/branch/extern/spdlog/include',
]

SCREAM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-DHOMMEXX_CONFIG_IS_CMAKE',
        '-DSCREAM_CONFIG_IS_CMAKE',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/control/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/share/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/share/field',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/share/util/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/physics/p3/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/physics/rrtmgp/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/src/physics/shoc/',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/scream/extern/catch2/include',
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/branch-dp/src',
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/branch-dp/src/dynamics/homme/homme/src/share/cxx',
        '-I/ascldap/users/lbertag/workdir/scream/scream-build/gcc/debug/branch-dp/tests/scream_homme',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/homme/src/share/cxx',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/homme/src/share/cxx/mpi',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/homme/src/share/cxx/utilities',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/homme/src/share/cxx/vector',
        '-I/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/homme/src/theta-l_kokkos/cxx',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp/kernels/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rte/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rte/kernels',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/scorpio/src/clib/',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/scorpio/src/gptl',
        '-isystem','/ascldap/users/lbertag/workdir/scream/scream-src/branch/externals/YAKL',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-src/components/homme/src/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/mpi',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/vector',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-src/components/homme/test/unit_tests/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-build-debug/src/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-build-debug/test_execs/preqx_flat_ut/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat/',
        '-I/ascldap/users/lbertag/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat_c/',
]

KOKKOS_FLAGS = [
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src/Cuda',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src/OpenMP',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src/Qthread',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src/Threads',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/core/src/impl',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/containers/src',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/containers/src/impl',
        '-I/ascldap/users/lbertag/workdir/kokkos/kokkos-src/algorithms/src',
]

IBECS_FLAGS = [
        '-I/ascldap/users/lbertag/workdir/ibecs/ibecs-src/src/',
        '-I/ascldap/users/lbertag/workdir/ibecs/ibecs-build-debug/src',
]

ALBANY_FLAGS = [
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/adapt',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/disc',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/disc/stk',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/disc/stk/percept',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance_utils',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/bc',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/gather',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/interpolation',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/pde',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/response',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/scatter',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/state',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/evaluators/utility',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/problems',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/responses',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/utility',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/utility/math',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/adapt',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce/evaluators',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce/evaluators/hydrology',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce/problems',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce/interface_with_cism',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/LandIce/interface_with_mpas',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/responses',
        '-I/ascldap/users/lbertag/workdir/albany/albany-src/branch/src/utility',
        '-I/ascldap/users/lbertag/workdir/albany/albany-build/gcc/opt/branch/src',
]

TRILINOS_FLAGS = [
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/aztecoo/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/belos/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/epetra/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/epetraext/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/inout',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/model_evaluator',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/transform',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ifpack2/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Cell',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Discretization',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Kokkos',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Orientation',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/luca',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/kokkos/core/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/kokkos/containers/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/kokkos/algorithms/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Coarsen',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Comm',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/FEGrid',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Include',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Krylov',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/LevelWrap',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/MLAPI',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Main',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/MatrixFree',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Operator',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/RefMaxwell',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Smoother',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/ml/src/Utils',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Graph',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Headers',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Interface',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Misc',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/MueCentral',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Rebalancing',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Smoothers',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Transfers',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Utils',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-epetra',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-lapack',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-mf',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-belos',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-petsc',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-thyra',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-epetra',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/nox/src-lapack',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/phalanx/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/piro/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rythmos/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/algorithm',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/elementwise',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/function',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/sol',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/status',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/step',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/utils',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/vector',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/rol/src/zoo',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/Fad',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFad',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFadET',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/utils',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/src/mpl',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/src/parameter',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/sacado/src/template',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/stk/stk_io/stk_io',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/base',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/baseImpl',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/stk/stk_topology/stk_topology',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/stk/stk_util/stk_util',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/teuchos/core/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/teuchos/comm/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/teuchos/parameterlist/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/teuchos/numerics/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/teuchos/kokkoscompat/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/client_support',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_solve/client_support',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetra/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/transformer',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/tpetra/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/src',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/inout',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/ext',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos2/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/anasazi/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/aztecoo/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/belos/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetra/src/'
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetraext/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack2/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid2/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos-kernels/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ml/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/muelu/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/minitensor/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/nox/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/piro/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/core/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/dof-mgr/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/phalanx/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rol/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rtop/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/sacado/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/exodus/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/ioss/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/shards/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stratimikos/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stk/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teko/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/thyra/core/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tempus/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/core/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/tsqr/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teuchos/core/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/xpetra/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan/src/',
        '-I/ascldap/users/lbertag/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan2/src/',
]

TRILINOS_INCLUDE_FLAGS = [
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/Cuda',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/generated_specializations_hpp',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/gtest',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/impl',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/OpenMP',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/Qthreads',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_expreval',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_io',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_math',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_mesh',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_ngp',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_search',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_simd',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_simd_view',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_tools',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_topology',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_transfer',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_unit_test_utils',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/stk_utils',
        '-isystem', '/ascldap/users/lbertag/workdir/trilinos/trilinos-install/mappy/gcc/debug/develop-serial/include/Threads',
        '-isystem', '/ascldap/users/lbertag/workdir/libs/netcdf/netcdf-c/netcdf-c-install/include/',
        '-isystem', '/ascldap/users/lbertag/workdir/libs/netcdf/pnetcdf/pnetcdf-install/include/',
]

def in_directory(file, directory, allow_symlink = False):
    #make both absolute
    directory = os.path.realpath(directory)
    file = os.path.realpath(file)

    #check whether file is a symbolic link, if yes, return false if they are not allowed
    if not allow_symlink and os.path.islink(file):
        return False

    #return true, if the common prefix of both is equal to directory
    #e.g. /a/b/c/d.rst and directory is /a/b, the common prefix is /a/b
    return os.path.commonprefix([file, directory]) == directory

def Settings(**kwargs):
    filename = kwargs[ 'filename' ]
    final_flags = []
    is_ekat = in_directory(filename,'/ascldap/users/lbertag/workdir/libs/ekat/ekat-src')
    if is_ekat :
      final_flags = final_flags + EKAT_FLAGS
    is_scream = in_directory(filename,'/ascldap/users/lbertag/workdir/scream/scream-src')
    if is_scream :
      final_flags = final_flags + SCREAM_FLAGS + SCREAM_EKAT_FLAGS
    is_e3sm = in_directory(filename,'/ascldap/users/lbertag/workdir/e3sm/e3sm-src')
    if is_e3sm :
      final_flags = final_flags + E3SM_FLAGS
    is_kokkos = in_directory(filename,'/ascldap/users/lbertag/workdir/kokkos/kokkos-src')
    if is_kokkos :
      final_flags = final_flags + KOKKOS_FLAGS
    is_albany = in_directory(filename,'/ascldap/users/lbertag/workdir/albany/albany-src')
    if is_albany:
      final_flags = final_flags + ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_ibecs = in_directory(filename,'/ascldap/users/lbertag/workdir/ibecs/ibecs-src')
    if is_ibecs :
      final_flags = final_flags + IBECS_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_trilinos = in_directory(filename,'/ascldap/users/lbertag/workdir/trilinos/trilinos-src')
    if is_trilinos :
      final_flags = final_flags + TRILINOS_FLAGS

    final_flags = final_flags + BASE_FLAGS;

    return {
      'flags'    : final_flags,
    }
