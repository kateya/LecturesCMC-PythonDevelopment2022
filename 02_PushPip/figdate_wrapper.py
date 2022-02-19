from argparse import ArgumentParser
import venv
import tempfile
import subprocess
import shutil

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("format", default="%Y %d %b, %A", nargs='?')
    parser.add_argument("font", default="graceful", nargs='?')
    args = parser.parse_args()

    env_dir = tempfile.mkdtemp()

    env = venv.create(env_dir, with_pip=True)

    subprocess.run([env_dir+"/bin/pip", "install", "pyfiglet"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    subprocess.run([env_dir+"/bin/python3", "-m", "figdate", args.format, args.font])

    shutil.rmtree(env_dir)


