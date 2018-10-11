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
        '-std=c++11',
        '-isystem','/home/shared/.vim/bundle/YouCompleteMe/third_party/ycmd/clang_includes/include',
        '-isystem','/home/shared/workdir/compilers/gcc/gcc-7.2.0-install/lib/gcc/x86_64-pc-linux-gnu/7.2.0/include/', # for omp.h
        '-isystem','/home/shared/workdir/compilers/openmpi/openmpi-3.0.0-install/include', # for mpi.h
        '-isystem','/home/shared/.vim',
]

E3SM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/utilities',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/vector',
        '-I/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/test/unit_tests/catch2/include',
        '-I/home/shared/workdir/e3sm/e3sm-build/gcc/opt/branch/',
        '-DPLEV=72',
        '-DNP=4',
        '-DQSIZE_D=4',
]

SCREAM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/control/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/share/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/physics/p3/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/physics/rrtmgp/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/src/physics/shoc/',
        '-I/home/shared/workdir/scream/scream-src/branch/components/scream/extern/catch2/include',
        '-isystem','/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx',
        '-isystem','/home/shared/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I/home/shared/workdir/hommexx/hommexx-src/components/homme/src/',
        '-I/home/shared/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/',
        '-I/home/shared/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/mpi',
        '-I/home/shared/workdir/hommexx/hommexx-src/components/homme/src/share/cxx/vector',
        '-I/home/shared/workdir/hommexx/hommexx-src/components/homme/test/unit_tests/',
        '-I/home/shared/workdir/hommexx/hommexx-build-debug/src/',
        '-I/home/shared/workdir/hommexx/hommexx-build-debug/test_execs/preqx_flat_ut/',
        '-I/home/shared/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat/',
        '-I/home/shared/workdir/hommexx/hommexx-build-debug/test_execs/prtcA_flat_c/',
]

KOKKOS_FLAGS = [
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src',
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src/Cuda',
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src/OpenMP',
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src/Qthread',
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src/Threads',
        '-I/home/shared/workdir/kokkos/kokkos-src/core/src/impl',
        '-I/home/shared/workdir/kokkos/kokkos-src/containers/src',
        '-I/home/shared/workdir/kokkos/kokkos-src/containers/src/impl',
        '-I/home/shared/workdir/kokkos/kokkos-src/algorithms/src',
]

IBECS_FLAGS = [
        '-I/home/shared/workdir/ibecs/ibecs-src/src/',
        '-I/home/shared/workdir/ibecs/ibecs-build-debug/src',
]

ALBANY_FLAGS = [
        '-I/home/shared/workdir/albany/albany-src/branch/src',
        '-I/home/shared/workdir/albany/albany-src/branch/src/adapt',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/catalyst',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/pumi',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/stk',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/stk/percept',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance',
        '-I/home/shared/workdir/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance_utils',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/bc',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/gather',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/interpolation',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/pde',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/response',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/scatter',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/state',
        '-I/home/shared/workdir/albany/albany-src/branch/src/evaluators/utility',
        '-I/home/shared/workdir/albany/albany-src/branch/src/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/utility',
        '-I/home/shared/workdir/albany/albany-src/branch/src/utility/math',
        '-I/home/shared/workdir/albany/albany-src/branch/src/adapt',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Aeras',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Aeras/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Aeras/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Aeras/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AFRL/communicators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AFRL/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AFRL/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AMP/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AMP/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/AMP/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/ANISO',
        '-I/home/shared/workdir/albany/albany-src/branch/src/ATO',
        '-I/home/shared/workdir/albany/albany-src/branch/src/ATO/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/ATO/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/ATO/utils',
        '-I/home/shared/workdir/albany/albany-src/branch/src/CTM',
        '-I/home/shared/workdir/albany/albany-src/branch/src/FELIX',
        '-I/home/shared/workdir/albany/albany-src/branch/src/FELIX/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/FELIX/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/FELIX/interface_with_cism',
        '-I/home/shared/workdir/albany/albany-src/branch/src/FELIX/interface_with_mpas',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Hydride/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Hydride/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/ACE',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/bc',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/HMC',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/kinematics',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/lame',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/linear-elasticity',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/peridigm',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/poro',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/projection',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/residuals',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/size-field',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/surface-element',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/evaluators/transport',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/models',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/models/core',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/models/variational',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/parallel_evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/parallel_models',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/problems/lame',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/solvers',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/test/unit_tests',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/test/utils',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/utils',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/utils/dtk_interp_and_error',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/utils/lame',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/utils/mortar',
        '-I/home/shared/workdir/albany/albany-src/branch/src/LCM/utils/topology',
        '-I/home/shared/workdir/albany/albany-src/branch/src/MOR',
        '-I/home/shared/workdir/albany/albany-src/branch/src/QCAD',
        '-I/home/shared/workdir/albany/albany-src/branch/src/QCAD/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/QCAD/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/QCAD/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/responses',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Tsunami/evaluators',
        '-I/home/shared/workdir/albany/albany-src/branch/src/Tsunami/problems',
        '-I/home/shared/workdir/albany/albany-src/branch/src/utility',
        '-I/home/shared/workdir/albany/albany-build/gcc/opt/branch/src',
]

