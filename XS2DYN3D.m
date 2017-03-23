function XS2DYN3D(USER_INP)

% ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
% Written by :: Kotlyar Dan
%               Date : 02-May-13
% version    :: ver.001
% Following features are not included: 
% - Radial ADFs
% - Axial  ADFs




% *******************************************************************
% MAIN FUNCTION:
% 1.  Executes each branching case independently
%     & creates an XS.dat file that contains all the parameters in 
%     a specific format
% 2.  Collects all the data and prepares the _wqs file (DYN3D format)
%     for each fuel (universe - in serpent).
% *******************************************************************

% Initialize parameters:
% 
% RESTART      = [];
% BURNUP_STEPS = [];
% FUEL         = [];
% COOLANT      = [];
% BU_br        = [];

% OBTAIN ALL INPUT PARAMETERS FROM THIS FILE
% 1 - check is this file is .m file
Nchars = length(USER_INP); % count the # of chars 
if Nchars>2
    % if not an .m file then convert to .m file
    if ~(strcmp(USER_INP(end-1:end),'.m')) % if not an .m file
        USER_INP_M = [USER_INP '.m'];
        copyfile(USER_INP,USER_INP_M);
    else
        USER_INP_M = USER_INP;
    end
else
    USER_INP_M = [USER_INP '.m'];
    copyfile(USER_INP,USER_INP_M);
end

% Evaluate all the parameters to the workspace of Matlab
eval(USER_INP_M(1:end-2))

% Display all the parameters of the USER and perform senity check
% -------------------------------------------------------------------
if isempty(RESTART)
    fprintf(1,'\n ... No restart option was chosen, Ordinary Branching is perform\n');
else
   if (length(RESTART)==3) 
   fprintf(1,'Restart option was chosen, BU = %d , Tfuel = %d, Cdensity = %d \n',RESTART); 
   else
   fprintf(1,'!!! Restart option was chosen, BUT the variable should contain 3 points:BU,Tfuel,Cdensity\n'); 
   fprintf(1,'Please correct the RESTART CARD\n'); 
   return;
   end
end

% The value BU =0 is not allowed in depletion calculation
if any(BURNUP_STEPS==0)
    BURNUP_STEPS(BURNUP_STEPS==0) = [];
end
% Constract the FUEL variable 
if iscell(FUEL) % check if the var type is cell
     FUELMAT = FUEL;
     fprintf(1,'The number of fuel types is: %d\n',size(FUEL,1));
     clear FUEL
    for idx_fuel=1:size(FUELMAT,1) % constract the FUEL(i).ID array     
        FUEL(idx_fuel).ID = FUELMAT{idx_fuel,:};
        fprintf(1,'FUEL ID # %d  is: %s\n',idx_fuel,FUEL(idx_fuel).ID);
    end
else
    fprintf(1,'!!! FUEL CARD: should be a cell type\n');
    fprintf(1,'Please add {...} parentheses \n');
    return;
end
% Constract the COOLANT variable 
if iscell(COOLANT) % check if the var type is cell
    COOLMAT = COOLANT;
    fprintf(1,'The number of coolant types is: %d\n',size(COOLANT,1));
    clear COOLANT
    for idx_cool=1:size(COOLMAT,1) % constract the FUEL(i).ID array     
        COOLANT(idx_cool).ID = COOLMAT{idx_cool,:};
        fprintf(1,'COOLANT ID # %d  is: %s\n',idx_cool,COOLANT(idx_cool).ID);
    end
else
    fprintf(1,'!!! COOLANT CARD: should be a cell type\n');
    fprintf(1,'Please add {...} parentheses \n');
    return;
end

if NG < 1
   fprintf(1,'!!! NG CARD: the number of energy group should be positive and integer\n'); 
   fprintf(1,'Example:  NG = 12 \n');
   return;
end


[BU_vals,~, ~]  = intersect(BURNUP_STEPS,BU);
BU_br = BU;
if any(BU==0), BU_br = BU; BU_br(BU==0)=[]; end
if all(BU_vals==BU_br)
    if BU(1)==0, fprintf(1,'For this burnup branching will be done: %3.3f  MWd/kg\n',0); end
        
    fprintf(1,'For this burnup branching will be done: %3.3f  MWd/kg\n',BU);
else
    fprintf(1,'!!! BU CARD: should contain points that exist in BURNUP_STEPS\n');
    fprintf(1,'Please update the BU card\n');
    return;
    
end
clear BU_vals

