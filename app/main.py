import os
def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    target_file = parts[2]


    if source_file == target_file:
        return

    with open(source_file, "r") as sf, open(target_file, "w") as tf:
        tf.write(sf.read())
