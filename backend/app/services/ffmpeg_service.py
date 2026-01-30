import subprocess


def run_ffmpeg(cmd: list[str]):
    subprocess.run(cmd, check=True)
