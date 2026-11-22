# SCRIPT: HW-BUILD-V6 — Ladder_of_Twins_v2_20261117.html: his ball scripts (unchanged), MM-MATH-V1, FL-MATH-V2 (unchanged), HW-WORLD-V6, HW-FEED-V1, HW-LAYER-V6.
# The page head and the three "details" blocks are taken from the v2 page as built on 17 Nov 2026 (this file re-assembles the scripts behind them).
v2 = open('Ladder_of_Twins_v2_20261117.html', encoding='utf-8').read(); head = v2.split('<script')[0]
s = head + open('ball_blocks.html', encoding='utf-8').read() + '\n<script>' + open('../mm/mm_math_v1.js', encoding='utf-8').read() + '</script>\n<script>' + open('../sea/fl_math_v2.js', encoding='utf-8').read() + '</script>\n<script>' + open('hw_world_v6.js', encoding='utf-8').read() + '</script>\n<script>' + open('hw_feed_v1.js', encoding='utf-8').read() + '</script>\n<script>' + open('hw_layer_v6.js', encoding='utf-8').read() + '</script>\n</body></html>'
open('Ladder_of_Twins_v2_20261117.html', 'w', encoding='utf-8').write(s); print(len(s))
