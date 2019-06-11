import os
import fnmatch
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
        '-DNDEBUG',
        '-std=c++11',
        '-isystem','/home/lbertag/.vim/bundle/YouCompleteMe/third_party/ycmd/clang_includes/include',
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/6.1.0/base/lib/gcc/x86_64-pc-linux-gnu/6.1.0/include',
        '-isystem','/usr/local/include',
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/6.1.0/base/include',
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/6.1.0/base/lib/gcc/x86_64-pc-linux-gnu/6.1.0/include-fixed',
        '-isystem','/usr/include',
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/7.2.0/base/lib/gcc/x86_64-pc-linux-gnu/7.2.0/include', # for omp.h
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/7.2.0/openmpi/1.8.7/include', # for mpi
]

NETCDF_FLAGS = [
        '-isystem' ,'/projects/sems/install/rhel7-x86_64/sems/tpl/netcdf/4.4.1/gcc/7.2.0/openmpi/1.10.1/exo_parallel/include/',
]

BOOST_FLAGS = [
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/tpl/boost/1.63.0/gcc/7.2.0/base/include',
]

TRILINOS_INCLUDE_FLAGS = BOOST_FLAGS + NETCDF_FLAGS + [
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/Cuda',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/generated_specializations_hpp',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/gtest',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/impl',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/OpenMP',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/Qthread',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_expreval',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_io',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_math',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_mesh',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_search',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_search',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_simd',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_simd_view',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_topology',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_transfer',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_unit_test_utils',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/stk_util',
        '-isystem','/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include/Threads',
        '-isystem','/projects/sems/install/rhel7-x86_64/sems/tpl/boost/1.63.0/gcc/6.1.0/base/include/',
]

SCREAM_FLAGS = [
        '-I/storage/workdir/scream/scream-src/branch/components/scream/extern/catch2/include/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/control/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme/homme/src/preqx_kokkos',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme/homme/src/share/cxx',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme/homme/src/share/cxx/mpi',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme/homme/src/share/cxx/utilities',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/dynamics/homme/homme/src/share/cxx/vector',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/physics/p3/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/physics/rrtmgp/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/physics/shoc/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/src/share/',
        '-I/storage/workdir/scream/scream-src/branch/components/scream/extern/catch2/include/',
        '-I/storage/workdir/scream/scream-build/gcc/debug/branch/src/',
        '-I/storage/workdir/scream/scream-build/gcc/debug/branch/src//dynamics/homme/homme/src/share/cxx',
        '-I/storage/workdir/scream/scream-build/gcc/debug/branch/src/dynamics/homme/preqx_kokkos_np4_nlev72_qsize40_pioFALSE_energyFALSE',
        '-DHAVE_CONFIG_H',
        '-DHOMMEXX_CONFIG_IS_CMAKE',
        '-DSCREAM_CONFIG_IS_CMAKE',
]

E3SM_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-DNP=4',
        '-DPLEV=72',
        '-DQSIZE_D=4',
        '-I/storage/workdir/e3sm/e3sm-src/branch/cime/src/share/timing/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/mpi',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/utilities/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/share/cxx/vector/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/src/theta-l_kokkos/cxx/',
        '-I/storage/workdir/e3sm/e3sm-src/branch/components/homme/test/unit_tests/',
        '-I/storage/workdir/e3sm/e3sm-build/homme/gcc/debug/branch/src/',
        '-I/storage/workdir/e3sm/e3sm-build/homme/gcc/debug/branch/test_execs/share_kokkos_ut/',
        '-I/storage/workdir/e3sm/e3sm-build/homme/gcc/debug/branch/test_execs/preqx_ut/',
        '-I/storage/workdir/e3sm/e3sm-build/homme/gcc/debug/branch/test_execs/preqx-nlev26-kokkos/',
        '-I/storage/workdir/e3sm/e3sm-build/homme/gcc/debug/branch/test_execs/preqx-nlev72-kokkos/',
        '-isystem', '/storage/workdir/e3sm/e3sm-src/branch/components/homme/test/unit_tests/catch2/include',
        '-isystem', '/storage/workdir/e3sm/e3sm-src/branch/components/homme/utils/cime/src/share/timing',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-D__AVX__',
        '-I/storage/workdir/hommexx/hommexx-src/branch/src/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/src/share/cxx/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/src/share/cxx/mpi',
        '-I/storage/workdir/hommexx/hommexx-src/branch/src/share/cxx/vector/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/test/unit_tests/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/src/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/share_ut/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/preqx_ut/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcA/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcA_c/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcB/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcB_c/',
]

