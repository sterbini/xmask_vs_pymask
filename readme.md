To run this test you need to install the environment with
```bash 
source 000_installation_script.sh 
```

then run the test with
```bash
source 001_run.sh
```

then run the test with
```bash
source 002_run.sh
```

then run the test with
```bash
source 003_run.sh
```

To check that all went as expected you can see the result files in 
```
011_test_lines/hl_lhc_collisions_offbb_offerrors/result.out
011_test_lines/hl_lhc_collisions_offbb_onerrors/result.out
011_test_lines/hl_lhc_collisions_onbb_onerrors/result.out
011_test_lines/hl_lhc_collisions_onbb_offerrors/result.out
```
All should end with 
```
    *********************************************************************************

    The line lhcb2 from test sequence and the line from reference are identical!
    
    *********************************************************************************
```



If the test is sucessful you can clean it
```bash
source clean_it.sh
```