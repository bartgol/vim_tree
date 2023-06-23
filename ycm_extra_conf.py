import os
import ycm_core
from pathlib import Path

home = str(Path.home())
workdir = home + '/workdir'
pnetcdf_root = "/projects/sems/install/rhel8-x86_64/sems/tpl/parallel-netcdf/1.12.1/gcc/10.1.0/openmpi/4.0.5/f2e2w5d/"

WARN_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Wshadow',
        '--pedantic',
]

trilinos_src = workdir + '/trilinos/trilinos-src'
scream_src = workdir + '/scream/scream-src/$bld'
scream_ycm_includes = home + '/scripts/scream-ycm-includes'

BASE_FLAGS = [
        '-x',
        'c++',
        '-Wall',
        '-Wextra',
        '-Wshadow',
        '--pedantic',
        '-fopenmp',
        '-ferror-limit=10000',
        '-std=c++17',
        '-isystem','/usr/include/openmpi-x86_64/', # for mpi.h
]

E3SM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/share/',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/share/cxx',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/share/cxx/utilities',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/share/cxx/vector',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/theta-l_kokkos/cxx',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/src/preqx_kokkos/cxx',
        '-I'+workdir+'/e3sm/e3sm-src/branch/components/homme/test/unit_tests/catch2/include',
        '-I'+workdir+'/e3sm/e3sm-build/gcc/opt/branch/',
        '-I'+workdir+'/e3sm/e3sm-src/branch/cime/src/share/timing',
        '-DPLEV=72',
        '-DNP=4',
        '-DQSIZE_D=4',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src/OpenMP',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src/impl',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src/HIP',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src/Cuda',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/core/src/Threads',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/algorithms/src/',
        '-isystem', workdir+'/e3sm/e3sm-src/master/externals/kokkos/containers/src/',
        '-isystem', workdir+'/e3sm/e3sm-build/homme/gcc/debug/branch-pack-8/kokkos/build/',
]

SCREAM_EKAT_FLAGS = [
        '-I' + scream_src + '/externals/ekat/extern/Catch2/single_include/',
        '-I' + scream_src + '/externals/ekat/src/',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/core/src/',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/core/src/impl',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/core/src/OpenMP',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/core/src/Serial',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/algorithms/src',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/containers/src/',
        '-isystem',scream_src + '/externals/ekat/extern/kokkos/tpls/desul/include',
        '-isystem',scream_src + '/externals/ekat/extern/spdlog/include/',
        '-isystem',scream_ycm_includes + '/externals/ekat/src/',
        '-isystem',scream_ycm_includes + '/externals/kokkos/',
]

EKAT_FLAGS = [
        '-DEKAT_TEST_DOUBLE_PRECISION',
        '-I'+workdir+'/libs/ekat/ekat-build/gcc/debug/branch/src',
        '-I'+workdir+'/libs/ekat/ekat-build/gcc/debug/branch/tests',
        '-I'+workdir+'/libs/ekat/ekat-src/branch/src/',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/Catch2/single_include/',
        '-isystem',workdir+'/libs/ekat/ekat-build/gcc/debug/branch/externals/kokkos',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/algorithms/src',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/containers/src',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/core/src',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Cuda/',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/core/src/OpenMP/',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/kokkos/core/src/Serial/',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/yaml-cpp/include/',
        '-isystem',workdir+'/libs/ekat/ekat-src/branch/extern/spdlog/include',
]

CLDERA_FLAGS = [
        '-I'+workdir+'/cldera/cldera-src/branch/src',
        '-I'+workdir+'/cldera/cldera-src/branch/src/profiling',
        '-I'+workdir+'/cldera/cldera-src/branch/externals/ekat/src',
        '-I'+workdir+'/cldera/cldera-src/branch/externals/ekat/extern/Catch2/single_include/',
        '-I'+workdir+'/cldera/cldera-src/branch/externals/ekat/extern/kokkos/core/src/',
        '-I'+workdir+'/cldera/cldera-build/gcc/debug/branch/src',
        '-I'+workdir+'/cldera/cldera-build/gcc/debug/branch/externals/ekat',
        '-I'+workdir+'/cldera/cldera-build/gcc/debug/branch/externals/kokkos/',
]

