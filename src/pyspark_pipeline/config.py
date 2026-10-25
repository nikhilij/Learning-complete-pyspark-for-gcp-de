from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class PipelineConfig:
    raw_path: str = "data/raw"
    cleaned_path: str = "data/cleaned"
    curated_path: str = "data/curated"
    output_path: str = "data/output"
    project_id: str = "your-gcp-project-id"
    bucket_name: str = "your-gcs-bucket"


def build_paths(base_dir: str | Path) -> PipelineConfig:
    base = Path(base_dir)
    return PipelineConfig(
        raw_path=str(base / "raw"),
        cleaned_path=str(base / "cleaned"),
        curated_path=str(base / "curated"),
        output_path=str(base / "output"),
    )


__all__ = ["PipelineConfig", "build_paths"]