if size(TF,1)~=size(FUELMAT,1) 
    fprintf(1,'!!! TF CARD: the size(TF,1) should be equal to %d\n',size(FUELMAT,1));
    fprintf(1,'Please update the TF card\n'); 
    return;
end
if size(CD,1)~=size(FUELMAT,1) 
    fprintf(1,'!!! CD CARD: the size(CD,1) should be equal to %d\n',size(FUELMAT,1));
    fprintf(1,'Please update the CD card\n'); 
    return;
end

if exist(SINP,'file')~=2
    fprintf(1,'!!! SINP CARD: The file %s does not exist\n',SINP);
    fprintf(1,'Please insert the name of the Serpent file\n'); 
    return;
end


% *******************************************************************
% USER DEFINED OPTIONS :: BRANCHING CASES DESCRIPTION
% -----------------------------------------------------
%
% THE DATA DESCRIBED BELOW COMES FROM THE INPUT FILE
% 
% % OPTION FOR RESTART
% --------------------------------------------------------
% RESTART = [];
% % RESTART = [iB iTF iCD];
% %********************
% % ALL BURNUP STEPS
% % --------------------------------------------------------
% BURNUP_STEPS = [0.1 0.5 0.7 1.25];
% %
% %********************
% % FUEL NAMES
% % --------------------------------------------------------
% FEUL = {'Fuel_101' ; 'Blanket' };
% %
% %********************
% % COOLANT NAMES
% % --------------------------------------------------------
% COOLANT = { 'water1' ; 'water2' };
% %
% %********************
% % NUMBER OF ENERGY GROUPS
% % --------------------------------------------------------
% % 
% NG = 2;
% %********************
% % BURNUP BRANCHING POINTS
% % --------------------------------------------------------
% %  
% BU = [0.1 0.7];
% %
% %********************
% % FUEL TEMPERATURE
% % --------------------------------------------------------
% %  
% TF = [600 900 1200;
%       600 900 1200];
% %********************      
% % COOLANT DENSITY
% % --------------------------------------------------------
% %       
% CD = [-0.650 0.700;
%       -0.650 0.700];
% %********************      
% % SERPENT INPUT FILE
% % --------------------------------------------------------
% %      
% SINP     = 'serp';
% %********************
% % EXECUTION COMMAND
% % --------------------------------------------------------
% %
% SEXE     = 'mpirun -hostfile host4MPI -np 4 sss2 -omp 4';   
% % 
% % ********************************************************        




% *******************************************************************
% CROSS SECTIONS PREFIXES DEFINITION
% 
PRF_LIB = ['.03c';'.06c';'.09c';'.12c';'.15c';'.18c']; % general prefix libraries
T_LIB   = [300;600;900;1200;1500;1800];                % adequate temperatures for the prfexis
% Preparation of the hom-XS
ver = 0; %0- DIFF = 1/3./P1_TRANSPXS;  1- DIFF = B1_INF_DIFFCOEF;
% ********************************************************************
    

% #########################################################################
% ###                                                                   ###
% ###                    START ACTIVE FUNCTION                          ###       
% ###                                                                   ###      
% #########################################################################                 


% NBC - N umber  of  B ranching  C ases
% NBC  = size(CD,2) * length(TF,2) ; 

% -------------------------------------------------------------------------
% --- 1) Read the input file and obtain all the required data
% 
% param includes all the original
% SINP  :: Serpent input file (without BU steps and without printm card)
% SINPM :: Modified Serpent file that don't include fuel material specification 
SINPM = ['mod_' SINP];
param = Read_Serpent_Input(SINP,SINPM,FUEL,COOLANT);
% 

% --- 2) Prepare new file with BU steps and execute to obtain all
%        compositions
% 
% SINP :: Serpent input file (without BU steps and without printm card)

SMOD = ['BU_' SINP]; % modified serpent file (includes BU&printm)

if isempty(RESTART)
    Burnup(SINP, SMOD, SEXE, BURNUP_STEPS);
    B_ini   = 1;
    TF_ini_ = 1;
    CD_ini  = 1;
else
    B_ini   = RESTART(1);
    TF_ini_ = RESTART(2);
    CD_ini  = RESTART(3);
end

% Read the new material name
new_material_file = [SMOD '.bumat0'];
param = Mod_mat_ID(new_material_file,param);


% --- 3) Create BR_CASES dir. and copy all the files there

% create the directory
mkdir('BR_CASES')
copyfile *.bumat* BR_CASES

