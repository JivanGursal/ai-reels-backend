import subprocess

def run_ffmpeg(cmd: list[str]):
    """
    Safe FFmpeg runner for Render / Linux
    """
    process = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if process.returncode != 0:
        raise RuntimeError(process.stderr.decode())