SCREAM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-DHOMMEXX_CONFIG_IS_CMAKE',
        '-DSCREAM_CONFIG_IS_CMAKE',
        '-I' + home + '/scripts/scream-ycm-includes/src/',
        '-I' + scream_ycm_includes + '/src/dynamics/homme/homme/src/share/cxx',
        '-I' + scream_ycm_includes + '/src/dynamics/homme/tests',
        '-I' + scream_src + '/components/eamxx/src/',
        '-I' + scream_src + '/components/eamxx/src/control/',
        '-I' + scream_src + '/components/eamxx/src/share/',
        '-I' + scream_src + '/components/eamxx/src/share/field',
        '-I' + scream_src + '/components/eamxx/src/share/util/',
        '-I' + scream_src + '/components/eamxx/src/physics/p3/',
        '-I' + scream_src + '/components/eamxx/src/physics/rrtmgp/',
        '-I' + scream_src + '/components/eamxx/src/physics/shoc/',
        '-I' + scream_src + '/components/scream/src/',
        '-I' + scream_src + '/components/scream/src/control/',
        '-I' + scream_src + '/components/scream/src/share/',
        '-I' + scream_src + '/components/scream/src/share/field',
        '-I' + scream_src + '/components/scream/src/share/util/',
        '-I' + scream_src + '/components/scream/src/physics/p3/',
        '-I' + scream_src + '/components/scream/src/physics/rrtmgp/',
        '-I' + scream_src + '/components/scream/src/physics/shoc/',
        '-I' + scream_src + '/components/homme/src/share/cxx',
        '-I' + scream_src + '/components/homme/src/share/cxx/mpi',
        '-I' + scream_src + '/components/homme/src/share/cxx/utilities',
        '-I' + scream_src + '/components/homme/src/share/cxx/vector',
        '-I' + scream_src + '/components/homme/src/theta-l_kokkos/cxx',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/cpp/rrtmgp/kernels/',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/cpp/rte/',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/cpp/rte/kernels',
        '-isystem',scream_src+'/components/eam/src/physics/rrtmgp/external/cpp/',
        '-isystem',scream_src+'/externals/',
        '-isystem',scream_src+'/externals/scorpio/src/clib/',
        '-isystem',scream_src+'/externals/scorpio/src/gptl',
        '-isystem',scream_src+'/externals/YAKL/src',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-I'+workdir+'/hommexx/hommexx-src/components/homme/src/',
        '-I'+workdir+'/hommexx/hommexx-src/components/homme/src/share/cxx/',
        '-I'+workdir+'/hommexx/hommexx-src/components/homme/src/share/cxx/mpi',
        '-I'+workdir+'/hommexx/hommexx-src/components/homme/src/share/cxx/vector',
        '-I'+workdir+'/hommexx/hommexx-src/components/homme/test/unit_tests/',
        '-I'+workdir+'/hommexx/hommexx-build-debug/src/',
        '-I'+workdir+'/hommexx/hommexx-build-debug/test_execs/preqx_flat_ut/',
        '-I'+workdir+'/hommexx/hommexx-build-debug/test_execs/prtcA_flat/',
        '-I'+workdir+'/hommexx/hommexx-build-debug/test_execs/prtcA_flat_c/',
]

KOKKOS_FLAGS = [
        '-I'+workdir+'/kokkos/kokkos-src/core/src',
        '-I'+workdir+'/kokkos/kokkos-src/core/src/Cuda',
        '-I'+workdir+'/kokkos/kokkos-src/core/src/OpenMP',
        '-I'+workdir+'/kokkos/kokkos-src/core/src/Qthread',
        '-I'+workdir+'/kokkos/kokkos-src/core/src/Threads',
        '-I'+workdir+'/kokkos/kokkos-src/core/src/impl',
        '-I'+workdir+'/kokkos/kokkos-src/containers/src',
        '-I'+workdir+'/kokkos/kokkos-src/containers/src/impl',
        '-I'+workdir+'/kokkos/kokkos-src/algorithms/src',
]

