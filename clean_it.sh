conda deactivate    
rm Miniforge3-Linux-x86_64.sh
rm -rf lhcmask  miniforge3  xdeps  xfields  xmask  xobjects  xpart  xtrack hllhc14 lhcerrors lhctoolkit  runIII

cd 010_reference_lines/hl_lhc_collisions_offbb_offerrors
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_offbb_onerrors
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_offerrors
source clean_it.sh
cd ../..

cd 010_reference_lines/hl_lhc_collisions_onbb_onerrors
source clean_it.sh
cd ../..

