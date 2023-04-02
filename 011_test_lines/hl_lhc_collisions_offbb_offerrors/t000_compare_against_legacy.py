import time
import json
import numpy as np

import xtrack as xt
import xfields as xf

def norm(x):
    return np.sqrt(np.sum(np.array(x) ** 2))

atol = 1e-12
rtol = 3e-4
strict = False

with open('collider_02_tuned_bb_off.json', 'r') as fid:
    dct = json.load(fid)
    collider = xt.Multiline.from_dict(dct)

for sequence in ['lhcb1', 'lhcb2']:
    ltest = collider[sequence]

    if sequence == 'lhcb1':
        lref = xt.Line.from_json('../../010_reference_lines/hl_lhc_collisions_offbb_offerrors_b1/'
                                 'xsuite_lines/line_bb_for_tracking.json')
    else:
        lref = xt.Line.from_json('../../010_reference_lines/hl_lhc_collisions_offbb_offerrors_b2/'
                                 'xsuite_lines/line_bb_for_tracking.json')

    # we switch off the mqs
    for nn in lref.element_names:
        if nn.startswith('mqs.'):
            lref[nn].ksl[1]=0

    # we swithch off the dipolar elements very weakly powered
    for ll in (lref, ltest):
        for ii, ee in enumerate(ll.elements):
            if isinstance(ee, xt.Multipole):
                if np.abs(ee.knl[0])<1e-9:
                    ee.knl[0] = 0
                if np.abs(ee.ksl[0])<1e-9:
                    ee.ksl[0] = 0



    lref.particle_ref = ltest.particle_ref
    lref.build_tracker()
    ltest.build_tracker()

    tw_lref = lref.twiss()
    tw_ltest = ltest.twiss()

    lref.unfreeze()
    ltest.unfreeze()


    original_length = ltest.get_length()
    assert (lref.get_length() - original_length) < 1e-6

    # Simplify the two machines
    for ll in (ltest, lref):
        ll._var_management = None
        ll.remove_markers(inplace=True)
        ll.remove_inactive_multipoles(inplace=True)
        ll.remove_zero_length_drifts(inplace=True)
        ll.merge_consecutive_drifts(inplace=True)
        ll.merge_consecutive_multipoles(inplace=True)

        # Remove inactive RFMultipoles and normalize phase
        for ii, ee in enumerate(ll.elements):
            if ee.__class__.__name__ == 'RFMultipole':
                if ( np.max(np.abs(ee.knl)) < 1e-20 and
                        np.max(np.abs(ee.ksl)) < 1e-20 and
                        abs(ee.voltage) < 1e-20):
                    ll.element_names[ii] = None
                # # Normalize phase
                # for kkll, pp in [[ee.knl, ee.pn],
                #                  [ee.ksl, ee.ps]]:
                #     for ii, vv in enumerate(kkll):
                #         if vv < 0:
                #             kkll[ii] = -vv
                #             pp[ii] += 180
                #         if pp[ii]>180:
                #             pp[ii] -= 360

        while None in ll.element_names:
            ll.element_names.remove(None)

    # Check that the two machines are identical
    assert len(ltest) == len(lref)

    assert (ltest.get_length() - original_length) < 1e-6
    assert (lref.get_length() - original_length) < 1e-6

    for ii, (ee_test, ee_six, nn_test, nn_six) in enumerate(
        zip(ltest.elements, lref.elements, ltest.element_names, lref.element_names)
    ):
        assert type(ee_test) == type(ee_six)

        dtest = ee_test.to_dict()
        dref = ee_six.to_dict()

        for kk in dtest.keys():

            # Check if they are identical
            if np.isscalar(dref[kk]) and dtest[kk] == dref[kk]:
                continue

            if isinstance(dref[kk], dict):
                if kk=='fieldmap':
                    continue
                if kk=='boost_parameters':
                    continue
                if kk=='Sigmas_0_star':
                    continue

            # Check if the relative error is small
            val_test = dtest[kk]
            val_ref = dref[kk]
            if not np.isscalar(val_ref):
                if len(val_ref) != len(val_test):
                    diff_rel = 100
                else:
                    for iiii, (vvr, vvt) in enumerate(list(zip(val_ref, val_test))):
                        if not np.isclose(vvr, vvt, atol=atol, rtol=rtol):
                            print(f'Issue found on `{kk}[{iiii}]`')
                            diff_rel = 1000
                        else:
                            diff_rel = 0
            else:
                if val_ref > 0:
                    diff_rel = np.abs((val_test - val_ref)/val_ref)
                else:
                    diff_rel = 100

            if diff_rel < rtol:
                continue

            # Check if absolute error is small

            if not np.isscalar(val_ref) and len(val_ref) != len(val_test):
                diff_abs = 1000
            else:
                diff_abs = norm(np.array(val_test) - np.array(val_ref))
            if diff_abs > 0:
                print(f"{nn_test}[{kk}] - test:{dtest[kk]} six:{dref[kk]}")
            if diff_abs < atol:
                continue

            # Exception: drift length (100 um tolerance)
            if not(strict) and isinstance(ee_test, xt.Drift):
                if kk == "length":
                    if diff_abs < 1e-4:
                        continue

            # Exception: multipole lrad is not passed to sixtraxk
            if isinstance(ee_test, xt.Multipole):
                if kk == "length":
                    if np.abs(ee_test.hxl) + np.abs(ee_test.hyl) == 0.0:
                        continue
                if kk == "order" or kk == "inv_factorial_order":
                    # Checked through bal
                    continue
                if kk == 'knl' or kk == 'ksl' or kk == 'bal':
                    if len(val_ref) != len(val_test):
                        lmin = min(len(val_ref), len(val_test))
                        for vv in [val_ref,val_test]:
                            if len(vv)> lmin:
                                for oo in range(lmin, len(vv)):
                                    # we do not care about errors above 10
                                    if vv[oo] != 0 and oo < {'knl':10,
                                                            'ksl':10, 'bal':20}[kk]:
                                        raise ValueError(
                                            'Missing significant multipole strength')

                        val_ref = val_ref[:lmin]
                        val_test = val_test[:lmin]

                    if len(val_ref) == 0 and len(val_test) == 0:
                        continue
                    else:
                        for iiii, (vvr, vvt) in enumerate(list(zip(val_ref, val_test))):
                            if not np.isclose(vvr, vvt, atol=atol, rtol=rtol):
                                print(f'Issue found on `{kk}[{iiii}]`')
                                diff_rel = 1000
                                break
                            else:
                                diff_rel = 0
                        if diff_rel < rtol:
                            continue

            # Exception: correctors involved in lumi leveling
            passed_corr = False
            for nn_corr in [
                'mcbcv.5l8.b1', 'mcbyv.a4l8.b1', 'mcbxv.3l8',
                'mcbyv.4r8.b1', 'mcbyv.b5r8.b1',
                'mcbyh.b5l2.b1', 'mcbyh.4l2.b1', 'mcbxh.3l2', 'mcbyh.a4r2.b1',
                'mcbch.5r2.b1',
                'mcbcv.5l8.b2', 'mcbyv.a4l8.b2', 'mcbxv.3l8',
                'mcbyv.4r8.b2', 'mcbyv.b5r8.b2',
                'mcbyh.b5l2.b2', 'mcbyh.4l2.b2', 'mcbxh.3l2', 'mcbyh.a4r2.b2',
                'mcbch.5r2.b2', 'mcbch.a5r2.b2', 'mcbyh.4r2.b2', 'mcbxh.3r2',
                'mcbyh.a4l2.b2', 'mcbyh.5l2.b2', 'mcbyv.5r8.b2', 'mcbyv.a4r8.b2',
                'mcbxv.3r8', 'mcbyv.4l8.b2', 'mcbcv.b5l8.b2']:
                if nn_corr in nn_test and kk in ['knl','ksl','bal']:
                    assert len(val_ref)<=2
                    assert len(val_test)<=2
                    diff_rel = norm(val_test-val_ref)/norm(val_ref)
                    passed_corr = (diff_rel < 1e-2)
                    if passed_corr:
                        break
            if not(strict) and  passed_corr:
                continue

            # Exceptions BB4D (separations are recalculated)
            if not(strict) and isinstance(ee_test, xf.BeamBeamBiGaussian2D):
                if kk == "other_beam_shift_x":
                    if diff_abs / np.sqrt(dtest["other_beam_Sigma_11"]) < 0.01: # This is neede to accommodate different leveling routines (1% difference)
                        continue
                if kk == "other_beam_shift_y":
                    if diff_abs / np.sqrt(dtest["other_beam_Sigma_33"]) < 0.01:
                        continue
                if kk == "other_beam_Sigma_11":
                    if diff_rel < (1e-5)**2:
                        continue
                if kk == "other_beam_Sigma_33":
                    if diff_rel < (1e-5)**2:
                        continue
            if isinstance(ee_test, xf.BeamBeamBiGaussian2D):
                if kk == 'other_beam_q0' or kk == 'other_beam_num_particles':
                    # ambiguity due to old interface
                    if np.abs(ee_test.other_beam_num_particles*ee_test.other_beam_q0 -
                            ee_six.other_beam_num_particles*ee_six.other_beam_q0 ) < 1.: # charges
                        continue

            # Exceptions BB6D (angles and separations are recalculated)
            if not(strict) and isinstance(ee_test, xf.BeamBeamBiGaussian3D):
                if kk == "_cos_alpha":
                    if diff_abs < 10e-6:
                        continue
                if kk == "_sin_alpha":
                    if diff_abs < 10e-6:
                        continue
                if kk == "ref_shift_x" or kk == "other_beam_shift_x":
                    if diff_abs / np.sqrt(dtest["slices_other_beam_Sigma_11_star"][0]) < 0.015:
                        continue
                if kk == "ref_shift_y" or kk == "other_beam_shift_y":
                    if diff_abs / np.sqrt(dtest["slices_other_beam_Sigma_33_star"][0]) < 0.015:
                        continue
                if kk == "ref_shift_zeta":
                    if diff_abs <1e-5:
                        continue
                if kk == "ref_shift_pzeta":
                    if diff_abs <1e-5:
                        continue
                if kk == "ref_shift_px" or kk == 'ref_shift_py':
                    if diff_abs <30e-9:
                        continue
            if isinstance(ee_test, xt.XYShift):
                if kk in ['dx','dy']:
                    if diff_abs <1e-9:
                        continue
            if isinstance(ee_test, xt.SRotation):
                if kk in ['sin_z', 'cos_z', 'angle']:
                    if diff_abs <1e-9:
                        continue
            # If it got here it means that no condition above is met
            raise ValueError("Too large discrepancy!")
    print(
        f"""
    *******************************************************************

    The line {sequence} from test seq. and the line from reference are identical!
    *******************************************************************
    """
    )

    time.sleep(1)