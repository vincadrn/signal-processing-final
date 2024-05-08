import sys
import imageio_ffmpeg
import subprocess as sp


class InputSource:
    @staticmethod
    def get_cam_inputname(index):
        if sys.platform.startswith("win"):
            CAM_FORMAT = "dshow"  # dshow or vfwcap
        elif sys.platform.startswith("linux"):
            CAM_FORMAT = "video4linux2"
        elif sys.platform.startswith("darwin"):
            CAM_FORMAT = "avfoundation"
        else:  # pragma: no cover
            CAM_FORMAT = "unknown-cam-format"

        if sys.platform.startswith("linux"):
            name_ = f"<video{index}>"
            return "/dev/" + name[1:-1]

        elif sys.platform.startswith("win"):
            # Ask ffmpeg for list of dshow device names
            ffmpeg_api = imageio_ffmpeg
            cmd = [
                ffmpeg_api.get_ffmpeg_exe(),
                "-list_devices",
                "true",
                "-f",
                CAM_FORMAT,
                "-i",
                "dummy",
            ]
            # Set `shell=True` in sp.run to prevent popup of a command
            # line window in frozen applications. Note: this would be a
            # security vulnerability if user-input goes into the cmd.
            # Note that the ffmpeg process returns with exit code 1 when
            # using `-list_devices` (or `-list_options`), even if the
            # command is successful, so we set `check=False` explicitly.
            completed_process = sp.run(
                cmd,
                stdout=sp.PIPE,
                stderr=sp.PIPE,
                encoding="utf-8",
                shell=True,
                check=False,
            )

            # Return device name at index
            try:
                name = InputSource._parse_device_names(completed_process.stderr)[index]
            except IndexError:
                raise IndexError("No ffdshow camera at index %i." % index)
            return "video=%s" % name

        elif sys.platform.startswith("darwin"):
            name = str(index)
            return name

        else:  # pragma: no cover
            return "??"
    
    @staticmethod
    def _parse_device_names(ffmpeg_output):
        """Parse the output of the ffmpeg -list-devices command"""
        device_names = []
        in_video_devices = False
        for line in ffmpeg_output.splitlines():
            if line.startswith("[dshow"):
                line = line.split("]", 1)[1].strip()
                if in_video_devices and line.startswith('"'):
                    friendly_name = line[1:-1]
                    device_names.append([friendly_name, ""])
                elif in_video_devices and line.lower().startswith("alternative name"):
                    alt_name = line.split(" name ", 1)[1].strip()[1:-1]
                    if sys.platform.startswith("win"):
                        alt_name = alt_name.replace("&", "^&")
                    else:
                        alt_name = alt_name.replace("&", "\\&")
                    device_names[-1][-1] = alt_name
                elif "video devices" in line:
                    in_video_devices = True
                elif "devices" in line:
                    # set False for subsequent "devices" sections
                    in_video_devices = False
        device_names2 = []
        for friendly_name, alt_name in device_names:
            if friendly_name not in device_names2:
                device_names2.append(friendly_name)
            elif alt_name:
                device_names2.append(alt_name)
            else:
                device_names2.append(friendly_name)  # duplicate, but not much we can do
        return device_names2