% delete files execpt .bumat .res
delete([SMOD '*.seed']);
delete([SMOD '*.out']);
delete([SMOD '*.png']);
% SINP file will be used as a template for different branching cases


% Loop over all branching case (FUEL & COOLANT)
%

BURNUP_STEPS = [0 BURNUP_STEPS];
[BU_vals, idxBUsteps, idxBUsave] = intersect(BURNUP_STEPS,BU);

for iB=B_ini:(length(BU_vals))   % Loop - BU branching calculations

    for iTF=TF_ini_:size(TF,2) % Loop - fuel T branching calculations
        
        for iCD=CD_ini:size(CD,2) % Loop - coolant Dens. branching calculations
           
            % Prepare the param variable that includes specific BR-CASE
            for iMat=1:length(param)
                param(iMat).prf_new = PRF_LIB(T_LIB == TF(iMat,iTF),:); % New prefix 900 = '.09c'
                param(iMat).den_new = CD(iMat,iCD);
            end
            
            % Files that are required for preparing the branching case
            SERP_EXE = ['BR_BU_' num2str(iB-1) '_TF_' num2str(iTF) '_CD_' num2str(iCD)];    % exe. serpent file
            MAT_EXE  = ['MATERIAL_' num2str(iB-1) '_TF_' num2str(iTF) '_CD_' num2str(iCD)]; % corresponding mat. file 
            MAT_INP  = [SMOD '.bumat' num2str(idxBUsteps(iB)-1)];
            % Prepare the branching input file for a specific 'i' set
            Branch_Case(SERP_EXE,MAT_EXE,SINPM,MAT_INP,param)
            % execute serpent for the specific BR-CASE
            [~,~] = unix([SEXE ' ' SERP_EXE],'-echo');

            % Reads all the XS from .res file and writes the data -->
            % XS.dat file
            % The file that contains all the results
            SERP_RES = [SERP_EXE '_res.m'];
            create_xs_dat(ver,SERP_RES,BU_vals(iB),TF(:,iTF),CD(:,iCD));            
            
            % delete the input files for this BR-CASE (except the .res
            % file)
            delete(SERP_EXE);
            delete(MAT_EXE);
            delete([SERP_EXE '*.seed']);
            delete([SERP_EXE '*.out']);
            delete([SERP_EXE '*.png']);
            % move the .res file to different directory
            movefile(SERP_RES,'BR_CASES');
            

            
        end % coolant Dens.
        
    end % fuel T
    
    % ---------------------------------------------------------
    % Prepare the .wqs file for DYN3D - for a specific BU step
    % the files are prepred for all universes types
    % includes all possible branching cases
    BU_flag=0; if iB==(length(BU_vals)), BU_flag=1; end
    CREATE_WQS_FILES_4_UNIVERSE(BU_flag,NG,BU_vals(iB),CD,TF);
    
    %
    %
    % ---------------------------------------------------------
    
    
end % Loop - BU
    
    
% END of the MAIN FUNCTION
% *************************************************************************
% *************************************************************************




function CREATE_WQS_FILES_4_UNIVERSE(BU_flag,ng,BU,DEN,FT)


% *******************************************************************
% CREATE_WQS_FILES_4_UNIVERSE:
% 1.  Reads XS.dat file and extract all the XS data for a certain universe
%     & creates a parmeter tlines_array which is then used:
% 2.  to Prepare the _wqs file (DYN3D format)
%     for each fuel (universe - in serpent).
% *******************************************************************

% -------------------------------------------------------
% outXSdat    ::  The name of XS (DYN3D format) for this universe
% ng          ::  Number of energy groups
% BU          ::  Current BU [MWd/kg]
% DEN         ::  Coolant density vector
% FT          ::  Fuel temperature vector
% -------------------------------------------------------

inpXSdat = 'XS.dat';
fid=fopen(inpXSdat);

% Copy the first line
tline = fgetl(fid);
tlines_array{1} = tline;
while 1
    
    tline = fgetl(fid);
    %Stop reading at the end of file
    if ~ischar(tline), break, end
    
    tlines_array =  [tlines_array;{tline}];
end
fclose(fid);
delete(inpXSdat);


% Create the XS file for DYN3D format
% =====================================================

% Matrix of the data
% 
% STUCTURE of the Matrix
% 
% UNIV;BU;TF;CD;TrXS;AbXs;ProdXS;kFiss;Sct;ADF;CHI
% Built the matrix with all the XS data
XSDATA = [];
for i_arr=1:length(tlines_array)
    XSDATA = [XSDATA;str2num(tlines_array{i_arr,:})];
