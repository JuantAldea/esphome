from __future__ import annotations

from pathlib import Path

import pytest

from .types import CompileOutput, ConfigWriter, OnlyCompileFunction


@pytest.mark.asyncio
async def test_cyclic_dependency(
    yaml_config: str, write_yaml_config: ConfigWriter, compile_only: OnlyCompileFunction
) -> None:
    """Compiles the test fixture YAML and asserts success while capturing output."""
    external_components_path = str(
        Path(__file__).parent / "fixtures" / "external_components"
    )

    yaml_config = yaml_config.replace(
        "EXTERNAL_COMPONENT_PATH", external_components_path
    )

    config_path: Path = await write_yaml_config(yaml_config, None)
    result: CompileOutput = await compile_only(config_path)

    assert result.returncode != 0
    assert "Circular dependency detected among components: cyclic_dep" in result.stderr
