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
        '-isystem','/home/luca/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clang/lib/clang/10.0.0/include',
        '-isystem','/home/luca/workdir/compilers/openmpi/openmpi-install/include', # for mpi.h
        '-isystem','/home/luca/.vim',
        '-isystem','/home/luca/workdir/compilers/gcc/gcc-install/lib/gcc/x86_64-pc-linux-gnu/9.3.1/include', # for omp.h
        '-isystem','/home/luca/workdir/libs/boost/boost-install/include',
]

E3SM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/share/',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/utilities',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/vector',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/theta-l_kokkos/cxx',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/src/preqx_kokkos/cxx',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/components/homme/test/unit_tests/catch2/include',
        '-I/home/luca/workdir/e3sm/e3sm-build/gcc/opt/branch/',
        '-I/home/luca/workdir/e3sm/e3sm-src/branch/cime/src/share/timing',
        '-DPLEV=72',
        '-DNP=4',
        '-DQSIZE_D=4',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/OpenMP',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/impl',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/HIP',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/Cuda',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/core/src/Threads',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/algorithms/src/',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-src/master/externals/kokkos/containers/src/',
        '-isystem', '/home/luca/workdir/e3sm/e3sm-build/homme/gcc/debug/branch-pack-8/kokkos/build/',
]

SCREAM_EKAT_FLAGS = [
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/ekat-branch/',
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/ekat-branch/tests',
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/branch-dp/externals/ekat/src',
        '-I/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/catch2/include/',
        '-I/home/luca/workdir/scream/scream-src/branch/externals/ekat/src/',
        '-isystem','/home/luca/workdir/scream/scream-build/gcc/debug/branch-dp/externals/kokkos/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/impl',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/OpenMP',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/core/src/Serial',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/algorithms/src',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/ekat/extern/kokkos/containers/src/',
]

EKAT_FLAGS = [
        '-DEKAT_TEST_DOUBLE_PRECISION',
        '-I/home/luca/workdir/libs/ekat/ekat-build/gcc/debug/branch/src',
        '-I/home/luca/workdir/libs/ekat/ekat-build/gcc/debug/branch/tests',
        '-I/home/luca/workdir/libs/ekat/ekat-src/branch/src/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/catch2/include/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-build/gcc/debug/branch/externals/kokkos',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/algorithms/src',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/containers/src',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Cuda/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/OpenMP/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Serial/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/yaml-cpp/src/',
        '-isystem','/home/luca/workdir/libs/ekat/ekat-src/branch/extern/yaml-cpp/src/contrib',
]

SCREAM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-DHOMMEXX_CONFIG_IS_CMAKE',
        '-DSCREAM_CONFIG_IS_CMAKE',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/control/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/share/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/share/field',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/physics/p3/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/physics/rrtmgp/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/src/physics/shoc/',
        '-I/home/luca/workdir/scream/scream-src/branch/components/scream/extern/catch2/include',
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/branch-dp/src',
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/branch-dp/src/dynamics/homme/homme/src/share/cxx',
        '-I/home/luca/workdir/scream/scream-build/gcc/debug/branch-dp/tests/scream_homme',
        '-I/home/luca/workdir/scream/scream-src/branch/components/homme/src/share/cxx',
        '-I/home/luca/workdir/scream/scream-src/branch/components/homme/src/share/cxx/mpi',
        '-I/home/luca/workdir/scream/scream-src/branch/components/homme/src/share/cxx/utilities',
        '-I/home/luca/workdir/scream/scream-src/branch/components/homme/src/share/cxx/vector',
        '-I/home/luca/workdir/scream/scream-src/branch/components/homme/src/theta-l_kokkos/cxx',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp/kernels/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rte/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/rte/kernels',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/components/eam/src/physics/rrtmgp/external/cpp/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/scorpio/src/clib/',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/scorpio/src/gptl',
        '-isystem','/home/luca/workdir/scream/scream-src/branch/externals/YAKL',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/home/luca/workdir/hommexx/hommexx-src/components/homme/src/',
        '-I/home/luca/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/',
        '-I/home/luca/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/mpi',
        '-I/home/luca/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/vector',
        '-I/home/luca/workdir/hommexx/hommexx-src/components/homme/test/unit_tests/',
        '-I/home/luca/workdir/hommexx/hommexx-build-debug/src/',
        '-I/home/luca/workdir/hommexx/hommexx-build-debug/test_execs/preqx_flat_ut/',
        '-I/home/luca/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat/',
        '-I/home/luca/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat_c/',
]

KOKKOS_FLAGS = [
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src',
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src/Cuda',
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src/OpenMP',
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src/Qthread',
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src/Threads',
        '-I/home/luca/workdir/kokkos/kokkos-src/core/src/impl',
        '-I/home/luca/workdir/kokkos/kokkos-src/containers/src',
        '-I/home/luca/workdir/kokkos/kokkos-src/containers/src/impl',
        '-I/home/luca/workdir/kokkos/kokkos-src/algorithms/src',
]

IBECS_FLAGS = [
        '-I/home/luca/workdir/ibecs/ibecs-src/src/',
        '-I/home/luca/workdir/ibecs/ibecs-build-debug/src',
]

