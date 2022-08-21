#!/usr/bin/env sh
# Attach to the first tmu session that has no attached clients.
# If there are no unattached sessions, then create a new session.
tmux attach -t $($(dirname $0)/./tmux-first-unattached-session.sh) 2> /dev/null || tmux