end
% UNI::Types of universes
UNI = unique(XSDATA(:,1));


for iU=1:length(UNI) % number of universes
    

    idx_uni = find(XSDATA(:,1) == UNI(iU)); % indeces of the specific universe
    % The part of the table for this universe iU
    XSDATA_UNIV = XSDATA(idx_uni,:);
    % Initialize the data for this specific universe
    UDATA = zeros(size(XSDATA_UNIV,1),size(XSDATA_UNIV,2)-4);
    count = 1;
    
    % The construction of the XS is done according to the NEMTAB fromat
    % (DYN3D)
    for iFT = 1:size(FT,2)
        for iDEN = 1:size(DEN,2)
            % XS data for specific universe for all its potential branching
            % for specific BU point
            
            idx_DEN = find(XSDATA_UNIV(:,4)==DEN(iU,iDEN)); % indeces of the specific densities
            idx_FT  = find(XSDATA_UNIV(:,3)==FT(iU,iFT));   % indeces of the specific densities
            % idx_case matches the specific case of required XS
            [idx_case,~,~] = intersect(idx_DEN,idx_FT);
            UDATA(count,:) = XSDATA_UNIV(idx_case,5:end);
            count = count + 1;
        end
    end
    
    % The file to where the data is stored
    out_file = ['XS_UNIV_' num2str(UNI(iU)) '.dat'];
    % prepares the XS (WQS) file
    nBR = size(FT,2) * size(DEN,2);
    SERPENT2DYN3D(BU_flag,out_file,UDATA,ng,BU,DEN(iU,:),FT(iU,:));
end


function SERPENT2DYN3D(BU_flag,outXSdat,XSVAL,ng,BU,DEN,FT)

% ---------------------------------------
% Description:
%  BU   =   burnup
% DEN   =   moderator density
% BOR   =   boron concentration
%  FT   =   fuel temperature
%  MT   =   moderator temperature

% Pre-determined strings
legend{1,:} = '* Transport XSEC Table';
legend{2,:} = '* Absorption XSEC Table';
legend{3,:} = '* Nu-Fission XSEC Table';
legend{4,:} = '* Kappa-Fission XSEC Table';
legend{5,:} = '* Scattering XSEC Table';
legend{6,:} = '* ADF Table';
legend{7,:} = '* Fission Spectrum';
legend{8,:} = '* Inverse Velocity';
legend{9,:} = '* Delay Neutron Decay Constant (Lambda)';
legend{10,:} = '* Delay Neutron Fraction (Beta)';

str1 = '*   Group ';
str2 = ' -> ';

