# last versions of xobjects, xpart, xtrack, xfields
cd xobjects 
git checkout main
cd ../

cd xpart 
git checkout main
cd ../

cd xtrack
git checkout main
cd ../

cd xfields
git checkout main
cd ../

cd 011_test_lines

cd hl_lhc_collisions_offbb_offerrors
python 000_xmask.py &
cd ../

cd hl_lhc_collisions_offbb_onerrors
python 000_xmask.py &
cd ../

cd hl_lhc_collisions_onbb_onerrors
python 000_xmask.py &
cd ../

cd hl_lhc_collisions_onbb_offerrors
python 000_xmask.py &
cd ../../

