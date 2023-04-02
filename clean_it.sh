conda deactivate    
rm Miniforge3-Linux-x86_64.sh
rm -rf lhcmask  miniforge3  xdeps  xfields  xmask  xobjects  xpart  xtrack hllhc14 lhcerrors lhctoolkit  runIII

cd 010_reference_lines/hl_lhc_collisions_offbb_offerrors_b1
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_offbb_onerrors_b1
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_offerrors_b1
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_onerrors_b1
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_offbb_offerrors_b2
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_offbb_onerrors_b2
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_offerrors_b2
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_onerrors_b2
source clean_it.sh
cd ../..