IBECS_FLAGS = [
        '-I'+workdir+'/ibecs/ibecs-src/src/',
        '-I'+workdir+'/ibecs/ibecs-build-debug/src',
]

ALBANY_FLAGS = [
        '-I'+workdir+'/albany/albany-src/branch/src',
        '-I'+workdir+'/albany/albany-src/branch/src/corePDEs/evaluators',
        '-I'+workdir+'/albany/albany-src/branch/src/corePDEs/problems',
        '-I'+workdir+'/albany/albany-src/branch/src/demoPDEs/evaluators',
        '-I'+workdir+'/albany/albany-src/branch/src/demoPDEs/problems',
        '-I'+workdir+'/albany/albany-src/branch/src/disc',
        '-I'+workdir+'/albany/albany-src/branch/src/disc/stk',
        '-I'+workdir+'/albany/albany-src/branch/src/disc/stk/percept',
        '-I'+workdir+'/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance',
        '-I'+workdir+'/albany/albany-src/branch/src/disc/stk/percept/stk_rebalance_utils',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/bc',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/gather',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/interpolation',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/pde',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/response',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/scatter',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/state',
        '-I'+workdir+'/albany/albany-src/branch/src/evaluators/utility',
        '-I'+workdir+'/albany/albany-src/branch/src/problems',
        '-I'+workdir+'/albany/albany-src/branch/src/responses',
        '-I'+workdir+'/albany/albany-src/branch/src/utility',
        '-I'+workdir+'/albany/albany-src/branch/src/adapt',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce/evaluators',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce/evaluators/hydrology',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce/problems',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce/interface_with_cism',
        '-I'+workdir+'/albany/albany-src/branch/src/LandIce/interface_with_mpas',
        '-I'+workdir+'/albany/albany-src/branch/src/responses',
        '-I'+workdir+'/albany/albany-src/branch/src/utility',
        '-I'+workdir+'/albany/albany-src/branch/tests/unit',
        '-I'+workdir+'/albany/albany-build/gcc/branch/debug/src',
]

TRILINOS_FLAGS = [
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/aztecoo/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/belos/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/epetra/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/epetraext/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/epetraext/src/inout',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/epetraext/src/model_evaluator',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/epetraext/src/transform',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ifpack2/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Cell',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Discretization',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Kokkos',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src/Orientation',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/intrepid2/core/src/luca',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/kokkos/core/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/kokkos/containers/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/kokkos/algorithms/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Coarsen',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Comm',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/FEGrid',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Include',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Krylov',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/LevelWrap',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/MLAPI',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Main',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/MatrixFree',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Operator',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/RefMaxwell',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Smoother',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/ml/src/Utils',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Graph',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Headers',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Interface',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Misc',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/MueCentral',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Rebalancing',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Smoothers',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Transfers',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/muelu/src/Utils',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-loca/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-loca/src-epetra',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-loca/src-lapack',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-loca/src-mf',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-belos',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-petsc',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-thyra',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-epetra',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/nox/src-lapack',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/adapters-stk',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/adapters-stk/src/stk_interface',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/core/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/disc-fe/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/dof-mgr/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/panzer/expr-eval/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/phalanx/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/piro/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rythmos/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/algorithm',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/elementwise',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/function',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/sol',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/status',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/step',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/utils',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/vector',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/rol/src/zoo',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/Fad/Fad',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFad',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/Fad/TinyFadET',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/Fad/utils',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/src/',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/src/mpl',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/src/parameter',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/sacado/src/template',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/shards/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_io/stk_io',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_mesh/',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/base',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_mesh/stk_mesh/baseImpl',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_topology/stk_topology',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/stk/stk_util/stk_util',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/teuchos/core/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/teuchos/comm/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/teuchos/parameterlist/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/teuchos/numerics/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/teuchos/kokkoscompat/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/client_support',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/support/operator_solve/client_support',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/adapters/epetra/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/adapters/epetraext/src/transformer',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/thyra/adapters/tpetra/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/tpetra/core/src',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/tpetra/core/inout',
        '-I'+workdir+'/trilinos/trilinos-src/develop/packages/tpetra/core/ext',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/amesos2/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/anasazi/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/aztecoo/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/belos/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetra/src/'
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/epetraext/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ifpack2/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/intrepid2/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/kokkos-kernels/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/ml/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/muelu/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/minitensor/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/nox/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/piro/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/core/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/panzer/dof-mgr/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/phalanx/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rol/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/rtop/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/sacado/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/exodus/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/seacas/libraries/ioss/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/shards/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stratimikos/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/stk/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teko/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/thyra/core/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tempus/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/core/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/tpetra/tsqr/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/teuchos/core/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/xpetra/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan/src/',
        '-I'+workdir+'/trilinos/trilinos-build/gcc/debug/develop-serial/packages/zoltan2/src/',
]

