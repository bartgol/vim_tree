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
        '-DNDEBUG',
        '-std=c++11',
        '-I/usr/lib/',
        '-I/usr/include/',
        '-isystem',
        '/home/lbertag/.vim/bundle/YouCompleteMe/include/omp', # for omp.h
        '-isystem',
        '/home/lbertag/.vim/bundle/YouCompleteMe/include/openmpi', # for mpi
        '-isystem',
        '/home/lbertag/.vim'
]

TRILINOS_INCLUDE_FLAGS = [
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/Cuda',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/generated_specializations_hpp',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/gtest',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/impl',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/OpenMP',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/Qthread',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_expreval',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_io',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_math',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_mesh',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_search',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_search',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_simd',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_simd_view',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_topology',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_transfer',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_unit_test_utils',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/stk_util',
        '-isystem',
        '/storage/workdir/trilinos/trilinos-install/groppello/gcc/debug/include/Threads',
]

HOMME_FLAGS = [
        '-DHAVE_CONFIG_H',
        '-D__AVX__',
        '-I/storage/workdir/hommexx/hommexx-src/branch/components/homme/src/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/components/homme/src/share/cxx/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/components/homme/src/share/cxx/mpi',
        '-I/storage/workdir/hommexx/hommexx-src/branch/components/homme/src/share/cxx/vector/',
        '-I/storage/workdir/hommexx/hommexx-src/branch/components/homme/test/unit_tests/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/src/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/share_ut/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/preqx_flat_ut/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcA_flat/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcA_flat_c/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcB_flat/',
        '-I/storage/workdir/hommexx/hommexx-build/gcc/branch/debug/test_execs/prtcB_flat_c/',
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
        '-I/storage/workdir/albany/albany-src/branch/src/FELIX/evaluators',
        '-I/storage/workdir/albany/albany-src/branch/src/FELIX/problems',
        '-I/storage/workdir/albany/albany-src/branch/src/FELIX/interface_with_cism',
        '-I/storage/workdir/albany/albany-src/branch/src/FELIX/interface_with_mpas',
]

IBECS_FLAGS = [
        '-I/storage/workdir/ibecs/ibecs-src/src/',
        '-I/storage/workdir/ibecs/ibecs-build-debug-gcc/src',
]

TRILINOS_FLAGS = [
        '-I/storage/workdir/trilinos/trilinos-src/packages/aztecoo/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/belos/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/epetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/epetraext/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/epetraext/src/inout',
        '-I/storage/workdir/trilinos/trilinos-src/packages/epetraext/src/model_evaluator',
        '-I/storage/workdir/trilinos/trilinos-src/packages/epetraext/src/transform',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ifpack2/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Cell',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Discretization',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Kokkos',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Orientation',
        '-I/storage/workdir/trilinos/trilinos-src/packages/intrepid2/core/src/Shared',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/abs',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/axpby',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/dot',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/fill',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/mult',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm1',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm2',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrm2w',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/nrmInf',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/recip',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/scal',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/spmv',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/sum',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/impl/generated_specializations_cpp/update',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/batched',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/batched/host',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/blas3',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/graph/',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/graph/impl',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos-kernels/src/stage/graph/utils',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/algorithms/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/containers/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/Cuda',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/OpenMP',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/OpenMPTarget',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/Qthreads',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/Threads',
        '-I/storage/workdir/trilinos/trilinos-src/packages/kokkos/core/src/impl',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Coarsen',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Comm',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/FEGrid',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Include',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Krylov',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/LevelWrap',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/MLAPI',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Main',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/MatrixFree',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Operator',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/RefMaxwell',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Smoother',
        '-I/storage/workdir/trilinos/trilinos-src/packages/ml/src/Utils',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Graph',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Headers',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Interface',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Misc',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/MueCentral',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Rebalancing',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Smoothers',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Transfers',
        '-I/storage/workdir/trilinos/trilinos-src/packages/muelu/src/Utils',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-belos',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-epetra',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-lapack',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-loca/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-epetra',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-lapack',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-loca/src-mf',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-petsc',
        '-I/storage/workdir/trilinos/trilinos-src/packages/nox/src-thyra',
        '-I/storage/workdir/trilinos/trilinos-src/packages/phalanx/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/piro/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/algorithm',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/elementwise',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/function',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/sol',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/status',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/step',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/utils',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/vector',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rol/src/zoo',
        '-I/storage/workdir/trilinos/trilinos-src/packages/rythmos/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/Fad/Fad',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/Fad/TinyFad',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/Fad/TinyFadET',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/Fad/utils',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/src/',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/src/mpl',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/src/parameter',
        '-I/storage/workdir/trilinos/trilinos-src/packages/sacado/src/template',
        '-I/storage/workdir/trilinos/trilinos-src/packages/stk/stk_io/stk_io',
        '-I/storage/workdir/trilinos/trilinos-src/packages/stk/stk_mesh/stk_mesh/base',
        '-I/storage/workdir/trilinos/trilinos-src/packages/stk/stk_mesh/stk_mesh/baseImpl',
        '-I/storage/workdir/trilinos/trilinos-src/packages/stk/stk_topology/stk_topology',
        '-I/storage/workdir/trilinos/trilinos-src/packages/stk/stk_util/stk_util',
        '-I/storage/workdir/trilinos/trilinos-src/packages/teuchos/comm/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/teuchos/core/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/teuchos/kokkoscompat/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/teuchos/numerics/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/teuchos/parameterlist/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetraext/src/model_evaluator',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/adapters/epetraext/src/transformer',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/adapters/tpetra/src',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/model_evaluator/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/solvers/extended',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/nonlinear/solvers/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_solve/extended',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_solve/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_vector/extended',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/interfaces/operator_vector/fundamental',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/nonlinear/model_evaluator/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/nonlinear/solvers/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_solve/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_vector/adapter_support',
        '-I/storage/workdir/trilinos/trilinos-src/packages/thyra/core/src/support/operator_vector/client_support',
        '-I/storage/workdir/trilinos/trilinos-src/packages/tpetra/core/ext',
        '-I/storage/workdir/trilinos/trilinos-src/packages/tpetra/core/inout',
        '-I/storage/workdir/trilinos/trilinos-src/packages/tpetra/core/src',
        '-I/storage/workdir/trilinos/trilinos-install-debug-gcc/include',
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
    if is_homme :
      final_flags = HOMME_FLAGS + TRILINOS_INCLUDE_FLAGS + BASE_FLAGS
    elif is_kokkos :
      final_flags = KOKKOS_FLAGS + BASE_FLAGS
    elif is_albany :
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
