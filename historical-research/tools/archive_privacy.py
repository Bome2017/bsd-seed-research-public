"""Inspect nested archives before evidence export; never extract to disk."""
import io
import tarfile
import zipfile


class ArchiveInspectionError(ValueError):
    pass


def contains_private_metadata(name, data, patterns, *, max_depth=5,
                              max_member_bytes=64*1024*1024,
                              max_total_bytes=256*1024*1024):
    inspected_bytes = 0

    def visit(label, blob, depth):
        nonlocal inspected_bytes
        inspected_bytes += len(blob)
        if inspected_bytes > max_total_bytes:
            raise ArchiveInspectionError('archive inspection byte budget exceeded')
        if any(rx.search(blob) for rx in patterns):
            return True
        is_tar = label.endswith(('.tar.gz', '.tgz', '.tar'))
        is_zip = label.endswith('.zip')
        if not is_tar and not is_zip:
            return False
        if depth >= max_depth:
            raise ArchiveInspectionError('archive nesting budget exceeded')
        try:
            if is_tar:
                with tarfile.open(fileobj=io.BytesIO(blob), mode='r:*') as archive:
                    for member in archive:
                        if member.isfile():
                            if member.size > max_member_bytes:
                                raise ArchiveInspectionError('archive member too large')
                            if visit(member.name, archive.extractfile(member).read(), depth+1):
                                return True
            else:
                with zipfile.ZipFile(io.BytesIO(blob)) as archive:
                    for member in archive.infolist():
                        if not member.is_dir():
                            if member.file_size > max_member_bytes:
                                raise ArchiveInspectionError('zip member too large')
                            if visit(member.filename, archive.read(member), depth+1):
                                return True
        except (tarfile.TarError, zipfile.BadZipFile, OSError, EOFError, RuntimeError) as exc:
            raise ArchiveInspectionError('archive could not be inspected') from exc
        return False

    return visit(name, data, 0)