TRILINOS_FLAGS = [
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/aztecoo/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/belos/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/epetra/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/epetraext/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/epetraext/src/inout',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/epetraext/src/model_evaluator',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/epetraext/src/transform',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ifpack2/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Cell',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Discretization',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Kokkos',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Orientation',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Shared',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/kokkos/core/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/kokkos/containers/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/kokkos/algorithms/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Coarsen',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Comm',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/FEGrid',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Include',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Krylov',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/LevelWrap',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/MLAPI',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Main',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/MatrixFree',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Operator',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/RefMaxwell',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Smoother',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/ml/src/Utils',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Graph',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Headers',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Interface',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Misc',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/MueCentral',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Rebalancing',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Smoothers',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Transfers',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/muelu/src/Utils',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-loca/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-epetra',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-lapack',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-mf',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-belos',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-petsc',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-thyra',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-epetra',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/nox/src-lapack',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/phalanx/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/piro/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rythmos/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/algorithm',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/elementwise',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/function',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/sol',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/status',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/step',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/utils',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/vector',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/rol/src/zoo',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/Fad/Fad',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/Fad/TinyFad',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/Fad/TinyFadET',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/Fad/utils',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/src/',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/src/mpl',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/src/parameter',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/sacado/src/template',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/stk/stk_io/stk_io',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/stk/stk_mesh/stk_mesh/base',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/stk/stk_mesh/stk_mesh/baseImpl',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/stk/stk_topology/stk_topology',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/stk/stk_util/stk_util',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/teuchos/core/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/teuchos/comm/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/teuchos/parameterlist/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/teuchos/numerics/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/teuchos/kokkoscompat/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_vector/client_support',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_solve/client_support',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetra/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetraext/src/transformer',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/thyra/adapters/tpetra/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/tpetra/core/src',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/tpetra/core/inout',
        '-I/home/shared/workdir/trilinos/trilinos-src/packages/tpetra/core/ext',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include',
]

TRILINOS_INCLUDE_FLAGS = [
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/Cuda',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/generated_specializations_hpp',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/gtest',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/impl',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/OpenMP',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/Qthreads',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_expreval',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_io',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_math',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_mesh',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_ngp',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_search',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_simd',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_simd_view',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_tools',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_topology',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_transfer',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_unit_test_utils',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/stk_utils',
        '-isystem',
        '/home/shared/workdir/trilinos/trilinos-install/marzemino/gcc/debug/develop/include/Threads',
]

KOKKOS_INCLUDE_FLAGS = [
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/Cuda',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/eti',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/impl',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/OpenMP',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/OpenMPTarget',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/Qthreads',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/ROCm',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/Serial',
        '-isystem',
        '/home/shared/workdir/kokkos/kokkos-install/marzemino/gcc/debug/include/Threads',
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

def FlagsForFile(filename, **kwargs):
    final_flags = []
    is_scream = in_directory(filename,'/home/shared/workdir/scream/scream-src')
    if is_scream :
      final_flags = final_flags + SCREAM_FLAGS + KOKKOS_INCLUDE_FLAGS
    is_e3sm = in_directory(filename,'/home/shared/workdir/e3sm/e3sm-src')
    if is_e3sm :
      final_flags = final_flags + E3SM_FLAGS + KOKKOS_INCLUDE_FLAGS
    is_homme = in_directory(filename,'/home/shared/workdir/hommexx/hommexx-src')
    if is_homme :
      final_flags = final_flags + HOMME_FLAGS + KOKKOS_INCLUDE_FLAGS
    is_kokkos = in_directory(filename,'/home/shared/workdir/kokkos/kokkos-src')
    if is_kokkos :
      final_flags = final_flags + KOKKOS_FLAGS
    is_albany = in_directory(filename,'/home/shared/workdir/albany/albany-src')
    if is_albany:
      final_flags = final_flags + ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_ibecs = in_directory(filename,'/home/shared/workdir/ibecs/ibecs-src')
    if is_ibecs :
      final_flags = final_flags + IBECS_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_trilinos = in_directory(filename,'/home/shared/workdir/trilinos/trilinos-src')
    if is_trilinos :
      final_flags = final_flags + TRILINOS_FLAGS

    final_flags = final_flags + BASE_FLAGS;

    return {
      'flags'    : final_flags,
    }
