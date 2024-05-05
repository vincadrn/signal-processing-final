from imageio_ffmpeg import read_frames, write_frames

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
            reader = read_frames(self._src_path)
            self._src_metadata = reader.__next__()
        except:
            raise
        finally:
            reader.close()

    def get_source_metadata(self):
        return self._src_metadata
    
    def transcode(
        self,
        path: str,
        src_path: str = None,
        codec: str = "h263p",
        dest_container: str = "avi",
        quality: int = 5,
    ):
        """
        Parameters:
            path (str): destination path for the transcoded video
            src_path (str): source path to the source video file
            codec (str): codec to choose from, default to `h263p`
            dest_container (str): output container format chosen (.avi, .mov, .mkv, etc.)
            quality (int): the quality of the output, 0 (least) - 10 (best), default to 5
        """
        if src_path:
            self.set_source_path(src_path)

        src = self._src_path
        dest = self._append_container_if_none(path, dest_container)

        try:
            reader = read_frames(src)
            reader.__next__()   # yield metadata first and discard. frames start in the next iteration

            writer = write_frames(
                dest,
                self._src_metadata["size"],
                fps=self._src_metadata["fps"],
                quality=quality,
                codec=codec,
                macro_block_size=8
            )
            writer.send(None)   # send nothing to init writer
            for frame in reader:
                writer.send(frame)
        except:
            raise
        finally:
            writer.close()
            reader.close()

    def _append_container_if_none(self, path: str, container: str):
        container_format = container.strip(".") if container is not None else ""

        if "." not in path:
            return f"{path}.{container_format}"
        
        return path