DEN = 1000*abs(DEN);
% check if this function is executed for the first time
if exist(outXSdat,'file') ~=2; % The file doesn't exist
    fid=fopen(outXSdat,'a');
    
    fprintf(fid,'*      Mod Dens      Boron      Fuel Temp       Mod Temp\n');
    fprintf(fid,'             %d          0             %d              0\n',[size(DEN,2) size(FT,2)]);
    
    basic_format = '%4.3f     ';
    print_format1 = ['         ' repmat(basic_format,1,size(DEN,2)) '\n'];
    print_format2 = ['         ' repmat(basic_format,1,size(FT,2)) '\n'];
    fprintf(fid,print_format1,DEN'); % print all the densities options
    fprintf(fid,print_format2,FT');  % print all the fuel temperature options
    
    fprintf(fid,'* \n');
    
else
    fid=fopen(outXSdat,'a');
    
end

% values of TrXS; AbXs; ProdXS; kFiss; Sct; ADF; CHI
% ng - number of groups

% stage-1: print the decsription of the current branching state
% -------
fprintf(fid,'* ----------------------------------------------------------------\n');
tline = ['* BURNUP   ' num2str(BU,'%04.3f')];
fprintf(fid,'%s\n',tline);
fprintf(fid,'* ----------------------------------------------------------------\n');
fprintf(fid,'* \n');

% stage-2: print the homogenized values for each legend
% -------

% FOR: TRXS,ABSXS,NUFXS,KAFISSXS
% *************************************************************************

for i=1:4
    tline = legend{i,:};
    fprintf(fid,'%s\n',tline);
    fprintf(fid,'* \n');
    
    % swip over group energies
    for ig=1:ng
        tline = [str1 num2str(ig,'%02.0f')];
        fprintf(fid,'%s\n',tline);
        NRXSVAL = reshape(XSVAL(:,1),size(DEN,2),size(FT,2))';
        for iBR=1:size(NRXSVAL,1)
            tline = ['  ' num2str(NRXSVAL(iBR,:),'%1.6e   ')];
            fprintf(fid,'%s\n',tline);
        end
        
        XSVAL(:,1) = [];
    end
    
    fprintf(fid,'* \n');
end


% Scattering XSEC Table
% *************************************************************************

tline = legend{5,:};
fprintf(fid,'%s\n',tline);
fprintf(fid,'* \n');

% swipe over group (ngxng) energies
for ig=1:ng
    for jg=1:ng
        tline = [str1 num2str(ig,'%02.0f') str2 num2str(jg,'%02.0f')];
        fprintf(fid,'%s\n',tline);
        
        NRXSVAL = reshape(XSVAL(:,1),size(DEN,2),size(FT,2))';
        for iBR=1:size(NRXSVAL,1)
            tline = ['  ' num2str(NRXSVAL(iBR,:),'%1.6e   ')];
            fprintf(fid,'%s\n',tline);
        end
        
        XSVAL(:,1) = [];
    end
end

fprintf(fid,'* \n');

% ADF Table
% *************************************************************************

tline = legend{6,:};
fprintf(fid,'%s\n',tline);
fprintf(fid,'* \n');

for ig=1:ng
    tline = [str1 num2str(ig,'%02.0f')];
    fprintf(fid,'%s\n',tline);
    
    NRXSVAL = reshape(XSVAL(:,1),size(DEN,2),size(FT,2))';
    for iBR=1:size(NRXSVAL,1)
        tline = ['  ' num2str(NRXSVAL(iBR,:),'%1.6e   ')];
        fprintf(fid,'%s\n',tline);
    end
    
    
    XSVAL(:,1) = [];
end

fprintf(fid,'* \n');

% Axial ADFs bottom and top
% *************************************************************************
% legendADF{1,:} = '* bottom';
% legendADF{2,:} = '* top';
% fprintf(fid,'* Axial ADF\n');
% AADF = [BADF;TADF];
% for iADF=1:2
%     tline = legendADF{iADF,:};
%     fprintf(fid,'%s\n',tline);
%     
%     % swip over group energies
%     for ig=1:ng
%         tline = [str1 num2str(ig,'%02.0f')];
%         fprintf(fid,'%s\n',tline);
%         tline = ['  ' num2str(AADF(iADF,ig),'%1.6e   ')];
%         fprintf(fid,'%s\n',tline);
%     end
%     
% end
% 
% fprintf(fid,'* \n');

% Fission Spectrum
% *************************************************************************

tline = legend{7,:};
fprintf(fid,'%s\n',tline);
fprintf(fid,'* \n');

tline1 = [];
tline2 = [];
for ig=1:ng
    tline1 = [tline1 '              ' num2str(ig,'%02.0f')];
    tline2 = [tline2 '   ' num2str(XSVAL(1),'%1.6e')];
    XSVAL(:,1) = [];
end
tline1 = [str1 tline1()];
fprintf(fid,'%s\n',tline1(12:end));
fprintf(fid,'%s\n',tline2(2:end));

fprintf(fid,'* \n');


% Inverse Velocity
% *************************************************************************

tline = legend{8,:};
fprintf(fid,'%s\n',tline);
fprintf(fid,'* \n');

tline1 = [];
tline2 = [];
for ig=1:ng
    tline1 = [tline1 '              ' num2str(ig,'%02.0f')];
    tline2 = [tline2 '   ' num2str(1,'%1.6e')];
end
tline1 = [str1 tline1()];
fprintf(fid,'%s\n',tline1(12:end));
fprintf(fid,'%s\n',tline2(2:end));

fprintf(fid,'* \n');

% Delay Neutron Data
% *************************************************************************
fprintf(fid,'* Delay Neutron Decay Constant (Lambda) \n');
fprintf(fid,'*   \n');
fprintf(fid,'* GROUP       1              2              3              4              5              6\n');
fprintf(fid,'  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000\n');
fprintf(fid,'*   \n');
fprintf(fid,'* Delay Neutron Fraction (Beta)\n');
fprintf(fid,'*   \n');
fprintf(fid,'* GROUP       1              2              3              4              5              6\n');
fprintf(fid,'  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000\n');
fprintf(fid,'*\n');

if BU_flag % if this is the last BU point
    fprintf(fid,'End\n');
end
% The END ++++++++++++++++++++++++++++
fclose(fid);




function create_xs_dat(B1_opt,file_list,BU,TF,CD)

% --------------------------------------
% This function creates XS.dat file
% that includes all the homogenized
% parameters in a .txt format
% --------------------------------------

% This is the option for diffusion coef. calculation
% 0- DIFF = 1/3./P1_TRANSPXS;  1- DIFF = B1_INF_DIFFCOEF;

B1=B1_opt;

% Serpent *res.m

Remove_NAN_resFile(file_list)

eval(file_list(1:end-2))


if (B1==1);
 
    TRANSPXS = B1_TRANSPXS;
    TRANSPXS(:,2:2:end)=[];
    
    RABSXS = B1_RABSXS;
    RABSXS(:,2:2:end)=[];
    
    NSF = B1_NSF;
    NSF(:,2:2:end)=[];
    
    FISSXS=B1_FISS;
    FISSXS(:,2:2:end)=[];

    FISSE=B1_KAPPA;
    FISSE(:,2:2:end)=[];
    
    CHI=B1_CHIT;
    CHI(:,2:2:end)=[];    
    
    GPRODXS = B1_SP0;
    GPRODXS(:,2:2:end)=[];
    
    %GPRODXS=reshape(GPRODXS,GC_NE(1),GC_NE(1))';
else
    
    TRANSPXS = INF_TRANSPXS;
    TRANSPXS(:,2:2:end)=[];
    
    RABSXS = INF_RABSXS;
    RABSXS(:,2:2:end)=[];
    
    NSF = INF_NSF;
    NSF(:,2:2:end)=[];
    
    FISSXS=INF_FISS;
    FISSXS(:,2:2:end)=[];

    FISSE=INF_KAPPA;
    FISSE(:,2:2:end)=[];
    
    CHI=INF_CHIT;
    CHI(:,2:2:end)=[];    
    
    GPRODXS = INF_SP0;
    GPRODXS(:,2:2:end)=[];
    % GPRODXS=reshape(GPRODXS,MACRO_NG(1),MACRO_NG(1))';

end




for i=1:idx
    a = reshape(GPRODXS(i,:),MACRO_NG(1),MACRO_NG(1));
    a1 = a;
    a2 = reshape(a1,MACRO_NG(1)*MACRO_NG(1),1)';
    GPRODXS(i,:) = a2;
end

SigTr = TRANSPXS;
SigA =   RABSXS;
SigP = NSF;
SigF = FISSXS;
SCT_MAT = GPRODXS;

FISSE=(1.60217653e-13)*FISSE;
kF = FISSE .* SigF;

testADFS = exist('ADFS','var');
if testADFS == 1
    ADFS(:,2:2:end)=[]; % Removing statisticis;
    % nSides = length(ADFS)/MACRO_NG(1);
    ADFS = ADFS(:,1:MACRO_NG(1));
else
    ADFS = ones(idx,  MACRO_NG(1));
end

% AllDataBasic
GC_UNI = str2num(GC_UNIVERSE_NAME);

nUNI = length(unique(GC_UNI)); % number of universes for which XS are prepared


AllData = [GC_UNI repmat(BU,length(GC_UNI),1) repmat(TF,length(GC_UNI)/nUNI,1) repmat(CD,length(GC_UNI)/nUNI,1) ... 
           SigTr SigA SigP kF SCT_MAT ADFS CHI];
basic_format = '%6.7e ';
nValues = size(AllData,2);
print_format = ['%6.0f ' repmat(basic_format,1,nValues-1) '\n'];

filename = 'XS.dat';
fid = fopen(filename,'a');
% ------------------------------------------------------
% Prints the legend that describes the different cases
% ------------------------------------------------------
% fprintf(fid,'Legend for every raw: \n');
% fprintf(fid,'Fuel type;BU; TF; CD; TrXS; AbXs; ProdXS; kFiss; Sct; ADF; CHI\n');
fprintf(fid,print_format,AllData');


fclose all;

% end function - create-xs-dat



function Branch_Case(exe_file,exe_mat,input_file,mat_file,param)


% ****************************************************
% 
% Function that executes only 1 branching case 
% for specific set of input (temp.&dens.) parameters
% 
% ****************************************************

% -------------------------------------------------------
% exe_file   ::  New updated serpent exe file
% exe_mat    ::  Material file with updated prefixes
% input_file ::  Serpent input file
% mat_file   ::  File that includes materials
% param      ::  Structure that includes
%                1) universe numbers
%                2) fuel&mod material id
%                3) fuel&mod temperatures and densities
% -------------------------------------------------------