KOKKOS_FLAGS = [
        '-I/storage/workdir/kokkos/kokkos-src/core/src',
        '-I/storage/workdir/kokkos/kokkos-src/core/src/Cuda',
        '-I/storage/workdir/kokkos/kokkos-src/core/src/OpenMP',
        '-I/storage/workdir/kokkos/kokkos-src/core/src/Qthread',
        '-I/storage/workdir/kokkos/kokkos-src/core/src/Threads',
        '-I/storage/workdir/kokkos/kokkos-src/core/src/impl',
        '-I/storage/workdir/kokkos/kokkos-src/containers/src',
        '-I/storage/workdir/kokkos/kokkos-src/containers/src/impl',
        '-I/storage/workdir/kokkos/kokkos-src/algorithms/src',
]

ALBANY_FLAGS = [
        '-I/storage/workdir/albany/albany-build/gcc/opt/branch/src',
        '-I/storage/workdir/albany/albany-src/branch/src/',
        '-I/storage/workdir/albany/albany-src/branch/src/adapt',
        '-I/storage/workdir/albany/albany-src/branch/src/disc',
        '-I/storage/workdir/albany/albany-src/branch/src/disc/stk',
        '-I/storage/workdir/albany/albany-src/branch/src/disc/catalyst',
        '-I/storage/workdir/albany/albany-src/branch/src/disc/pumi',
        '-I/storage/workdir/albany/albany-src/branch/src/disc/tools',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/bc',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/gather',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/interpolation',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/pde',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/response',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/scatter',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/state',
        '-I/storage/workdir/albany/albany-src/branch/src/evaluators/utility',
        '-I/storage/workdir/albany/albany-src/branch/src/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/responses',
        '-I/storage/workdir/albany/albany-src/branch/src/utility',
        '-I/storage/workdir/albany/albany-src/branch/src/Aeras',
        '-I/storage/workdir/albany/albany-src/branch/src/Aeras/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/Aeras/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/Aeras/responses',
        '-I/storage/workdir/albany/albany-src/branch/src/AMP/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/AMP/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/AMP/responses',
        '-I/storage/workdir/albany/albany-src/branch/src/ATO',
        '-I/storage/workdir/albany/albany-src/branch/src/ATO/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/ATO/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/ATO/utils',
        '-I/storage/workdir/albany/albany-src/branch/src/LandIce/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/LandIce/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/LandIce/interface_with_cism',
        '-I/storage/workdir/albany/albany-src/branch/src/LandIce/interface_with_mpas',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/bc',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/kinematics',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/lame',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/linear-elasticity',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/peridigm',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/poro',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/projection',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/residuals',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/responses',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/size-field',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/evaluators/surface-element',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/models',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/models/core',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/models/variational',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/parallel_evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/parallel_models',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/solvers',
        '-I/storage/workdir/albany/albany-src/branch/src/LCM/utils',
]

PLATO_FLAGS = [
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/analyze',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/data_layer',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/Cogent/core',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/Cogent/geometry/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/Cogent/geometry/unit_tests',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/Cogent/unittest/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/MovingLeastSquares/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/geometry/MovingLeastSquares/unittest',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/input_checkers',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/input_generator',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/input_generator/unittest',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/interface',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/iso',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/iso/main',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/iso/unit_tests',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/models',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/optimize',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/proxy/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/support_structure/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/support_structure/main',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/tools/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/tools/math_parser',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/tools/unittest',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/xtk',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/xtk/unittest',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/Filters/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/AbstractInterface/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/Agent/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/BoundedSupportFunction',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/DiscreteGlobalOptimization',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/Example',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/Filter',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/Geometry',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/Helper',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/ParameterData',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibrary/SpatialSearching',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/base/src/PlatoSubproblemLibraryInterface/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/alpso_proxy/',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/bcpso_proxy',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/cogent',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/ksal_proxy',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/proxy',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/rocket',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/rosenbrock',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/services',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/services/matlab',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/services/python',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/services/python/expy',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/services/unittest',
        '-isystem', '/storage/workdir/other/platoengine/platoengine-src/apps/statics',
]