TRILINOS_INCLUDE_FLAGS = [
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/Cuda',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/generated_specializations_hpp',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/gtest',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/impl',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/OpenMP',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/Qthreads',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_expreval',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_io',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_math',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_mesh',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_ngp',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_search',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_simd',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_simd_view',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_tools',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_topology',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_transfer',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_unit_test_utils',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/stk_utils',
        '-isystem', workdir+'/trilinos/trilinos-install/morellino/gcc/debug/develop-serial/include/Threads',
        '-isystem', workdir+'/libs/netcdf/netcdf-c/netcdf-c-install/include/',
        '-isystem', workdir+'/libs/netcdf/pnetcdf/pnetcdf-install/include/',
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

def is_master(file):
    #make absolute
    file = os.path.realpath(file)

    #return true, if the file name contains 'master'
    print ("file: {}".format(file))
    print ("master: {}".format("master" in file))
    return "master" in file

def Settings(**kwargs):
    filename = kwargs[ 'filename' ]
    final_flags = []
    is_ekat = in_directory(filename,workdir+'/libs/ekat/ekat-src')
    if is_ekat :
      final_flags = final_flags + EKAT_FLAGS
    is_scream = in_directory(filename,workdir+'/scream/scream-src')
    if is_scream :
      final_flags = final_flags + SCREAM_FLAGS + SCREAM_EKAT_FLAGS
    is_e3sm = in_directory(filename,workdir+'/e3sm/e3sm-src')
    if is_e3sm :
      final_flags = final_flags + E3SM_FLAGS
    is_kokkos = in_directory(filename,workdir+'/kokkos/kokkos-src')
    if is_kokkos :
      final_flags = final_flags + KOKKOS_FLAGS
    is_albany = in_directory(filename,workdir+'/albany/albany-src')
    if is_albany:
      final_flags = final_flags + ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_ibecs = in_directory(filename,workdir+'/ibecs/ibecs-src')
    if is_ibecs :
      final_flags = final_flags + IBECS_FLAGS + TRILINOS_INCLUDE_FLAGS
    is_trilinos = in_directory(filename,workdir+'/trilinos/trilinos-src')
    if is_trilinos :
      final_flags = final_flags + TRILINOS_FLAGS
    is_cldera = in_directory(filename,workdir+'/cldera/cldera-tools-src')
    if is_cldera :
      final_flags = final_flags + CLDERA_FLAGS


    if is_master(filename):
        final_flags = [i.replace('$bld','master') for i in final_flags]
    else:
        final_flags = [i.replace('$bld','branch') for i in final_flags]

    final_flags = final_flags + BASE_FLAGS;

    return {
      'flags'    : final_flags,
    }
