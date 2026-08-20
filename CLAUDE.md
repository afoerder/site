# Claude Code: read MAINTENANCE.md first

Before editing anything in this repo, read `MAINTENANCE.md`. It covers the
publish workflow, two failure modes that have already caused live errors,
where the dust storm numbers are allowed to come from, and a list of
decisions that look like mistakes but are deliberate.

Three things that matter most:

1. **`rm -rf _site` before publishing.** Stale build output has put deleted
   draft pages on the live site.
2. **Numbers about the dust storm project come only from
   `~/Downloads/mars-dust-storm/LICENSED_NUMBERS.md`.** Not from memory,
   not from a conversation, not from an older version of the site. A
   retired figure reached the live site by traveling through chat.
3. **Don't "fix" the deliberate choices.** The broad headline, the withheld
   code, the literal status labels, and the limitations printed next to
   results are all intentional. Ask before changing one.
