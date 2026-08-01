"""
Configuration management for Autonomous Synthesis Planner.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class SearchConfig(BaseModel):
    """Configuration for synthesis route search."""

    max_depth: int = Field(
        default=5,
        ge=1,
        description="Maximum retrosynthetic search depth.",
    )

    beam_width: int = Field(
        default=10,
        ge=1,
        description="Beam width for heuristic search.",
    )

    max_routes: int = Field(
        default=20,
        ge=1,
        description="Maximum number of candidate routes to return.",
    )

    timeout: int = Field(
        default=300,
        ge=1,
        description="Maximum planning time in seconds.",
    )


class ScoringConfig(BaseModel):
    """Configuration for route scoring."""

    complexity_weight: float = Field(default=1.0, ge=0.0)

    confidence_weight: float = Field(default=1.0, ge=0.0)

    accessibility_weight: float = Field(default=1.0, ge=0.0)

    cost_weight: float = Field(default=1.0, ge=0.0)


class VisualizationConfig(BaseModel):
    """Visualization settings."""

    enabled: bool = True

    export_format: str = "png"

    dpi: int = Field(default=300, ge=72)


class LoggingConfig(BaseModel):
    """Logging configuration."""

    level: str = "INFO"

    log_to_file: bool = False

    log_directory: Path = Path("logs")


class AppConfig(BaseModel):
    """Global application configuration."""

    model_config = ConfigDict(validate_assignment=True)

    search: SearchConfig = SearchConfig()

    scoring: ScoringConfig = ScoringConfig()

    visualization: VisualizationConfig = VisualizationConfig()

    logging: LoggingConfig = LoggingConfig()


DEFAULT_CONFIG = AppConfig()
