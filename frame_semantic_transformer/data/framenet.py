from __future__ import annotations
from functools import lru_cache
from typing import Any, Iterable, Sequence, Mapping
import nltk

from nltk.corpus import framenet as fn


class InvalidFrameError(Exception):
    pass


def ensure_framenet_downloaded() -> None:
    nltk.download("framenet_v17")


def is_valid_frame(frame: str) -> bool:
    return frame in get_all_valid_frame_names()


def get_frame_element_names(frame: str) -> Iterable[str]:
    if not is_valid_frame(frame):
        raise InvalidFrameError(frame)
    return fn.frame(frame).FE.keys()


@lru_cache(1)
def get_all_valid_frame_names() -> set[str]:
    return {frame.name for frame in fn.frames()}


def get_fulltext_docs() -> Sequence[Mapping[str, Any]]:
    return fn.docs()