input = mat_file;
ouput = exe_mat;

% param(1).fuel_id = 'Fuel_101';
% param(1).prf_ref = '.09c';
% param(1).prf_new = '.06c';
% param(1).mod_id = 'water1';
% param(1).den_ref = '-0.7500';
% param(1).den_new = '-0.6900';

% -------------------------------------------------------
% Write the fuel temperature

fidi = fopen(input);
fido = fopen(ouput,'w');

nMat = length(param);     % number of universes to update

while 1
    tline = fgetl(fidi);
    %Stop reading at the end of file
    if ~ischar(tline), break, end

    % Identify the fuel material --> to obtain temperature (prefix)
    mat_test = regexpi(tline,'mat ','start');
    com_test = regexpi(tline,'%','start');
    if ( ~isempty(mat_test) && isempty(com_test))
        
        for imat=1:nMat
            [str1 ~] = strtok(tline(4:end));     % reads the name of the material from the .butot file 
            if strfind(str1,param(imat).fuel_id)
                prf_ref = param(imat).prf_ref;   % reference prefix (temperature)
                prf_new = param(imat).prf_new;   % modified  prefix (temperature)
                break;
            end
        end
    end
    
    %Find the temperatures dependent isotopes
    c_test = regexpi(tline,'.[0-9]+c');
    if ~isempty(c_test)
        tline = strrep(tline,prf_ref,prf_new);   % replace the reference prefix with the modified one
    end


    fprintf(fido,'%s\n',tline);

