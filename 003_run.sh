cd 011_test_lines


cd hl_lhc_collisions_offbb_offerrors
python t000_compare_against_legacy.py > result.out &
cd ../

cd hl_lhc_collisions_offbb_onerrors
python t000_compare_against_legacy.py > result.out &
cd ../

cd hl_lhc_collisions_onbb_onerrors
python t000_compare_against_legacy.py > result.out &
cd ../

cd hl_lhc_collisions_onbb_offerrors
python t000_compare_against_legacy.py > result.out &
cd ../../
