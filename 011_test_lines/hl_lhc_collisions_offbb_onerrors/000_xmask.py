correction_setup = {}
correction_setup['lhcb1'] = {
    'IR1 left': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.r8.b1',
        end='e.ds.l1.b1',
        vary=(
            'corr_co_acbh14.l1b1',
            'corr_co_acbh12.l1b1',
            'corr_co_acbv15.l1b1',
            'corr_co_acbv13.l1b1',
            ),
        targets=('e.ds.l1.b1',),
    ),
    'IR1 right': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r1.b1',
        end='s.ds.l2.b1',
        vary=(
            'corr_co_acbh13.r1b1',
            'corr_co_acbh15.r1b1',
            'corr_co_acbv12.r1b1',
            'corr_co_acbv14.r1b1',
            ),
        targets=('s.ds.l2.b1',),
    ),
    'IR5 left': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.r4.b1',
        end='e.ds.l5.b1',
        vary=(
            'corr_co_acbh14.l5b1',
            'corr_co_acbh12.l5b1',
            'corr_co_acbv15.l5b1',
            'corr_co_acbv13.l5b1',
            ),
        targets=('e.ds.l5.b1',),
    ),
    'IR5 right': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r5.b1',
        end='s.ds.l6.b1',
        vary=(
            'corr_co_acbh13.r5b1',
            'corr_co_acbh15.r5b1',
            'corr_co_acbv12.r5b1',
            'corr_co_acbv14.r5b1',
            ),
        targets=('s.ds.l6.b1',),
    ),
    'IP1': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l1.b1',
        end='s.ds.r1.b1',
        vary=(
            'corr_co_acbch6.l1b1',
            'corr_co_acbcv5.l1b1',
            'corr_co_acbch5.r1b1',
            'corr_co_acbcv6.r1b1',
            'corr_co_acbyhs4.l1b1',
            'corr_co_acbyhs4.r1b1',
            'corr_co_acbyvs4.l1b1',
            'corr_co_acbyvs4.r1b1',
        ),
        targets=('ip1', 's.ds.r1.b1'),
    ),
    'IP2': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l2.b1',
        end='s.ds.r2.b1',
        vary=(
            'corr_co_acbyhs5.l2b1',
            'corr_co_acbchs5.r2b1',
            'corr_co_acbyvs5.l2b1',
            'corr_co_acbcvs5.r2b1',
            'corr_co_acbyhs4.l2b1',
            'corr_co_acbyhs4.r2b1',
            'corr_co_acbyvs4.l2b1',
            'corr_co_acbyvs4.r2b1',
        ),
        targets=('ip2', 's.ds.r2.b1'),
    ),
    'IP5': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l5.b1',
        end='s.ds.r5.b1',
        vary=(
            'corr_co_acbch6.l5b1',
            'corr_co_acbcv5.l5b1',
            'corr_co_acbch5.r5b1',
            'corr_co_acbcv6.r5b1',
            'corr_co_acbyhs4.l5b1',
            'corr_co_acbyhs4.r5b1',
            'corr_co_acbyvs4.l5b1',
            'corr_co_acbyvs4.r5b1',
        ),
        targets=('ip5', 's.ds.r5.b1'),
    ),
    'IP8': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l8.b1',
        end='s.ds.r8.b1',
        vary=(
            'corr_co_acbch5.l8b1',
            'corr_co_acbyhs4.l8b1',
            'corr_co_acbyhs4.r8b1',
            'corr_co_acbyhs5.r8b1',
            'corr_co_acbcvs5.l8b1',
            'corr_co_acbyvs4.l8b1',
            'corr_co_acbyvs4.r8b1',
            'corr_co_acbyvs5.r8b1',
        ),
        targets=('ip8', 's.ds.r8.b1'),
    ),
}

