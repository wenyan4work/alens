#!/usr/bin/env python

from pathlib import Path
from read_write_utils import read_sylinder_ascii_file, read_links_ascii_file, TriBendLink


syl_path = Path.cwd() / 'TubuleInitial_old.dat'
new_syl_path = Path.cwd() / 'TubuleInitial.dat'
syls = read_sylinder_ascii_file(syl_path)
links = read_links_ascii_file(syl_path)

# create new tribend links
tribend_links = []
for link in links[:-2]:  # assumes only one filament
    tribend_links += [TriBendLink(
        f'T {link._next_id} {link._prev_id} {link._next_id+1} 0 0 0')]


with new_syl_path.open('w') as tf:
    tf.write('Initial tubule config file\n\n')
    for syl in syls:
        tf.write(syl.to_string())
    for l in links:
        tf.write(l.to_string())
    for tbl in tribend_links:
        tf.write(tbl.to_string())
