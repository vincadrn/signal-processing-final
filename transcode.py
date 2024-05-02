import imageio.v3 as iio3

class Transcoder:
    def __init__(self):
        self._src_path = ""
        self._src_metadata = None

    def set_source_path(self, path: str):
        """
        `path`: original path to the source video
        """
        self._src_path = path
        try:
            src_file = iio3.imopen(self._src_path, "r")
            self._src_metadata = src_file.metadata()
        except:
            raise
        finally:
            src_file.close()
    
    def transcode(self, path: str, src_path: str = None, codec: str = "h263p", dest_container: str = "avi"):
        """
        `path`: destination path for the compressed and converted video
        `src_path`: source path to the source video file
        `codec`: codec to choose from, default to `h263`
        `container`: output container format chosen (.mp4, .3gp, .mkv, .avi, etc.)
        """
        if src_path:
            self.set_source_path(src_path)

        src = self._src_path
        dest = self._append_container_if_none(path, dest_container)

        with iio3.imopen(dest, "w", plugin="pyav") as out:
            out.init_video_stream(codec=codec)

            for frame in iio3.imiter(src):
                out.write_frame(frame)

    def _append_container_if_none(self, path: str, container: str):
        container_format = container.strip(".") if container is not None else ""

        if "." not in path:
            return f"{path}.{container_format}"
        
        return path
