cd 010_reference_lines

cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_offbb_onerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_onbb_offerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_onbb_onerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_offbb_offerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_offbb_onerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_onbb_offerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/clean_it.sh hl_lhc_collisions_onbb_onerrors_b2/

cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_offbb_onerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_onbb_offerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_onbb_onerrors_b1/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_offbb_offerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_offbb_onerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_onbb_offerrors_b2/
cp hl_lhc_collisions_offbb_offerrors_b1/*.py hl_lhc_collisions_onbb_onerrors_b2/

cd hl_lhc_collisions_offbb_offerrors_b1
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_offbb_onerrors_b1
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_offerrors_b1
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_onerrors_b1
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_offbb_offerrors_b2
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_offbb_onerrors_b2
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_offerrors_b2
python 000_pymask.py > output.log 2> error.log &
cd ../

cd hl_lhc_collisions_onbb_onerrors_b2
python 000_pymask.py > output.log 2> error.log &
cd ../../