IBECS_FLAGS = [
        '-I/storage/workdir/ibecs/ibecs-src/src/',
        '-I/storage/workdir/ibecs/ibecs-build-debug-gcc/src',
]

TRILINOS_FLAGS = NETCDF_FLAGS + BOOST_FLAGS + [
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/aztecoo/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/belos/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/epetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/epetraext/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/epetraext/src/inout',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/epetraext/src/model_evaluator',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/epetraext/src/transform',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ifpack2/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src/Cell',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src/Discretization',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src/Kokkos',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src/Orientation',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/intrepid2/core/src/Shared',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/abs',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/axpby',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/dot',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/fill',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/mult',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm1',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm2',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm2w',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrmInf',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/recip',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/scal',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/spmv',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/sum',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/impl/generated_specializations_cpp/update',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/batched',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/batched/host',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/blas3',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/graph/',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/graph/impl',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos-kernels/src/stage/graph/utils',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/algorithms/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/containers/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/Cuda',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/OpenMP',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/OpenMPTarget',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/Qthreads',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/Threads',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/kokkos/core/src/impl',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Coarsen',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Comm',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/FEGrid',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Include',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Krylov',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/LevelWrap',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/MLAPI',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Main',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/MatrixFree',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Operator',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/RefMaxwell',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Smoother',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/ml/src/Utils',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Graph',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Headers',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Interface',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Misc',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/MueCentral',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Rebalancing',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Smoothers',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Transfers',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/muelu/src/Utils',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-belos',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-epetra',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-lapack',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-loca/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-loca/src-epetra',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-loca/src-lapack',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-loca/src-mf',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-petsc',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/nox/src-thyra',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/phalanx/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/piro/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/algorithm',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/elementwise',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/function',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/sol',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/status',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/step',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/utils',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/vector',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rol/src/zoo',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/rythmos/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/Fad/Fad',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/Fad/TinyFad',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/Fad/TinyFadET',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/Fad/utils',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/src/',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/src/mpl',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/src/parameter',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/sacado/src/template',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/seacas/libraries/ioss/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/seacas/libraries/ioss/src/exodus',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/seacas/libraries/ioss/src/exo_par',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/seacas/libraries/ioss/src/exo_fac',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/seacas/libraries/ioss/src/exo_fpp',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/stk/stk_io',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/stk/stk_mesh',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/stk/stk_topology',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/stk/stk_util',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/comm/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/kokkoscompat/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/numerics/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/parameterlist/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/teuchos/parser/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/adapters/epetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/adapters/epetraext/src/transformer',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/adapters/tpetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/support/operator_solve/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/thyra/core/src/support/operator_vector/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/tpetra/core/ext',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/tpetra/core/inout',
        '-I/storage/workdir/trilinos/trilinos-src/branch/packages/tpetra/core/src',
        '-I/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/develop/include', # assuming trilnos was installed before, this picks up all the XYZ_config.h files
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
    is_homme = in_directory(filename,'/storage/workdir/hommexx')
    is_kokkos = in_directory(filename,'/storage/workdir/kokkos')
    is_albany = in_directory(filename,'/storage/workdir/albany')
    is_ibecs = in_directory(filename,'/storage/workdir/ibecs')
    is_trilinos = in_directory(filename,'/storage/workdir/trilinos')
    is_e3sm = in_directory(filename,'/storage/workdir/e3sm')
    is_scream = in_directory(filename,'/storage/workdir/scream')
    if is_e3sm :
      final_flags = E3SM_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_homme:
      final_flags = HOMME_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_scream:
      final_flags = SCREAM_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_kokkos :
      final_flags = KOKKOS_FLAGS + BASE_FLAGS
    elif is_albany :
      if fnmatch.fnmatch(filename,'*Main_Solve_MPMD.cpp'):
        final_flags = ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS + PLATO_FLAGS + BASE_FLAGS
      else:
        final_flags = ALBANY_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_ibecs :
      final_flags = IBECS_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_trilinos :
      final_flags = TRILINOS_FLAGS + BASE_FLAGS
    else:
      final_flags = BASE_FLAGS

    return {
      'flags'    : final_flags,
    }