end

fclose(fidi);
fclose(fido);


% -------------------------------------------------------
% Write the Moderator density and the new fuel name

fidi = fopen(input_file);
fido = fopen(exe_file,'w');

mat_position = [param.position]; % pointers position of all material location

while 1
    tline = fgetl(fidi);
    %Stop reading at the end of file
    if ~ischar(tline), break, end
    
    curr_pos = ftell(fidi);
    idx_mat = find(mat_position == curr_pos); 
    if ~isempty(idx_mat)
        tline = strrep(tline,param(idx_mat).fuel_id,param(idx_mat).fuel_id_mod);
    end
    
    
    % Identify the fuel material --> to obtain temperature (prefix)
    mat_test = regexpi(tline,'mat ','start');
    if ~isempty(mat_test)
        if (tline(1)=='%'), continue, end
        for imat=1:nMat
            [str1 ~] = strtok(tline(4:end));     % reads the name of the material from the serpent input file
            if strfind(str1,param(imat).mod_id)
                den_ref = param(imat).den_ref;   % reference coolant density
                den_new = param(imat).den_new;   % modified  coolant density
                tline = strrep(tline,den_ref,num2str(den_new,'%4.5f'));   % replace the reference density with the modified one
                break;
            end
        end
    end
    

    fprintf(fido,'%s\n',tline);

end

% include the corresponding mat file
fprintf(fido,'include "%s"\n',exe_mat);

fclose(fidi);
fclose(fido);



% end function -  create_xs_dat 




function [param] = Read_Serpent_Input(InpWithMat,InpNoMat,FUEL,COOLANT)


% ****************************************************
% 
% Function that reads the input and excludes the 
% fuel material from the actual.  
% In addition, fuel T and coolant densities are saved
% ****************************************************

% -------------------------------------------------------
% InpWithMat  ::  S-input file with    burnable materials
% InpNoMat    ::  S-input file withOUT burnable materials
% FUEL        ::  Fuel Structure with Name
% COOLANT     ::  Coolant Structure with Name
% -------------------------------------------------------

% FUEL(1).ID    = 'Fuel_101';
% FUEL(2).ID    = 'Blanket';
% COOLANT(1).ID = 'water1';
% COOLANT(2).ID = 'water2';


nMat = length(FUEL); % number of burnable regions
% Initialize the basic data for each fuel&coolant type
for iMat=1:nMat
    param(iMat).fuel_id = FUEL(iMat).ID;
    param(iMat).fuel_id_mod = []; % new fuel name
    param(iMat).prf_ref = [];
    param(iMat).prf_new = [];
    param(iMat).position = [];
    param(iMat).mod_id  = COOLANT(iMat).ID;
    param(iMat).den_ref = [];
    param(iMat).den_new = [];
end

fidi = fopen(InpWithMat);
fido = fopen(InpNoMat,'w');


