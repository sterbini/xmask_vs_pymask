wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b -p ./miniforge3
rm Miniforge3-Linux-x86_64.sh

source miniforge3/bin/activate

pip install numpy scipy matplotlib pandas ipython pytest pyarrow pyyaml

git clone https://github.com/xsuite/xobjects --branch v0.1.32
pip install -e xobjects

git clone https://github.com/xsuite/xdeps 
pip install -e xdeps

git clone https://github.com/xsuite/xpart --branch v0.13.0
pip install -e xpart

git clone https://github.com/xsuite/xtrack --branch v0.28.0
pip install -e xtrack

git clone https://github.com/xsuite/xfields --branch v0.10.1
pip install -e xfields

git clone https://github.com/lhcopt/lhcmask
pip install -e lhcmask

git clone https://github.com/lhcopt/hllhc14
git clone https://github.com/lhcopt/lhcerrors
git clone https://github.com/lhcopt/lhctoolkit

git clone $(whoami)@lxplus.cern.ch:/afs/cern.ch/eng/lhc/optics/runIII

pip install xsuite --no-deps
xsuite-prebuild

git clone https://github.com/xsuite/xmask
pip install -e xmask
cd xmask
git submodule init
git submodule update
cd ..
