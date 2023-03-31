wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b -p ./miniforge3
rm Miniforge3-Linux-x86_64.sh

source miniforge3/bin/activate

pip install numpy scipy matplotlib pandas ipython pytest pyarrow

git clone https://github.com/xsuite/xobjects
pip install -e xobjects

git clone https://github.com/xsuite/xdeps
pip install -e xdeps

git clone https://github.com/xsuite/xpart
pip install -e xpart

git clone https://github.com/xsuite/xtrack
pip install -e xtrack

git clone https://github.com/xsuite/xfields
pip install -e xfields

git clone https://github.com/xsuite/xmask
pip install -e xmask



cd xmask
git submodule init
git submodule update
cd ..

git clone https://github.com/lhcopt/lhcmask
pip install -e lhcmask

git clone https://github.com/lhcopt/hllhc14
git clone https://github.com/lhcopt/lhcerrors
git clone https://github.com/lhcopt/lhctoolkit

git clone $(whoami)@lxplus.cern.ch:/afs/cern.ch/eng/lhc/optics/runIII

pip install xsuite --no-deps
xsuite-prebuild