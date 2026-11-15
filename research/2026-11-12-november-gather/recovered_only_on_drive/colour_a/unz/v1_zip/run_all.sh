#!/bin/bash
# runs every check script of the colour paper in this folder and keeps each printed output beside it
cd "$(dirname "$0")"
for s in t1_schrodinger_qgt t4_two_books_light color_projector_check cl1_colour_selects_leader f1_fall_colour_clock sound_music_checks bridge_checks w1_where_the_constant_goes w2_scale_and_sign c1_two_clock_model cycle_entropy_check light_matter_check weight_between_core_checks c4_richardson r30_colour_branching r30_colour_branching_opposite r30_colour_branching_widthsplit; do
  echo "== $s"; timeout 1500 python3 $s.py > ${s}_out.txt 2>&1; echo "exit $?"
done