ALBANY_FLAGS = [
        '-I/home/luca/workdir/albany/albany-src/branch/src',
        '-I/home/luca/workdir/albany/albany-src/branch/src/adapt',
        '-I/home/luca/workdir/albany/albany-src/branch/src/disc',
        '-I/home/luca/workdir/albany/albany-src/branch/src/disc/stk',
        '-I/home/luca/workdir/albany/albany-src/branch/src/disc/stk/percept',
        '-I/home/luca/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance',
        '-I/home/luca/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance_utils',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/bc',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/gather',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/interpolation',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/pde',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/response',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/scatter',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/state',
        '-I/home/luca/workdir/albany/albany-src/branch/src/evaluators/utility',
        '-I/home/luca/workdir/albany/albany-src/branch/src/problems',
        '-I/home/luca/workdir/albany/albany-src/branch/src/responses',
        '-I/home/luca/workdir/albany/albany-src/branch/src/utility',
        '-I/home/luca/workdir/albany/albany-src/branch/src/utility/math',
        '-I/home/luca/workdir/albany/albany-src/branch/src/adapt',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce/evaluators',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce/evaluators/hydrology',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce/problems',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce/interface_with_cism',
        '-I/home/luca/workdir/albany/albany-src/branch/src/LandIce/interface_with_mpas',
        '-I/home/luca/workdir/albany/albany-src/branch/src/responses',
        '-I/home/luca/workdir/albany/albany-src/branch/src/utility',
        '-I/home/luca/workdir/albany/albany-build/gcc/opt/branch/src',
]

TRILINOS_FLAGS = [
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/aztecoo/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/belos/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/epetra/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/epetraext/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/inout',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/model_evaluator',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/epetraext/src/transform',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ifpack2/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Cell',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Discretization',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Kokkos',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Orientation',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/intrepid2/core/src/luca',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/kokkos/core/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/kokkos/containers/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/kokkos/algorithms/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Coarsen',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Comm',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/FEGrid',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Include',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Krylov',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/LevelWrap',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/MLAPI',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Main',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/MatrixFree',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Operator',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/RefMaxwell',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Smoother',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/ml/src/Utils',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Graph',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Headers',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Interface',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Misc',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/MueCentral',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Rebalancing',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Smoothers',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Transfers',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/muelu/src/Utils',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-epetra',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-lapack',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-loca/src-mf',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-belos',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-petsc',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-thyra',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-epetra',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/nox/src-lapack',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/phalanx/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/piro/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rythmos/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/algorithm',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/elementwise',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/function',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/sol',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/status',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/step',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/utils',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/vector',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/rol/src/zoo',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/Fad',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFad',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFadET',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/Fad/utils',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/src/',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/src/mpl',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/src/parameter',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/sacado/src/template',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/stk/stk_io/stk_io',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/base',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/baseImpl',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/stk/stk_topology/stk_topology',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/stk/stk_util/stk_util',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/teuchos/core/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/teuchos/comm/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/teuchos/parameterlist/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/teuchos/numerics/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/teuchos/kokkoscompat/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/client_support',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_solve/client_support',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetra/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/transformer',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/thyra/adapters/tpetra/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/src',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/inout',
        '-I/home/luca/workdir/trilinos/trilinos-src/develop/packages/tpetra/core/ext',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos2/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/anasazi/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/aztecoo/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/belos/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetra/src/'
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetraext/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack2/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid2/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos-kernels/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ml/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/muelu/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/minitensor/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/nox/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/piro/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/core/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/dof-mgr/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/phalanx/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rol/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rtop/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/sacado/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/exodus/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/ioss/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/shards/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stratimikos/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stk/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teko/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/thyra/core/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tempus/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/core/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/tsqr/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teuchos/core/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/xpetra/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan/src/',
        '-I/home/luca/workdir/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan2/src/',
]

TRILINOS_INCLUDE_FLAGS = [
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/Cuda',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/generated_specializations_hpp',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/gtest',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/impl',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/OpenMP',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/Qthreads',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_expreval',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_io',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_math',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_mesh',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_ngp',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_search',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_simd',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_simd_view',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_tools',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_topology',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_transfer',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_unit_test_utils',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/stk_utils',
        '-isystem', '/home/luca/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop-serial/include/Threads',
        '-isystem', '/home/luca/workdir/libs/netcdf/netcdf-c/netcdf-c-install/include/',
        '-isystem', '/home/luca/workdir/libs/netcdf/pnetcdf/pnetcdf-install/include/',
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
    is_ekat = in_directory(filename,'/home/luca/workdir/libs/ekat/ekat-src')
    if is_ekat :
      final_flags = final_flags + EKAT_FLAGS
    is_scream = in_directory(filename,'/home/luca/workdir/scream/scream-src')
    if is_scream :
      final_flags = final_flags + SCREAM_FLAGS + SCREAM_EKAT_FLAGS
    is_e3sm = in_directory(filename,'/home/luca/workdir/e3sm/e3sm-src')
    if is_e3sm :
      final_flags = final_flags + E3SM_FLAGS
    is_kokkos = in_directory(filename,'/home/luca/workdir/kokkos/kokkos-src')
    if is_kokkos :
      final_flags = final_flags + KOKKOS_FLAGS
    is_albany = in_directory(filename,'/home/luca/workdir/albany/albany-src')
    if is_albany:
      final_flags = final_flags + ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_ibecs = in_directory(filename,'/home/luca/workdir/ibecs/ibecs-src')
    if is_ibecs :
      final_flags = final_flags + IBECS_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_trilinos = in_directory(filename,'/home/luca/workdir/trilinos/trilinos-src')
    if is_trilinos :
      final_flags = final_flags + TRILINOS_FLAGS

    final_flags = final_flags + BASE_FLAGS;

    return {
      'flags'    : final_flags,
    }
