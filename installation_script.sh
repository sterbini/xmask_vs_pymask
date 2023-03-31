wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-latest-Linux-x86_64.sh
source miniforge3/bin/activate
pip install numpy scipy matplotlib pandas ipython pytest

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

git clone https://github.com/xsuite/lhcmask
pip install -e lhcmask

pip install -e xsuite --no-deps
xsuite-prebuild
