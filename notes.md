


## Download the android device iso



## To run an android device via QEMU

    qemu-system-x86_64 \
        -m 2048 \
        -enable-kvm \
        -cdrom android-x86_64-9.0-r2.iso \
        -boot d \
        -net nic \
        -net user,hostfwd=tcp::5555-:5555




## Boot preconfigured iso using the python shell

    qemu-system-x86_64 -m 2048 -boot d -cdrom preconfigured_android.iso



    TODO RUN ANDROID IMG file from home .android on qemu