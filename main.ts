// news-image-20261122 entry (Node 22, standard library only).
//
// The picture is entry.png, laid out in this repo as HTML/CSS
// (front-page.html) and rendered with the local
// chrome-headless-shell (render.sh): a 1024x1024 newspaper front
// page summing up Sunday 22 November 2026 — Tesla's FSD V15
// rollout with Reality View as the lead, the Nvidia SEC probe and
// 14% rout, Anthropic's wobbly second day as a public company,
// the Riemann confirmation standing, plus the day's other news in
// a footer strip. The program's only job is to place that exact
// file at the grader's output path, byte for byte.
//
// Run it twice and the bytes are identical: it reads one fixed file
// and writes it unchanged, with no network, no clock and no random
// input anywhere in the path.
//
// Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from 'node:crypto';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

const bytes = readFileSync(source);
mkdirSync(outDir, { recursive: true });
writeFileSync(target, bytes);

const digest = createHash('sha256').update(bytes).digest('hex');
console.log(`wrote ${target} (${bytes.length} bytes, sha256 ${digest})`);