while 1
    tline = fgetl(fidi);
    %Stop reading at the end of file
    if ~ischar(tline), break, end
    
    
    % Identify the fuel material --> to obtain temperature (prefix)
    mat_test = regexpi(tline,'mat ','start');
    
    
    % Loop that finds pointer location of the fuel material
    for iMat=1:nMat
        if (~isempty(regexpi(tline,[param(iMat).fuel_id ' '],'start')) && isempty(mat_test))
        param(iMat).position = ftell(fidi); % the position of the fuel name
        end   
    end
    
    

    
    if ~isempty(mat_test) % If any material is found
        
        if (tline(1)=='%'), continue, end % check if it is a comment line
        
        for imat=1:nMat
            
            [str1 ~] = strtok(tline(4:end));     % str1 is the ID of the material
            
            if strfind(str1,param(imat).fuel_id) % check if the mat is fuel
                
                while 1 % procedure that reads the prefix composition
                    tline = fgetl(fidi);
                    c_test = regexpi(tline,'.[0-9]+c');
                    if ~isempty(c_test)
                        param(imat).prf_ref = tline(6:9);
                    else
                        break;
                    end
                    
                end % while
                
                break;
            end % if - strfind (fuel)
            
            coolant_cond = regexpi(tline,[param(imat).mod_id ' '],'end');
            if ~isempty(coolant_cond)  % check if the mat is coolant
                [param(imat).den_ref, ~] = strtok(tline(coolant_cond+1:end));    
                break;
            end
            
        end % for nMat
    end % mat_test
    
    fprintf(fido,'%s\n',tline);

end

fclose(fidi);
fclose(fido);



function Burnup(SINP, SMOD, SEXE, BURNUP_STEPS)


% ****************************************************
% 
% Function that executes BU calculations and prepares 
% composition file for each step
% 
% ****************************************************

% -------------------------------------------------------
% SINP          ::  Original serpent input (average branching parameters)
% SMOD          ::  Modified serpent file that includes BU steps [MWd/kg] 
% SEXE          ::  Serpent execution data 
% BURNUP_STEPS  ::  All the burnup steps to prepare the composition for
% -------------------------------------------------------


% SEXE = 'mpirun -hostfile host4MPI -np 12 ~kotlyar/sss '


% Add to the input file the BU steps
% -----------------------------------
copyfile(SINP,SMOD)
fid = fopen(SMOD,'a');
% Write the dep card to the new file
tline = ['dep butot ' num2str(BURNUP_STEPS,'%4.4f ')];
fprintf(fid,'%s\n',tline);
% Create all the XS data
fprintf(fid,'set printm 1 \n'); 
fclose(fid);


% Execute the new file to get all the compositions at different BU steps
% 

[~,~] = unix([SEXE ' ' SMOD ],'-echo');



function [param] = Mod_mat_ID(FMAT,param)


% ****************************************************
% 
% This function finds what is the modified name of the 
% fuel material in the included
% mat (/bumat) file
% ****************************************************


fidi = fopen(FMAT);

nMat = length(param);     % number of universes to update
count = 1;
while 1
    tline = fgetl(fidi);
    %Stop reading at the end of file
    if ~ischar(tline), break, end

    % Identify the fuel material --> to obtain temperature (prefix)
    mat_test = regexpi(tline,'mat ','start');
    com_test = regexpi(tline,'%','start');
    if ( ~isempty(mat_test) && isempty(com_test))
        
        for imat=1:nMat
            [str1 ~] = strtok(tline(4:end));     % reads the name of the material from the .butot file 
            if strfind(str1,param(imat).fuel_id)
                param(imat).fuel_id_mod = str1;   % new modified fuel name
                count=count+1;
                break;
            end
        end
    if count>nMat, break, end
    end
    

end

fclose(fidi);


function Remove_NAN_resFile(resFile)

resFile_temp = ['NAN' resFile];
fidi = fopen(resFile);
fido = fopen(resFile_temp,'w');

while 1
    tline = fgetl(fidi);
    %Stop reading at the end of file
    if ~ischar(tline), break, end

    % Identify the fuel material --> to obtain temperature (prefix)
    nan_test = regexpi(tline,'NAN','start');

    if ~isempty(nan_test)
       tline = strrep(tline,'NAN','0.0E+00'); 
    end

    fprintf(fido,'%s\n',tline);

end

fclose(fidi);
fclose(fido);

delete(resFile);
movefile(resFile_temp,resFile)



