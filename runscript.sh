#!/bin/bash
qemu-system-x86_64 \
    -m 2048 \
    -enable-kvm \
    -cdrom android-x86_64-9.0-r2.iso \
    -boot d \
    -net nic \
    -net user,hostfwd=tcp::5555-:5555