correction_setup['lhcb2'] = {
    'IR1 left': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l1.b2',
        end='e.ds.r8.b2',
        vary=(
            'corr_co_acbh13.l1b2',
            'corr_co_acbh15.l1b2',
            'corr_co_acbv12.l1b2',
            'corr_co_acbv14.l1b2',
            ),
        targets=('e.ds.r8.b2',),
    ),
    'IR1 right': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.l2.b2',
        end='s.ds.r1.b2',
        vary=(
            'corr_co_acbh12.r1b2',
            'corr_co_acbh14.r1b2',
            'corr_co_acbv13.r1b2',
            'corr_co_acbv15.r1b2',
            ),
        targets=('s.ds.r1.b2',),
    ),
    'IR5 left': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='e.ds.l5.b2',
        end='e.ds.r4.b2',
        vary=(
            'corr_co_acbh13.l5b2',
            'corr_co_acbh15.l5b2',
            'corr_co_acbv12.l5b2',
            'corr_co_acbv14.l5b2',
            ),
        targets=('e.ds.r4.b2',),
    ),
    'IR5 right': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.l6.b2',
        end='s.ds.r5.b2',
        vary=(
            'corr_co_acbh12.r5b2',
            'corr_co_acbh14.r5b2',
            'corr_co_acbv13.r5b2',
            'corr_co_acbv15.r5b2',
            ),
        targets=('s.ds.r5.b2',),
    ),
    'IP1': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r1.b2',
        end='e.ds.l1.b2',
        vary=(
            'corr_co_acbch6.r1b2',
            'corr_co_acbcv5.r1b2',
            'corr_co_acbch5.l1b2',
            'corr_co_acbcv6.l1b2',
            'corr_co_acbyhs4.l1b2',
            'corr_co_acbyhs4.r1b2',
            'corr_co_acbyvs4.l1b2',
            'corr_co_acbyvs4.r1b2',
        ),
        targets=('ip1', 'e.ds.l1.b2',),
    ),
    'IP2': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r2.b2',
        end='e.ds.l2.b2',
        vary=(
            'corr_co_acbyhs5.l2b2',
            'corr_co_acbchs5.r2b2',
            'corr_co_acbyvs5.l2b2',
            'corr_co_acbcvs5.r2b2',
            'corr_co_acbyhs4.l2b2',
            'corr_co_acbyhs4.r2b2',
            'corr_co_acbyvs4.l2b2',
            'corr_co_acbyvs4.r2b2',
        ),
        targets=('ip2', 'e.ds.l2.b2'),
    ),
    'IP5': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r5.b2',
        end='e.ds.l5.b2',
        vary=(
            'corr_co_acbch6.r5b2',
            'corr_co_acbcv5.r5b2',
            'corr_co_acbch5.l5b2',
            'corr_co_acbcv6.l5b2',
            'corr_co_acbyhs4.l5b2',
            'corr_co_acbyhs4.r5b2',
            'corr_co_acbyvs4.l5b2',
            'corr_co_acbyvs4.r5b2',
        ),
        targets=('ip5', 'e.ds.l5.b2',),
    ),
    'IP8': dict(
        ref_with_knobs={'on_corr_co': 0, 'on_disp': 0},
        start='s.ds.r8.b2',
        end='e.ds.l8.b2',
        vary=(
            'corr_co_acbchs5.l8b2',
            'corr_co_acbyhs5.r8b2',
            'corr_co_acbcvs5.l8b2',
            'corr_co_acbyvs5.r8b2',
            'corr_co_acbyhs4.l8b2',
            'corr_co_acbyhs4.r8b2',
            'corr_co_acbyvs4.l8b2',
            'corr_co_acbyvs4.r8b2',
        ),
        targets=('ip8', 'e.ds.l8.b2',),
    ),
}


import json
for nn in ['lhcb1', 'lhcb2']:
    with open(f'corr_co_{nn}.json', 'w') as fid:
        json.dump(correction_setup[nn], fid, indent=4)

from cpymad.madx import Madx
import xtrack as xt

import xmask as xm
import xmask.lhc as xmlhc

# Import user-defined optics-specific tools
import optics_specific_tools_hlhc14 as ost

# Read config file
with open('config.yaml','r') as fid:
    config = xm.yaml.load(fid)
config_mad_model = config['config_mad']

# Make mad environment
xm.make_mad_environment(links=config_mad_model['links'])

# Start mad
mad_b1b2 = Madx(command_log="mad_collider.log")
mad_b4 = Madx(command_log="mad_b4.log")

# Build sequences
ost.build_sequence(mad_b1b2, mylhcbeam=1)
ost.build_sequence(mad_b4, mylhcbeam=4)

# Apply optics (only for b1b2, b4 will be generated from b1b2)
ost.apply_optics(mad_b1b2, optics_file=config_mad_model['optics_file'])

# Build xsuite collider
collider = xmlhc.build_xsuite_collider(
    sequence_b1=mad_b1b2.sequence.lhcb1,
    sequence_b2=mad_b1b2.sequence.lhcb2,
    sequence_b4=mad_b4.sequence.lhcb2,
    beam_config=config_mad_model['beam_config'],
    enable_imperfections=config_mad_model['enable_imperfections'],
    enable_knob_synthesis=config_mad_model['enable_knob_synthesis'],
    pars_for_imperfections=config_mad_model['pars_for_imperfections'],
    ver_lhc_run=config_mad_model['ver_lhc_run'],
    ver_hllhc_optics=config_mad_model['ver_hllhc_optics'])

# Save to file
collider.to_json('collider_00_from_mad.json')


# Load collider anf build trackers
collider.build_trackers()

# Read knobs and tuning settings from config file
with open('config.yaml','r') as fid:
    config = xm.yaml.load(fid)
conf_knobs_and_tuning = config['config_knobs_and_tuning']

# Set all knobs (crossing angles, dispersion correction, rf, crab cavities,
# experimental magnets, etc.)
for kk, vv in conf_knobs_and_tuning['knob_settings'].items():
    collider.vars[kk] = vv

# Tunings
for line_name in ['lhcb1', 'lhcb2']:

    knob_names = conf_knobs_and_tuning['knob_names'][line_name]

    targets = {
        'qx': conf_knobs_and_tuning['qx'][line_name],
        'qy': conf_knobs_and_tuning['qy'][line_name],
        'dqx': conf_knobs_and_tuning['dqx'][line_name],
        'dqy': conf_knobs_and_tuning['dqy'][line_name],
    }

    xm.machine_tuning(line=collider[line_name],
        enable_closed_orbit_correction=True,
        enable_linear_coupling_correction=True,
        enable_tune_correction=True,
        enable_chromaticity_correction=True,
        knob_names=knob_names,
        targets=targets,
        line_co_ref=collider[line_name+'_co_ref'],
        co_corr_config=conf_knobs_and_tuning['closed_orbit_correction'][line_name],
        tune_knob_step=conf_knobs_and_tuning['tune_knob_step'],
        chromaticity_knob_step=conf_knobs_and_tuning['chromaticity_knob_step'],
        tune_tol=conf_knobs_and_tuning['tune_tol'],
        chromaticity_tol=conf_knobs_and_tuning['chromaticity_tol'],)

collider.to_json('collider_02_tuned_bb_off.json')


