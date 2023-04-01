cd 010_reference_lines/hl_lhc_collisions_offbb_offerrors
python 000_pymask.py > output.log 2> error.log &
cd ../

cp hl_lhc_collisions_offbb_offerrors/clean_it.sh hl_lhc_collisions_offbb_onerrors/
cp hl_lhc_collisions_offbb_offerrors/clean_it.sh hl_lhc_collisions_onbb_offerrors/
cp hl_lhc_collisions_offbb_offerrors/clean_it.sh hl_lhc_collisions_onbb_onerrors/

cp hl_lhc_collisions_offbb_offerrors/*.py hl_lhc_collisions_offbb_onerrors/
cp hl_lhc_collisions_offbb_offerrors/*.py hl_lhc_collisions_onbb_offerrors/
cp hl_lhc_collisions_offbb_offerrors/*.py hl_lhc_collisions_onbb_onerrors/

cd hl_lhc_collisions_offbb_onerrors
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_offerrors
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_onerrors
python 000_pymask.py > output.log 2> error.log &
cd ../../

cd ../



