
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.27' ;
COMPILE_DATE              (idx, [1: 20])  = 'Jan  2 2017 18:32:04' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 15])  = 'PWR Pin TH ONLY' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pwrpin300_p001' ;
WORKING_DIRECTORY         (idx, [1: 49])  = '/gpfs/pace1/project/pme/pme2/ajohnson400/GPT/d300' ;
HOSTNAME                  (idx, [1: 25])  = 'iw-k37-36.pace.gatech.edu' ;
CPU_TYPE                  (idx, [1: 39])  = 'Six-Core AMD Opteron(tm) Processor 8431' ;
CPU_MHZ                   (idx, 1)        = 2399.8 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 27 20:05:11 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Feb 27 20:34:03 2017' ;

% Run parameters:

POP                       (idx, 1)        = 100000 ;
CYCLES                    (idx, 1)        = 550 ;
SKIP                      (idx, 1)        = 100 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1488243911 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 3 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 0 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 16 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  16]) = [  9.79992E-01  1.02100E+00  9.99963E-01  9.78096E-01  1.03297E+00  9.97326E-01  9.76963E-01  1.02291E+00  1.02924E+00  9.67782E-01  1.02853E+00  9.99483E-01  9.68800E-01  9.98626E-01  1.02072E+00  9.77605E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 53])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 1.5E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  7.02770E-03 0.00028  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.92972E-01 2.0E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  6.69529E-01 4.2E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  6.70265E-01 4.2E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.87840E+00 8.5E-05  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.71287E+01 7.6E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.71281E+01 7.6E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.33456E+01 0.00013  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.63090E+01 7.8E-05  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 550 ;
SOURCE_POPULATION         (idx, 1)        = 55000717 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00001E+05 0.00019 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00001E+05 0.00019 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  4.22480E+02 ;
RUNNING_TIME              (idx, 1)        =  2.88631E+01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.72817E-01  1.72817E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.45500E-02  1.45500E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  2.86637E+01  2.86637E+01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  2.83873E+01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 14.63740 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.52200E+01 0.00100 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.92537E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64556.10 ;
ALLOC_MEMSIZE             (idx, 1)        = 3580.27;
MEMSIZE                   (idx, 1)        = 1043.73;
XS_MEMSIZE                (idx, 1)        = 122.46;
MAT_MEMSIZE               (idx, 1)        = 336.28;
RES_MEMSIZE               (idx, 1)        = 0.71;
MISC_MEMSIZE              (idx, 1)        = 584.28;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 2536.54;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 2 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 210454 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-09 ;
NEUTRON_EMAX              (idx, 1)        =  1.50000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 7 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 45 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 45 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 580 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  2.90007E+07 ;
TOT_DECAY_HEAT            (idx, 1)        =  2.01247E-05 ;
TOT_SF_RATE               (idx, 1)        =  1.32086E+03 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  2.90007E+07 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  2.01247E-05 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  2.34410E+02 ;
INGESTION_TOXICITY        (idx, 1)        =  1.31465E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
TOT_PHOTON_SRC            (idx, 1)        =  7.60276E+06 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  3.47956E+10 0.00013  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  4.98254E-01 0.00031 ];
U235_FISS                 (idx, [1:   4]) = [  1.73181E+15 0.00014  9.30876E-01 5.0E-05 ];
U238_FISS                 (idx, [1:   4]) = [  1.28601E+14 0.00073  6.91240E-02 0.00068 ];
U235_CAPT                 (idx, [1:   4]) = [  3.90941E+14 0.00038  2.40672E-01 0.00033 ];
U238_CAPT                 (idx, [1:   4]) = [  1.05774E+15 0.00029  6.51165E-01 0.00014 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 55000859 5.50009E+07 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 1.16646E+05 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 55000859 5.51175E+07 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 25620313 2.56758E+07 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 29346457 2.94069E+07 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 33947 3.39650E+04 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 55000717 5.51166E+07 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  6.03908E+04 3.3E-09 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.01136E-02 5.1E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.58350E+15 4.0E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.86048E+15 4.4E-07 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  1.62445E+15 0.00014 ];
TOT_ABSRATE               (idx, [1:   2]) = [  3.48493E+15 6.6E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  3.47956E+15 0.00013 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.57152E+17 0.00012 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  2.14879E+12 0.00545 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.48708E+15 6.7E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  9.45892E+16 9.8E-05 ];
INI_FMASS                 (idx, 1)        =  2.00543E+00 ;
TOT_FMASS                 (idx, 1)        =  2.00543E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46362E+00 4.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02599E+02 4.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.31723E+00 0.00013  1.30815E+00 0.00013  9.09047E-03 0.00221 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.31722E+00 6.7E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.31728E+00 0.00013 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.31722E+00 6.7E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.31804E+00 6.6E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.47253E-03 0.00162  1.52665E-04 0.00977  8.66699E-04 0.00396  8.45940E-04 0.00406  2.51734E-03 0.00245  8.16187E-04 0.00426  2.73700E-04 0.00658 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.16224E-01 0.00353  1.24908E-02 6.7E-07  3.16333E-02 6.7E-05  1.10289E-01 8.0E-05  3.21001E-01 6.6E-05  1.34484E+00 4.7E-05  8.90468E+00 0.00041 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.96039E-03 0.00226  1.94007E-04 0.01360  1.10154E-03 0.00563  1.08612E-03 0.00576  3.19491E-03 0.00342  1.03978E-03 0.00586  3.44029E-04 0.00958 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.11421E-01 0.00509  1.24908E-02 8.8E-07  3.16301E-02 9.1E-05  1.10287E-01 0.00012  3.21034E-01 9.3E-05  1.34475E+00 6.8E-05  8.90857E+00 0.00060 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.66780E-05 0.00028  1.66684E-05 0.00028  1.80564E-05 0.00268 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.19685E-05 0.00025  2.19559E-05 0.00025  2.37842E-05 0.00268 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.90079E-03 0.00221  1.91806E-04 0.01311  1.09134E-03 0.00545  1.06557E-03 0.00597  3.16853E-03 0.00332  1.03675E-03 0.00574  3.46805E-04 0.00956 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.19754E-01 0.00503  1.24908E-02 9.7E-07  3.16354E-02 9.4E-05  1.10300E-01 0.00011  3.20998E-01 9.5E-05  1.34470E+00 7.0E-05  8.90805E+00 0.00063 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.66647E-05 0.00065  1.66554E-05 0.00065  1.80238E-05 0.00681 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.19509E-05 0.00063  2.19387E-05 0.00063  2.37397E-05 0.00679 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.87732E-03 0.00661  2.01686E-04 0.03766  1.10065E-03 0.01702  1.06429E-03 0.01703  3.10394E-03 0.01002  1.04023E-03 0.01651  3.66519E-04 0.02943 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.43321E-01 0.01562  1.24908E-02 2.6E-06  3.16395E-02 0.00027  1.10285E-01 0.00034  3.20763E-01 0.00026  1.34473E+00 0.00020  8.89650E+00 0.00164 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.86677E-03 0.00637  2.00164E-04 0.03642  1.09791E-03 0.01637  1.06125E-03 0.01625  3.10501E-03 0.00964  1.03690E-03 0.01606  3.65538E-04 0.02872 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.42431E-01 0.01537  1.24908E-02 2.6E-06  3.16395E-02 0.00026  1.10290E-01 0.00032  3.20741E-01 0.00026  1.34465E+00 0.00020  8.89830E+00 0.00161 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.13055E+02 0.00668 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.66924E-05 0.00017 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.19875E-05 0.00012 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.89359E-03 0.00131 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.12983E+02 0.00132 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.80934E-07 0.00016 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.09715E-06 0.00014  3.09718E-06 0.00014  3.09385E-06 0.00153 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.54480E-05 0.00017  2.54493E-05 0.00017  2.52822E-05 0.00192 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.91653E-01 0.00012  5.90455E-01 0.00012  8.10474E-01 0.00255 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.02171E+01 0.00379 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.71281E+01 7.6E-05  3.01227E+01 9.5E-05 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 1 ;
MICRO_E                   (idx, [1:   2]) = [  6.25000E-07  1.96403E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1:   2]) = [  7.76379E+07 0.00019 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  3.08986E-01 0.00021 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.35072E+17 0.00025  0.00000E+00 0.0E+00 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.96244E-01 0.00017  0.00000E+00 0.0E+00 ];
INF_CAPT                  (idx, [1:   4]) = [  7.43008E-03 0.00016  0.00000E+00 0.0E+00 ];
INF_ABS                   (idx, [1:   4]) = [  1.05736E-02 0.00013  0.00000E+00 0.0E+00 ];
INF_FISS                  (idx, [1:   4]) = [  3.14349E-03 0.00012  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  8.03050E-03 0.00013  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.55464E+00 1.8E-05  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03709E+02 1.5E-06  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.57454E-08 0.00014  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.70200E-01 0.00017  0.00000E+00 0.0E+00 ];
INF_SCATT1                (idx, [1:   4]) = [  2.22510E-01 0.00021  0.00000E+00 0.0E+00 ];
INF_SCATT2                (idx, [1:   4]) = [  9.06993E-02 0.00022  0.00000E+00 0.0E+00 ];
INF_SCATT3                (idx, [1:   4]) = [  9.29391E-03 0.00059  0.00000E+00 0.0E+00 ];
INF_SCATT4                (idx, [1:   4]) = [ -8.22748E-03 0.00085  0.00000E+00 0.0E+00 ];
INF_SCATT5                (idx, [1:   4]) = [  6.33518E-04 0.00944  0.00000E+00 0.0E+00 ];
INF_SCATT6                (idx, [1:   4]) = [  5.11476E-03 0.00104  0.00000E+00 0.0E+00 ];
INF_SCATT7                (idx, [1:   4]) = [  9.23773E-04 0.00483  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.70254E-01 0.00017  0.00000E+00 0.0E+00 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.22511E-01 0.00021  0.00000E+00 0.0E+00 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.06995E-02 0.00022  0.00000E+00 0.0E+00 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.29388E-03 0.00059  0.00000E+00 0.0E+00 ];
INF_SCATTP4               (idx, [1:   4]) = [ -8.22757E-03 0.00085  0.00000E+00 0.0E+00 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.33577E-04 0.00946  0.00000E+00 0.0E+00 ];
INF_SCATTP6               (idx, [1:   4]) = [  5.11481E-03 0.00104  0.00000E+00 0.0E+00 ];
INF_SCATTP7               (idx, [1:   4]) = [  9.23814E-04 0.00485  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.66413E-01 0.00013  0.00000E+00 0.0E+00 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.25119E+00 0.00013  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.05189E-02 0.00013  0.00000E+00 0.0E+00 ];
INF_REMXS                 (idx, [1:   4]) = [  2.60446E-02 0.00020  0.00000E+00 0.0E+00 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  4.70200E-01 0.00017  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S1                    (idx, [1:   8]) = [  2.22510E-01 0.00021  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S2                    (idx, [1:   8]) = [  9.06993E-02 0.00022  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S3                    (idx, [1:   8]) = [  9.29391E-03 0.00059  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S4                    (idx, [1:   8]) = [ -8.22748E-03 0.00085  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S5                    (idx, [1:   8]) = [  6.33518E-04 0.00944  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S6                    (idx, [1:   8]) = [  5.11476E-03 0.00104  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S7                    (idx, [1:   8]) = [  9.23773E-04 0.00483  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  4.70254E-01 0.00017  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP1                   (idx, [1:   8]) = [  2.22511E-01 0.00021  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP2                   (idx, [1:   8]) = [  9.06995E-02 0.00022  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP3                   (idx, [1:   8]) = [  9.29388E-03 0.00059  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP4                   (idx, [1:   8]) = [ -8.22757E-03 0.00085  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP5                   (idx, [1:   8]) = [  6.33577E-04 0.00946  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP6                   (idx, [1:   8]) = [  5.11481E-03 0.00104  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP7                   (idx, [1:   8]) = [  9.23814E-04 0.00485  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  5.10165E-01 0.00037  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  5.09911E-01 0.00041  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  5.10125E-01 0.00045  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  5.10463E-01 0.00040  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  6.53385E-01 0.00037  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  6.53712E-01 0.00041  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  6.53439E-01 0.00045  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  6.53005E-01 0.00040  0.00000E+00 0.0E+00 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.96039E-03 0.00226  1.94007E-04 0.01360  1.10154E-03 0.00563  1.08612E-03 0.00576  3.19491E-03 0.00342  1.03978E-03 0.00586  3.44029E-04 0.00958 ];
LAMBDA                    (idx, [1:  14]) = [  8.11421E-01 0.00509  1.24908E-02 8.8E-07  3.16301E-02 9.1E-05  1.10287E-01 0.00012  3.21034E-01 9.3E-05  1.34475E+00 6.8E-05  8.90857E+00 0.00060 ];

